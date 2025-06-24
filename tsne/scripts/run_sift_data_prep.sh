#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/data_prep/sift_data_prep_%j.log


source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 

python3 ~/repos/graph-visualization/tsne/txt_data_preparation.py -input /global/cfs/cdirs/m4293/visulaization_paper/large_scale/SIFT/sift.txt -output $SCRATCH/datasets/graph-viz/SIFT -dataset SIFT
