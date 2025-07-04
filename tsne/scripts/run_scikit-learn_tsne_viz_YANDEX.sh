#!/bin/bash

INPUT_FILE_PREFIX="/pscratch/sd/d/dhaura/datasets/graph-viz/YANDEX/YANDEX_subset"
OUTPUT_PATH_PREFIX="/pscratch/sd/d/dhaura/datasets/graph-viz/output/scikit-learn/embeddings/YANDEX_embed"
MAX_ITER=1000
INIT_DATASET_SIZE=20000
PERPLEXITY=50

for i in {0..6}; do
    DATASET_SIZE=$((2**i * INIT_DATASET_SIZE))

    if [ $DATASET_SIZE -gt 1000000 ]; then
        DATASET_SIZE=1000000
    fi

    INPUT_FILE="${INPUT_FILE_PREFIX}_${DATASET_SIZE}.txt"
    OUTPUT_PATH="${OUTPUT_PATH_PREFIX}_p_${PERPLEXITY}_size_${DATASET_SIZE}.txt"
    TEMP_SCRIPT="temp_scikit-learn_tsne_viz_YANDEX_p_${PERPLEXITY}_size_${DATASET_SIZE}.sh"

    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/scikit-learn_tsne_viz_large_scale_template.sh | \
    sed "s|__DATASET__|YANDEX|" | \
    sed "s|__PERPLEXITY__|$PERPLEXITY|" | \
    sed "s|__MAX_ITER__|$MAX_ITER|" | \
    sed "s|__SIZE__|$DATASET_SIZE|" | \
    sed "s|__INPUT_FILE__|$INPUT_FILE|" | \
    sed "s|__OUTPUT_PATH__|$OUTPUT_PATH|" > $TEMP_SCRIPT

    sbatch $TEMP_SCRIPT
    sleep 1
done
