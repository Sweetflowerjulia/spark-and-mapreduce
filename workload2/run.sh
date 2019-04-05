#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./driver.sh [input_location] [output_location]"
    exit 1
fi

spark-submit \
    --master local[4] \
    Top10_result.py \
    --input $1  \
    --output $2
