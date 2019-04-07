#!/usr/bin/python3

import sys

# function of reading input from reducer_1
def read_reducer_1_output(file):
    
    for line in file:
        yield line.strip().split("\t")

"""
Second Job - Mapper
Return category and num_countries
Input - key: category, value: number of countries for each video_id
Output - key: category, value: number of countries for each video_id, and count 1
"""

def mapper_2():

    data = read_reducer_1_output(sys.stdin)
    
    for category, num_countries in data:
        value = "{},1".format(num_countries)
        print("{}\t{}".format(category, value))

if __name__ == "__main__":
    mapper_2()
