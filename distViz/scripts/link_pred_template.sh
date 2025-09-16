#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/link_pred/BIG_ANN_link_pred_size_1000000_%j.log


source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 
export OPENBLAS_NUM_THREADS=32

python3 ~/repos/graph-visualization/distViz/link_prediction_large_scale.py ~/repos/graph-visualization/distViz/output/knng.mtx 1 ~/repos/graph-visualization/distViz/output/embedding.txt 128
