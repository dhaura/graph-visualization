#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/link_pred/__DATASET___link_pred_size___SIZE___%j.log


source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 
export OPENBLAS_NUM_THREADS=32

python3 ~/repos/graph-visualization/tsne/link_prediction_large_scale.py __INPUT_FILE__ 1 __EMBED_FILE__ __DIM__
