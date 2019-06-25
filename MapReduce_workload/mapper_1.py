#!/usr/bin/python3

import sys

def mapper_1():
    """
    First Job - Mapper
    This mapper selects three columns from the input: video_id, category, country
    Return key: video_id
         value: category + country
    """
    header = True
    
    for line in sys.stdin:
        # Clean and split input
        line = line.strip().split(",")
        # Filter header
        if header:
            header = False
            continue
            
        # Check the format of the columns
        if len(line) != 12:
            continue
        # Extract three relevant columns
        video_id = line[0].strip()
        category = line[3].strip()
        country = line[-1].strip()
        
        # Check and filter header
        category_country = category + "," + country
        print("{}\t{}".format(video_id, category_country))

if __name__ == "__main__":
    mapper_1()
