#!/usr/bin/python3

import sys

# function of reading input from mapper_1
def read_map_1_output(file):

    for line in file:
        yield line.strip().split("\t")

"""
First Job - Reducer
First reducer counts number of countries by video_id.
Input -  key: video_id, value: category + country
Output - key: category, value: number of countries for each video_id
"""

def reducer_1():
    # initial values
    current_id = ""
    countries = set()

    data = read_map_1_output(sys.stdin)
    
    for video_id, category_country in data:
        category, country = category_country.strip().split(",")
        
        if current_id != video_id:
            
            # Print output - number of countries belong to each (video id + category)
            if current_id != "":
                num_countries = len(countries)
                print("{}\t{}".format(current_category, num_countries))

            # move to next video_id
            current_id = video_id
            current_category = category
            countries = set()
        # Add country to the set, save unique country for each video id.
        countries.add(country)

    # print last result out
    if current_id != "":
        num_countries = len(countries)
        print("{}\t{}".format(current_category, num_countries))

if __name__ == "__main__":
    reducer_1()
