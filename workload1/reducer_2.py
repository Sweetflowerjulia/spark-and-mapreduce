#!/usr/bin/python3

import sys

# function of reading input from mapper_2
def read_map_2_output(file):

    for line in file:
        yield line.strip().split("\t")

"""
Second Job - Reducer
The second reducer counts video_id by category (counts input by category),and sum up number of countries by category. Lastly, calculates average number of countries for each category.
Input -  key: category, value: number of countries of each video id
Output - key: category, value: average number of countries of each video id
"""

def reducer_2():
    # initial values
    current_category = ""
    
    data = read_map_2_output(sys.stdin)
    
    for category, num_countries in data:
        if current_category != category:
            
            # print output
            if current_category != "":
                # average number of countries
                avg = sum_countries/count
                print("{}\t{}".format(current_category, avg))
        
            # move to next category
            current_category = category
            count = 0
            sum_countries = 0
        # count the input - number of video id
        count += 1
        # sum number of countries for each category
        sum_countries += int(num_countries)

    # print last result out
    if current_category != "":
        avg = sum_countries/count
        print("{}\t{}".format(current_category, avg))

if __name__ == "__main__":
    reducer_2()
