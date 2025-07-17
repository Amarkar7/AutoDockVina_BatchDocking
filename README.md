# AutoDock Vina: Batch Docking Workflow for Multiple Ligands

This repository provides a complete pipeline for high-throughput molecular docking of multiple ligands to a single receptor using **AutoDock Vina**. The workflow includes:
1. Protein preparation using Autodock
2. Ligand cleaning and 3D conformer generation using RDKit
3. Format conversion to `.pdbqt` using OpenBabel
4. Automated docking using a Perl script
5. Extraction of top 5 ligands with the best binding affinities

## Requirements

Install the following:

```bash
conda create -n vina_env python=3.9 rdkit openbabel -c conda-forge
conda activate vina_env
sudo apt install autodock-vina
# AutoDockVina_BatchDocking
A complete step-by-step pipeline to dock multiple ligands using AutoDock Vina. Includes ligand preparation, file format conversion, batch docking, and result extraction.
