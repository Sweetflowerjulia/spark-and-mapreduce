#!/usr/bin/python3

import sys

def mapper():
    """ This mapper select category and return key:category; value: video_id + country.
    """
    for line in sys.stdin:
        # Clean and split input
        line = line.strip().split(",")

        # Check the format of the columns
        if len(line) != 12:
          continue

        video_id = line[0].strip()
        category = line[3].strip()
        country = line[-1].strip()
        
        value = video_id + "\t" + country
        
        print("{}\t{}".format(category, value))

if __name__ == "__main__":
    mapper()
