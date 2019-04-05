#!/usr/bin/python3

import sys

# function of reading input from mapper
def read_map_2_output(file):

    for line in file:
        yield line.strip().split("\t")

"""
In the second reducer, count of video id by category - number of input of each category..
Input -  key: category, value: number of countries of each video id
Output - key: category, value: average number of countries of each video id
"""

def reducer_2():
    # initial values
    current_category = ""
    count = 0
    sum_countries = 0
    
    data = read_map_2_output(sys.stdin)
    
    for category, num_countries in data:
        if current_category != category:
            
            if current_category != "":

                avg = sum_countries/count
                print("{}\t{}".format(category, avg))
        
            # move to next category
            current_category = category
            count = 0
            sum_countries = 0
        
        count += 1
        sum_countries += int(num_countries)

    # print last result out
    if current_category != "":
        avg = sum_countries/count
        print("{}\t{}".format(category, avg))

if __name__ == "__main__":
    reducer_2()
