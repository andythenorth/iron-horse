#!/bin/bash

MODIFIED_DIR="./tmp/modified_consist_classes"
ORIGINAL_DIR="./tmp/consist_classes"
QUEUE_DIR="./tmp/insertion_queue"

mkdir -p "$QUEUE_DIR"

for modified_file in "$MODIFIED_DIR"/*.py; do
    base_name=$(basename "$modified_file")
    original_file="$ORIGINAL_DIR/$base_name"

    if [[ -f "$original_file" ]]; then
        # Normalize files before comparison
        diff -wB "$original_file" "$modified_file" > /dev/null
        if [[ $? -ne 0 ]]; then
            echo "🔄 Difference detected in $base_name, adding to queue."
            cp "$modified_file" "$QUEUE_DIR/"
        fi
    else
        echo "⚠️ No original version found for $base_name, adding to queue."
        cp "$modified_file" "$QUEUE_DIR/"
    fi
done

echo "✅ Queue updated with modified files."
