#!/bin/bash

INPUT_FILE="/global/cfs/cdirs/m4293/visulaization_paper/small_scale/pendigits/pendigits.txt"
LABEL_FILE="/global/cfs/cdirs/m4293/visulaization_paper/small_scale/pendigits/digit_labels.txt"
OUTPUT_DIR="~/repos/graph-visualization/tsne/output/openTSNE"
INPUT_TYPE=2

for i in 10 20 30 50 100; do
    PERPLEXITY=$i

    OUTPUT_FILE="$OUTPUT_DIR/pendigits_p_${PERPLEXITY}.png"
    TEMP_SCRIPT="temp_openTSNE_tsne_viz_pendigits_p_${PERPLEXITY}.sh"

    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/openTSNE_tsne_viz_template.sh | \
    sed "s|__DATASET__|pendigits|" | \
    sed "s|__PERPLEXITY__|$PERPLEXITY|" | \
    sed "s|__INPUT_FILE__|$INPUT_FILE|" | \
    sed "s|__LABEL_FILE__|$LABEL_FILE|" | \
    sed "s|__INPUT_TYPE__|$INPUT_TYPE|" | \
    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" > $TEMP_SCRIPT

    sbatch $TEMP_SCRIPT
    sleep 1
done
