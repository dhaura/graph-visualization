#!/bin/bash

INPUT_FILE_PREFIX="$SCRATCH/datasets/graph-viz/SIFT/"
EMBED_FILE_PREFIX="$SCRATCH/datasets/graph-viz/output/scikit-learn/embeddings/"
DIM=128
INIT_DATASET_SIZE=20000
PERPLEXITY=50

for i in {5..6}; do
    DATASET_SIZE=$((2**i * INIT_DATASET_SIZE))

    if [ $DATASET_SIZE -gt 1000000 ]; then
        DATASET_SIZE=1000000
    fi

    INPUT_FILE="${INPUT_FILE_PREFIX}SIFT_size_${DATASET_SIZE}_adjacency.mtx"
    EMBED_FILE="${EMBED_FILE_PREFIX}SIFT_embed_p_${PERPLEXITY}_size_${DATASET_SIZE}.txt"
    TEMP_SCRIPT="temp_link_pred_SIFT_p_${PERPLEXITY}_size_${DATASET_SIZE}.sh"

    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/link_pred_template.sh | \
    sed "s|__DIM__|$DIM|" | \
    sed "s|__SIZE__|$DATASET_SIZE|" | \
    sed "s|__DATASET__|SIFT|" | \
    sed "s|__INPUT_FILE__|$INPUT_FILE|" | \
    sed "s|__EMBED_FILE__|$EMBED_FILE|" > $TEMP_SCRIPT

    sbatch $TEMP_SCRIPT
    sleep 1
done
