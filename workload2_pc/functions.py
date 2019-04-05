import csv
from datetime import datetime

"""
This module includes a few functions used in computing average rating per genre
"""

def extractColumns(data):
    """ This function converts entries of ratings.csv into key,value pair of the following format
    (movieID, rating)
    Args:
        record (str): A row of CSV file, with four columns separated by comma
    Returns:
        The return value is a tuple (movieID, genre)
    """
    try:
        line = data.strip().split(",")
        video_id = line[0]
        trending_date = datetime.strptime(line[1], '%y.%d.%m')
        category = line[3]
        likes = int(line[6])
        dislikes = int(line[7])
        country = line[-1]
        VideoId_Country = (video_id, country)
        Values = (trending_date,category, likes, dislikes)
        return (VideoId_Country, Values)

    except:
        return ()

    
def sortByDate(video_list):

    VideoId_Country, TrendingList = video_list

    sortedByDate = sorted(TrendingList, key=lambda date:date[0], reverse=True)
    if len(sortedByDate) >= 2 and :    
        return VideoId_Country, sortedByDate[:2]
    

    
    
    
def Function(a):
    (VideoId, Country), value = a
    first, second = value
    result = (second[2] - first[2])-(second[1] - first[1])
    return 





def mapToPair(line):
    """ This function converts tuples of (genre, rating) into key,value pair of the following format
    (genre,rating)
    
    Args:
        line (str): A touple of  (genre, rating) 
    Returns:
        The return value is a tuple  (genre, rating) 
    """
    genre, rating = line
    return (genre, rating)


def mergeRating(accumulatedPair, currentRating):
    """This funtion update a current  summary (ratingTotal, ratingCount) with a new rating value.
    
    Args:
        accumulatedPair (tuple): a tuple of (ratingTotal, ratingCount)
        currentRating (float):a new rating value, 
    Returns:
        The return value is an updated tuple of (ratingTotal, ratingCount)
    
    """
    ratingTotal, ratingCount = accumulatedPair
    ratingTotal += currentRating
    ratingCount += 1
    return (ratingTotal, ratingCount)


def mergeCombiners(accumulatedPair1, accumulatedPair2):
    """This function merges two intermedate summaries of the format (ratingTotal, ratingCount)
  
    Args:
        accumulatedPair1 (tuple): a tuple of (ratingTotal, ratingCount)
        accumulatedPair2 (fuple): a tuple of (ratingTotal, ratingCount) 
    Returns:
        The return value is an updated tuple of (ratingTotal, ratingCount)
    """
    ratingTotal1, ratingCount1 = accumulatedPair1
    ratingTotal2, ratingCount2 = accumulatedPair2
    return (ratingTotal1+ratingTotal2, ratingCount1+ratingCount2)


def mapAverageRating(line):
    """This function compute the average with a given sum and count for a genre
    Args:
        line (tuple): a tuple of (genre, (ratingTotal,ratingCount))
    Returns:
        The return value is a tuple of (genre, average_rating)
    """

    genre, ratingTotalCount = line
    ratingAverage = ratingTotalCount[0]/ratingTotalCount[1]
    return (genre, ratingAverage)