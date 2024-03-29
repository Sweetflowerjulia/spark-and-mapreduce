#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./run.sh [input_data_file] [output_location]"
    exit 1
fi

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='Category and Trending Correlation_JOB1' \
-file mapper_1.py \
-mapper mapper_1.py \
-file reducer_1.py \
-reducer reducer_1.py \
-input $1 \
-output FirstJobOutput


hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.reduces=1 \
-D mapreduce.job.name='Category and Trending Correlation_JOB2' \
-file mapper_2.py \
-mapper mapper_2.py \
-file reducer_2.py \
-reducer reducer_2.py \
-input FirstJobOutput \
-output $2
