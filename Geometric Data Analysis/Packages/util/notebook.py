import torch
import numpy as np

from torch.utils.data import DataLoader, Dataset
from util import riemann, tensors


class ImageDataset(Dataset):
    def __init__(self, vector_fields, masks):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        if len(vector_fields) == 1:
            self.sample = {
                'vector_field':vector_fields.permute(2, 0, 1).to(device).float() * 1000.0,
                'mask': masks.permute(1, 0).float().to(device).unsqueeze(0)
            }
        else:
            self.sample = {
                'vector_field': torch.cat(
                    [
                        vector_field.permute(2, 0, 1).to(device).float() * 1000.0
                        for vector_field in vector_fields
                    ],
                    dim=0
                ), 'masks': [
                    mask.permute(1, 0).float().to(device).unsqueeze(0)
                    for mask in masks
                ]
            }

    def __len__(self):
        return 1

    def __getitem__(self, idx):
        return self.sample


def matrix_exp_2d(A):
    """
    Construct positive definite matrix from symmetric matrix field A
    Args:
        A, torch.Tensor
    Returns:
        psd, torch.Tensor
    """
    I = torch.zeros_like(A, device=A.device)
    I[..., 0, 0] = 1
    I[..., 1, 1] = 1

    s = ((A[..., 0, 0] + A[..., 1, 1]) / 2.).unsqueeze(-1).unsqueeze(-1)
    q = torch.sqrt(-torch.det(A - torch.mul(s, I))).unsqueeze(-1).unsqueeze(-1)

    psd = torch.exp(s) * (torch.mul((torch.cosh(q) - s * torch.sinh(q) / q), I) + torch.sinh(q) / q * A)
    return psd


def pde(u, vector_lin, mask, differential_accuracy=2):
    s = tensors.lin2mat(u)
    metric_mat = matrix_exp_2d(s)
    nabla_vv = riemann.covariant_derivative_2d(vector_lin, metric_mat, mask, differential_accuracy=differential_accuracy)

    return nabla_vv


def make_square(vector_field, mask):
    """
    Rend les tableaux carrés en ajoutant du padding (zéros)
    autour de la dimension la plus petite pour centrer l'image.
    """
    h, w = mask.shape
    target_size = max(h, w)
    target_size += (4 - target_size) % 4

    # Calcul du padding nécessaire (total)
    pad_h = target_size - h
    pad_w = target_size - w

    # Répartition du padding (Haut/Bas et Gauche/Droite)
    # On utilise // 2 pour centrer l'image
    pad_top = pad_h // 2
    pad_bottom = pad_h - pad_top
    pad_left = pad_w // 2
    pad_right = pad_w - pad_left

    # 1. Padding du Mask (2D : Height, Width)
    # mode='constant', constant_values=0 ajoute des False (0) autour
    square_mask = np.pad(mask,
                         ((pad_top, pad_bottom), (pad_left, pad_right)),
                         mode='constant', constant_values=0)

    # 2. Padding du Champ de Vecteur (3D : Height, Width, Channels)
    # Attention : on ne veut PAS ajouter de padding sur la 3ème dimension (les composantes x,y)
    # Donc on met (0, 0) pour la dernière dimension
    square_vectors = np.pad(vector_field,
                            ((pad_top, pad_bottom), (pad_left, pad_right), (0, 0)),
                            mode='constant', constant_values=0)

    return square_vectors, square_mask

def disp_path(ax, x, y, label, color, size, alpha):
    ax.scatter(x[::1], y[::1], c=color, s=size, alpha=alpha, label=label, zorder=1)