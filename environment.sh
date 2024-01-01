#!/bin/bash

: << 'comment'
The set up herein is in line with the Dockerfile set up.  Both use the same
requirements.txt file to create an environment.
comment

# The environment in focus
prefix=/opt/miniconda3/envs/systems

: << 'delete'
  Delete the existing <systems> environment
delete
conda remove -y --prefix $prefix --all

: << 'rebuild'
  Rebuild environment <systems> via a requirements.txt file
rebuild
conda env create -f environment.yml -p $prefix
