#!/usr/bin/python3

import sys

# function of reading input from mapper
def read_map_output(file):

    for line in file:
        yield line.strip().split("\t")


def reducer():
    # initial values
    current_category = ""
    id_country = {}
    
    data = read_map_output(sys.stdin)
    
    for category, video_id, country in data:
        if current_category != category:
            
            if current_category != "":
                num_countries = 0
                
                for id, country_list in id_country.items():
                    # sum number of countries of each video id
                    num_countries += len(country_list)
                # calculate average
                output = num_countries/len(id_country.keys())
                print("{}\t{}".format(current_category, output))
        
            # move to next category
            current_category = category
            id_country = {}
        
        # for each category, make a dictionary for {video_id:countries}
        if video_id not in id_country.keys():
            id_country[video_id] = (country,)
        if video_id in id_country.keys():
            id_country[video_id] += (country,)

    # print last result out
    if current_category != "":
        num_countries = 0
        
        for id, country_list in id_country.items():
            num_countries += len(country_list)
            output = num_countries/len(id_country.keys())
            print("{}\t{}".format(current_category, output))

if __name__ == "__main__":
    reducer()
