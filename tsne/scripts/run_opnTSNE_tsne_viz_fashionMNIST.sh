#!/bin/bash

INPUT_FILE="~/repos/graph-visualization/tsne/data/fashionMNIST/train-images-idx3-ubyte.gz"
LABEL_FILE="~/repos/graph-visualization/tsne/data/fashionMNIST/train-labels-idx1-ubyte.gz"
OUTPUT_DIR="~/repos/graph-visualization/tsne/output/openTSNE"

for i in 10 20 30 50 100; do
    PERPLEXITY=$i

    for j in 10 20 50 100; do
        N_NEIGHBORS=$j

        OUTPUT_FILE="$OUTPUT_DIR/fashionMNIST_p_${PERPLEXITY}_n_${N_NEIGHBORS}_mi_${MAX_ITER}.png"
        TEMP_SCRIPT="temp_openTSNE_tsne_viz_fashionMNIST_p_${PERPLEXITY}_n_${N_NEIGHBORS}_mi_${MAX_ITER}.sh"

        sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/openTSNE_tsne_viz_template.sh | \
        sed "s|__PERPLEXITY__|$PERPLEXITY|" | \
        sed "s|__N_NEIGHBORS__|$N_NEIGHBORS|" | \
        sed "s|__INPUT_FILE__|$INPUT_FILE|" | \
        sed "s|__LABEL_FILE__|$LABEL_FILE|" | \
        sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" > $TEMP_SCRIPT

        sbatch $TEMP_SCRIPT
        sleep 1
    done
done
