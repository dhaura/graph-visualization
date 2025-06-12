#!/bin/bash
#SBATCH --qos=debug
#SBATCH --time=30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/openTSNE/fashionMNIST_p___PERPLEXITY__n___N_NEIGHBORS___%j.log

export OMP_NUM_THREADS=64
export OPENBLAS_NUM_THREADS=64
export MKL_NUM_THREADS=64
export NUMEXPR_NUM_THREADS=64

module load conda
conda activate tsne-env

python3 ~/repos/graph-visualization/tsne/openTSNE_tsne_visualization.py -input __INPUT_FILE__ -labels __LABEL_FILE__ -output __OUTPUT_FILE__ -n_jobs 64 -perplexity __PERPLEXITY__ -n_neighbors __N_NEIGHBORS__
