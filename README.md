# CNT Growth Simulation with NNP

This repository aims to reproduce the study on carbon nanotube (CNT) growth using Neural Network Potentials (NNPs), as described in the following paper:

- [Edge Dynamics in Iron-Cluster Catalyzed Growth of Single-Walled Carbon Nanotubes Revealed by Molecular Dynamics Simulations based on a Neural Network Potential (arXiv:2302.09264)](https://arxiv.org/abs/2302.09264)

## Overview

We attempt to trace the CNT growth process using:
- [fairchem](https://github.com/facebookresearch/fairchem): an open-source neural network potential developed by FAIR
- [ASE (Atomic Simulation Environment)](https://wiki.fysik.dtu.dk/ase/): a Python library for setting up, running, and analyzing atomistic simulations

## Goal

- Evaluate whether a general-purpose open-source NNP (such as `fairchem`) can reproduce the results of CNT growth simulations originally performed using a custom, CNT-specific NNP.
- Develop reproducible simulation scripts for CNT growth using only open-source tools.


## Requirements

This project uses:

- Python 3.12
- fairchem
- ASE

Please install necessary packages via pip or conda.

