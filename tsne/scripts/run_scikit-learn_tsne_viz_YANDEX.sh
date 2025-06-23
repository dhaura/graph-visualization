#!/bin/bash

INPUT_FILE_PREFIX="/pscratch/sd/d/dhaura/datasets/graph-viz/YANDEX/YANDEX_subset"
MAX_ITER=1000

for i in 20000; do
    INPUT_FILE="${INPUT_FILE_PREFIX}_${i}.txt"

    TEMP_SCRIPT="temp_scikit-learn_tsne_viz_YANDEX_p_30_size_${i}.sh"

    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/scikit-learn_tsne_viz_large_scale_template.sh | \
    sed "s|__DATASET__|YANDEX|" | \
    sed "s|__MAX_ITER__|$MAX_ITER|" | \
    sed "s|__SIZE__|${i}|" | \
    sed "s|__INPUT_FILE__|$INPUT_FILE|" > $TEMP_SCRIPT

    sbatch $TEMP_SCRIPT
    sleep 1
done
