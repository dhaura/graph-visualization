#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=00:30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/scikit-learn/YANDEX_p_50_size_20000_%j.log

export OMP_NUM_THREADS=64
export OPENBLAS_NUM_THREADS=64
export MKL_NUM_THREADS=64
export NUMEXPR_NUM_THREADS=64

source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 

python3 ~/repos/graph-visualization/tsne/scikit-learn_tsne_visualization_large_scale.py -input /pscratch/sd/d/dhaura/datasets/graph-viz/YANDEX/YANDEX_subset_20000.txt -n_jobs 64 -perplexity 50 -n_components 2 -max_iter 1000
