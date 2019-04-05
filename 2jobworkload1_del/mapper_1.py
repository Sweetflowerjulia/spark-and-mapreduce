#!/usr/bin/python3

import sys

def mapper_1():
    """ This mapper select three columns from the input line and return key:video_id; value: category + country.
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
        
        value = category + "\t" + country
        
        print("{}\t{}".format(video_id, value))

if __name__ == "__main__":
    mapper_1()
