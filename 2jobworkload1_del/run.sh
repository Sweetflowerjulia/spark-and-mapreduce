#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./driver.sh [input_location] [output_location]"
    exit 1
fi

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \

-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='Category and Trending Correlation' \
-file mapper_1.py \
-mapper mapper_1.py \
-file reducer_1.py \
-reducer reducer_1.py \
-input $1 \
-output outputfolder


hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \

-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='Category and Trending Correlation' \
-file mapper_2.py \
-mapper mapper_2.py \
-file reducer_2.py \
-reducer reducer_2.py \
-input outputfolder \
-output $2
