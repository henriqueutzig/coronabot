import os
import tweepy
import time
import datetime
from coronaTrackerAPI import getLatestData
from twitterBot import postTweet, startup
from database import compareData, storeData


def main():
    bot_api = startup()
    while True:
        # Get current data 
        currentData = getLatestData()
        
        # Compare new data with older data 
        isDifferent = compareData(currentData)
        
        # Post current data on Twitter
        if (isDifferent == True):
            postTweet(bot_api, currentData)
            storeData(currentData)

        
        time.sleep(600) #s
        


if __name__== '__main__':
    main()
