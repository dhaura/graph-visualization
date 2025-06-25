#!/bin/bash
#SBATCH --qos=regular
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/openTSNE/__DATASET___p___PERPLEXITY___%j.log

export OMP_NUM_THREADS=64
export OPENBLAS_NUM_THREADS=64
export MKL_NUM_THREADS=64
export NUMEXPR_NUM_THREADS=64

module load conda
conda activate tsne-env

export PYTHONUNBUFFERED=1 

python3 ~/repos/graph-visualization/tsne/openTSNE_tsne_visualization.py -input __INPUT_FILE__ -labels __LABEL_FILE__ -input_type __INPUT_TYPE__ -output __OUTPUT_FILE__ -n_jobs 64 -perplexity __PERPLEXITY__
