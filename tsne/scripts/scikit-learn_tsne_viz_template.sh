#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/scikit-learn/__DATASET___p___PERPLEXITY___%j.log

export OMP_NUM_THREADS=64
export OPENBLAS_NUM_THREADS=64
export MKL_NUM_THREADS=64
export NUMEXPR_NUM_THREADS=64

source ~/repos/graph-visualization/venv/bin/activate

export PYTHONUNBUFFERED=1 

python3 ~/repos/graph-visualization/tsne/scikit-learn_tsne_visualization.py -input __INPUT_FILE__ -labels __LABEL_FILE__ -input_type __INPUT_TYPE__ -output __OUTPUT_FILE__ -n_jobs 64 -perplexity __PERPLEXITY__ -n_components 2 -max_iter __MAX_ITER__
