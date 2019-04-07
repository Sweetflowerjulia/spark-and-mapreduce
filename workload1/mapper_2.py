#!/usr/bin/python3

import sys

# function of reading input from reducer_1
def read_reducer_1_output(file):
    
    for line in file:
        yield line.strip().split("\t")

"""
Second Job - Mapper
Return category and num_countries pairs by category
Input - key: category, value: number of countries for each video_id
Output - key: category, value: number of countries for each video_id
"""

def mapper_2():

    data = read_reducer_1_output(sys.stdin)
    
    for category, num_countries in data:
        print("{}\t{}=1".format(category, num_countries))

if __name__ == "__main__":
    mapper_2()
