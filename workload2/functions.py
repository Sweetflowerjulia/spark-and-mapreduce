# Workload2 - functions
import csv
from datetime import datetime

'''
This is the second code file of workload2, only functions inclued.
Workload2 have two code files: 1. Top10_result.py  2. functions.py
Please run the 'Top10_result.py' code file. 
'''

def extractColumns(data):
    """ This function converts entries of AllVideos_short.csv into key,value pair:
    key: (video_id, country)
    value: (trending_date,category, likes, dislikes)
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
    """
    For each (video_id, country), sort the values by trending date.
    Input is VideoId_Country and TrendingList(trending date, category, likes, dislikes)
    Return (video_id, country) and sorted values of the first two trending dates. 
    Only return results while the key-(video_id, country) contains at least two values.
    """
    VideoId_Country, TrendingList = video_list
    
    # Sort by trending date
    sortedByDate = sorted(TrendingList, key=lambda x:x[0], reverse=False)
    # Check trending dates have two records at leat
    if len(sortedByDate) >= 2 :
        # Drop trending date, only return category, likes, dislikes
        Category_likes_dislikes_List = [i[1:] for i in sortedByDate]
        return VideoId_Country, Category_likes_dislikes_List[:2]
    
        
def CalculateIncrease(trendings):
    """
    For each (VideoId, Country), calculate dislike growth value.
    Input is VideoId, Country and two trending records with category, likes and dislikes
    Return video_id, dislike growth value, category, country
    """
    (VideoId, Country), Two_TrendingList = trendings
    first_trending, second_trending = Two_TrendingList
    category_1, first_likes, first_dislikes = first_trending
    category_2, second_likes, second_dislikes = second_trending
    
    result = (second_dislikes-first_dislikes)-(second_likes-first_likes)
    result = round(result,2)
    
    return VideoId, result, category_1, Country

