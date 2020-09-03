import time
from os import environ
from src.bot import Bot
from src.tweet import Tweet
from src.tracker import Tracker

def main():
    TIME =  60 * 60 # 60 min * 60s --> s
    # getting twitter keys 
    CONSUMER_KEY = environ['CONSUMER_KEY']
    CONSUMER_SECRET = environ['CONSUMER_SECRET']
    ACCESS_TOKEN = environ['ACCESS_KEY']
    ACCESS_TOKEN_SECRET = environ['ACCESS_SECRET']

    # init bot
    bot = Bot(CONSUMER_KEY=CONSUMER_KEY, CONSUMER_SECRET=CONSUMER_SECRET,
              ACCESS_TOKEN=ACCESS_TOKEN, ACCESS_TOKEN_SECRET=ACCESS_TOKEN_SECRET)
    # init tracker (database api call)
    tracker = Tracker()
    # tweet init 
    tweet = Tweet(totalDeaths=(tracker.getTotalDeaths()),
                  totalInfected=(tracker.getTotalInfected()))

    while True:
        # Get latest data from Tracker
        tracker.update()
        # Generate tweet with latest data
        tweet.update(totalDeaths=(tracker.totalDeaths),
                     totalInfected=(tracker.totalInfected))
        
        # Get old tweets
        oldTweets = bot.getOldTweets()
        # Check if tweet is not duplicated
        if (tweet.isDuplicated(oldTweets=oldTweets) == False):
            bot.postTweet(text=(tweet.text))

        time.sleep(TIME) #s 



if __name__== '__main__':
    main()
