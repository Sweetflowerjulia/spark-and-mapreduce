#!/usr/bin/python3

import sys

# function of reading input from reducer_1
def read_reducer_1_output(file):
    
    for line in file:
        yield line.strip().split("\t")

def mapper_2():
    """ This is the second mapper.
        Input - key: video_id + category, value: num_countries
        Output - key: category, value: num_countries
    """
    data = read_reducer_1_output(sys.stdin)
    
    for video_id, category, num_countries in data:
        
        print("{}\t{}".format(category, num_countries))

if __name__ == "__main__":
    mapper_2()
