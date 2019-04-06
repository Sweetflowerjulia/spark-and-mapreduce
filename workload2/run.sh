#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./run.sh [input_data_file] [output_location]"
    exit 1
fi

export PYSPARK_PYTHON=python3
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --num-executors 3 \
    --py-files functions.py Top10_result.py \
    --input $1 \
    --output $2
