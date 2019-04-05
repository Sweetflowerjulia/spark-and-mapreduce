#!/usr/bin/python3

import sys

# function of reading input from mapper
def read_map_1_output(file):

    for line in file:
        yield line.strip().split("\t")

"""
In the first reducer, count number of countries by video_id.
Input -  key: video_id, value: category + country
Output - key: video_id + category, value:num_countries
"""

def reducer_1():
    # initial values
    current_id = ""
    countries = {}
    
    data = read_map_1_output(sys.stdin)
    
    for video_id, category, country in data:
        if current_id != video_id:
            
            if current_id != "":

                for key, country_list in countries.items():
                    # sum number of countries by video id
                    num_countries = len(country_list)
                    # key: category, value: number of countries by video_id
                    print("{}\t{}".format(key, num_countries))
        
            # move to next video_id
            current_id = video_id
            countries = {}
        
        # for each (video_id + category), add countries to the tuple (unique county list)
        key = "{}\t{}".format(video_id, category)
        
        if key not in countries.keys():
            countries[key] = (country,)
        if key in countries.keys():
            countries[key] += (country,)

    # print last result out
    if current_id != "":
        
        for key, country_list in countries.items():
            num_countries = len(country_list)
            print("{}\t{}".format(key, num_countries))

if __name__ == "__main__":
    reducer_1()
