#!/bin/bash

INPUT_FILE="/global/cfs/cdirs/m4293/visulaization_paper/small_scale/shuttle/shuttle_data.txt"
LABEL_FILE="/global/cfs/cdirs/m4293/visulaization_paper/small_scale/shuttle/shuttle_labels.txt"
OUTPUT_DIR="~/repos/graph-visualization/tsne/output/scikit-learn"
MAX_ITER=1000
INPUT_TYPE=2

for i in 10 20 30 50 100; do
    PERPLEXITY=$i

    OUTPUT_FILE="$OUTPUT_DIR/shuttle_p_${PERPLEXITY}.png"
    TEMP_SCRIPT="temp_scikit-learn_tsne_viz_shuttle_p_${PERPLEXITY}.sh"

    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" ~/repos/graph-visualization/tsne/scripts/scikit-learn_tsne_viz_template.sh | \
    sed "s|__DATASET__|shuttle|" | \
    sed "s|__PERPLEXITY__|$PERPLEXITY|" | \
    sed "s|__MAX_ITER__|$MAX_ITER|" | \
    sed "s|__INPUT_FILE__|$INPUT_FILE|" | \
    sed "s|__LABEL_FILE__|$LABEL_FILE|" | \
    sed "s|__INPUT_TYPE__|$INPUT_TYPE|" | \
    sed "s|__OUTPUT_FILE__|$OUTPUT_FILE|" > $TEMP_SCRIPT

    sbatch $TEMP_SCRIPT
    sleep 1
done
