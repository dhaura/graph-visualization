#!/bin/bash
#SBATCH --qos=regular
#SBATCH --time=02:30:00
#SBATCH --nodes=1
#SBATCH --constraint=cpu
#SBATCH --output=logs/openTSNE/__DATASET___p___PERPLEXITY___size___SIZE___%j.log

export OMP_NUM_THREADS=128
export OPENBLAS_NUM_THREADS=128
export MKL_NUM_THREADS=128
export NUMEXPR_NUM_THREADS=128

module load conda
conda activate tsne-env

export PYTHONUNBUFFERED=1 

python3 ~/repos/graph-visualization/tsne/openTSNE_tsne_visualization_large_scale.py -input __INPUT_FILE__ -output __OUTPUT_PATH__ -n_jobs 128 -perplexity __PERPLEXITY__
