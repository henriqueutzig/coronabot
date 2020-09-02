import time
from coronaTrackerAPI import getLatestData
from twitterBot import postTweet, startup
from database import compareData, storeData

TIME =  60 * 60 # 60 min * 60 --> s

def main():

    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_TOKEN = environ['ACCESS_KEY']
    ACCESS_TOKEN_SECRET = environ['ACCESS_SECRET']


    bot_api = startup()
    while True:
        # Get current data 
        currentData = getLatestData()
        
        # Compare new data with older data 
        isDifferent = compareData(currentData)
        
        # Post current data on Twitter
        if (isDifferent == True):
            postTweet(bot_api)
            storeData(currentData)

        time.sleep(TIME) #s 



if __name__== '__main__':
    main()
