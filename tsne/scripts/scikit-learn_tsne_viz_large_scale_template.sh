#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/scikit-learn/__DATASET___p_50_size___SIZE___%j.log

export OMP_NUM_THREADS=64
export OPENBLAS_NUM_THREADS=64
export MKL_NUM_THREADS=64
export NUMEXPR_NUM_THREADS=64

source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 

python3 ~/repos/graph-visualization/tsne/scikit-learn_tsne_visualization_large_scale.py -input __INPUT_FILE__ -n_jobs 64 -perplexity 50 -n_components 2 -max_iter __MAX_ITER__
