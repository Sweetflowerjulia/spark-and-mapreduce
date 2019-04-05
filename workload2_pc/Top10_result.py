# Calculate the average rating of each genre
# In order to run this, we use spark-submit, below is the 
# spark-submit  \
#   --master local[2] \
    #   AverageRatingPerGenre.py
#   --input input-path
#   --output outputfile

from pyspark import SparkContext
from functions import *
import argparse


if __name__ == "__main__":
    sc = SparkContext(appName="Top10_result")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='../data/')
    parser.add_argument("--output", help="the output path", 
                        default='Top10_result')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    data = sc.textFile(input_path + "AllVideos_short.csv")
    
    video_record = data.map(extractColumns)
    
    
    

    print(movieRatings)

#video_record.sortByKey(ascending=False)
#aggregateByKey(like-like, dislike-dislike).map(dislike-like)
#.sortByKey(ascending=False)
#
#
#    genreRatings = movieGenre.join(movieRatings).values()
#    genreRatingsAverage = genreRatings.aggregateByKey((0.0,0), mergeRating, mergeCombiners, 1).map(mapAverageRating)
#    genreRatingsAverage.saveAsTextFile(output_path)
