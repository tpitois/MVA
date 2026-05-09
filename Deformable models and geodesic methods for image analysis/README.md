# Finsler-Laplace-Beltrami Operators with Application to Shape Analysis

**Course:** Geodesic Methods and Deformable Models  
**Instructor:** Laurent D. Cohen

## Project Overview

The goal of this project is to study and implement the findings of the paper *[Finsler-Laplace-Beltrami Operators with Application to Shape Analysis](https://arxiv.org/pdf/2404.03999)* by Simon Weber, Thomas Dagès, Maolin Gao, and Daniel Cremers.

This paper proposes an approach using Finsler geometry to generalize standard geometric operators (such as the Laplace-Beltrami operator), allowing for a more refined and directionally-aware analysis of surfaces, shape matching, and deformations.

📄 **[Read the full project report here (report.pdf)](https://github.com/tpitois/MVA/blob/main/Deformable%20models%20and%20geodesic%20methods%20for%20image%20analysis/docs/report.pdf)**

## Notebooks & Experiments

| Experiment              | Description                                                                                                                                                         | Link                                                                                                                                                                           |
|:------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Heat Diffusion**      | Mathematical implementation of the FLBO and visual simulation of heat diffusion on 3D meshes.                                                                       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/FLBO/blob/master/notebooks/heat_diffusion.ipynb)           |
| **Shape Correspondence**| Training and evaluation of a neural network leveraging FLBO for convolutions on the TOSCA dataset, featuring 3D shape correspondence visualization and PCK curves. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tpitois/FLBO/blob/master/notebooks/train.ipynb) |
