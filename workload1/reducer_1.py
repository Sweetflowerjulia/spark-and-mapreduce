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
Output - key: video_id + category, value: number of countries
"""

def reducer_1():
    # initial values
    current_id = ""
    countries = {}
    
    data = read_map_1_output(sys.stdin)
    
    for video_id, category_country in data:
        category, country = category_country.strip().split(",")
        
        if current_id != video_id:
            
            # Print output - number of countries belong to each (video id + category)
            if current_id != "":
                for videoId_category, country_list in countries.items():
                    # count number of countries
                    num_countries = len(country_list)
                    # key: (video_id + category), value: number of countries for each video id
                    print("{}\t{}".format(videoId_category, num_countries))
        
            # move to next video_id
            current_id = video_id
            countries = {}
        
        # for each (video_id + category), add countries to the tuple (unique county list)
        videoId_category = "{},{}".format(video_id, category)
        
        if videoId_category not in countries.keys():
            countries[videoId_category] = (country,)
        if videoId_category in countries.keys():
            countries[videoId_category] += (country,)

    # print last result out
    if current_id != "":
        
        for videoId_category, country_list in countries.items():
            num_countries = len(country_list)
            print("{}\t{}".format(videoId_category, num_countries))

if __name__ == "__main__":
    reducer_1()
