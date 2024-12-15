#!/bin/bash

# Configuration file and base command
CONFIG_FILE="config_file_1.nn"
BASE_COMMAND="./my_torch_analyzer --train $CONFIG_FILE"

# List of test dataset files
DATASETS=(
    "tests/datasets/check/10_pieces.txt"
    "tests/datasets/check/20_pieces.txt"
    "tests/datasets/check/many_pieces.txt"

    "tests/datasets/checkmate/10_pieces.txt"
    "tests/datasets/checkmate/20_pieces.txt"
    "tests/datasets/checkmate/many_pieces.txt"

    "tests/datasets/nothing/10_pieces.txt"
    "tests/datasets/nothing/20_pieces.txt"
    "tests/datasets/nothing/many_pieces.txt"

    "tests/datasets/stalemate/10_pieces.txt"
    "tests/datasets/stalemate/20_pieces.txt"
    "tests/datasets/stalemate/many_pieces.txt"
)

# Loop through each dataset and execute the command
for DATASET in "${DATASETS[@]}"
do
    echo "Running prediction for dataset: $DATASET"
    $BASE_COMMAND "$DATASET"
    if [ $? -ne 0 ]; then
        echo "Error: Command failed for dataset $DATASET"
        exit 1
    fi
    echo "Completed prediction for dataset: $DATASET"
done

echo "All predictions completed successfully."
