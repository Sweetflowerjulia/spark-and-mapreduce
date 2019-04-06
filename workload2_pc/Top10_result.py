# Workload2 - Top10_result

from pyspark import SparkContext
from functions import *
import argparse

'''
This is the main code file of workload2.
Workload2 have two code files: 1. Top10_result.py  2. functions.py
Please make sure the 'functions.py' file is in the same directory with this file before run the code. 
'''

if __name__ == "__main__":
    
    sc = SparkContext(appName="Top10_result")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path", default="AllVideos_short.csv")
    parser.add_argument("--output", help="the output path", default="juli7727_Top10_result")
    args = parser.parse_args()
    
    input_path = args.input
    output_path = args.output
    
    data = sc.textFile(input_path)
    # identify and remove the header
    header = data.first()
    allVideos = data.filter(lambda line:line!=header)
    
    # Extract related columns and group by (video_id, country)
    GroupBy_VideoId_Country = allVideos.map(extractColumns).groupByKey(1)
    
    # For each (video_id, country), select first and second trending appearances and remove the records which contain less than 2 records.
    First_Second_Trending = GroupBy_VideoId_Country.map(sortByDate).filter(lambda line:line!=None)
    
    # Calculate the growth of dislikes for each (video_id, country), and sort by caculated results in descending order
    SortedResult = First_Second_Trending.map(CalculateIncrease).sortBy(lambda x:x[1], ascending=False)
    
    # Only select top10 values
    TopTen = SortedResult.zipWithIndex().filter(lambda index:index[1]<10).keys()
    
    TopTen.saveAsTextFile(output_path)
    