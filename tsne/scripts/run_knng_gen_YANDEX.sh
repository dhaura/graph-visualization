#!/bin/bash

INIT_DATASET_SIZE=20000

for i in {0..6}; do
    DATASET_SIZE=$((2**i * INIT_DATASET_SIZE))

    if [ $DATASET_SIZE -gt 1000000 ]; then
        DATASET_SIZE=1000000
    fi

    TEMP_SCRIPT="temp_knng_gen_YANDEX_size_${DATASET_SIZE}.sh"

    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/knng_construction_template.sh | \
    sed "s|__SIZE__|$DATASET_SIZE|" | \
    sed "s|__DATASET__|YANDEX|" | \
    sed "s|__DATASET__|YANDEX|" | \
    sed "s|__DATASET__|YANDEX|" > $TEMP_SCRIPT

    sbatch $TEMP_SCRIPT
    sleep 1
done
