#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/knng_gen/__DATASET___knng_gen_size___SIZE___%j.log


source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 
export OPENBLAS_NUM_THREADS=1

python3 ~/repos/graph-visualization/tsne/knng_generation.py -input $SCRATCH/datasets/graph-viz/__DATASET__ -output $SCRATCH/datasets/graph-viz/__DATASET__ -dataset __DATASET__ -size __SIZE__
