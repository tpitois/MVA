# Modeling the Shape of the Brain Connectome via Deep Neural Networks

**Course:** Geometric Data Analysis (Master MVA)  
**Instructor:** Jean Feydy  

## Project Overview

The goal of this project is to study and reproduce the findings of the paper [Modeling the Shape of the Brain Connectome via Deep Neural Networks](https://arxiv.org/abs/2203.06122) (Dai et al., 2023).

This paper proposes a method to estimate a Riemannian metric compatible with Diffusion-Weighted Imaging (DWI) data, allowing for the modeling of neural connections as geodesics on a manifold.

## Repository Structure

Due to computational constraints, we focus exclusively on the **2D implementation** of the model. Consequently, this repository is a fork of [Metric-Cnn-2D-IPMI](https://github.com/aarentai/Metric-Cnn-2D-IPMI).

**Our Contribution:**
Our work is concentrated in the [`Notebooks`](Notebooks) directory. We provide a set of notebooks to:
1.  **Reproduce** the original authors' results on synthetic data.
2.  **Extend** the experiments to new, custom-generated vector fields (branching, crossing).
3.  **Explore** real-world data concepts (HCP).

## Notebooks & Experiments

For reproducibility, **ready-to-run Colab links** are provided for each experiment.

| Experiment                   | Description                                                                                                                        | Link                                                                                                                                                                                              |
|:-----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **0. Original Reproduction** | Reproduction of the "Braid" experiment using the original `.nhdr` files provided by the authors.                                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/Metric-Cnn-2D-IPMI/blob/main/Notebooks/00_2_braids_file.ipynb)      |
| **1. Generated Braid**       | Reproduction of the "Braid" experiment using our own synthetic data generator (Python implementation of the trigonometric fields). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/Metric-Cnn-2D-IPMI/blob/main/Notebooks/01_2_braids_generated.ipynb) |
| **2. Branching Fibers**      | Testing the model on a custom 3-fiber branching structure (diverging paths).                                                       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/Metric-Cnn-2D-IPMI/blob/main/Notebooks/02_3_branching.ipynb)        |
| **3. Branching & Crossing**  | Stress-testing the model on complex fields combining branching and crossings.                                                      | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/Metric-Cnn-2D-IPMI/blob/main/Notebooks/03_3_branching_cross.ipynb)  |
| **4. HCP Data Exploration**  | Exploration and visualization of Human Connectome Project (DWI) data structures.                                                   | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/Metric-Cnn-2D-IPMI/blob/main/Notebooks/04_explore_hcp.ipynb)        |
