# 'https://realpython.com/twitter-bot-python-tweepy/'
import tweepy
import json
import os
from coronaTrackerAPI import getTotalDeaths, getTotalInfected


#getting twitter keys
from os import environ

class Bot: 

    def __init__(self, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET
        self.ACCESS_TOKEN = ACCESS_TOKEN
        self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
        self.api = self.startup()

    def startup(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)

        # Create API object
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
        return api
        
    def postTweet(self, text):
        if(text.length <= 280 and text != ""):
            print(text + "\ntamanho:" + str(len(text)))
            self.api.update_status()

    def getOldTweets(self):
        return self.api.user_timeline(tweet_mode='extended')
        




def isDuplicated(tweet, api):
    isDup = True
    tweet = tweet[:tweet.find("Fonte")]
    # gets old tweets
    oldTweets = api.user_timeline(tweet_mode='extended')
    tweetList = []
    # creating an array with all the contents 
    for t in oldTweets:
        text = t.full_text[:t.full_text.find("Fonte")]
        tweetList.append(text)
    # compare old tweets with new and set isDup to True or False
    if (tweet not in tweetList):
        isDup = False
    print("isDuplicated: " + str(isDup)) # print for debugging
    return isDup

# function that gets the difference between the current Data and
# the data stored in 'data.json' and return a stg to be added on the tweet
''' 
TODO:
    implement thread that tweets only the diference of values every 24h 
'''
def dataDiff(currentData):
    diffTxt = ""
    confirmed = currentData['confirmed']['value']
    deaths = currentData['deaths']['value']
    recovered = currentData['recovered']['value']
    
    if(os.path.isfile('data.json')):
        with open('data.json', 'r') as rj:
            rj_file = rj.read()
        oldData = json.loads(rj_file)
        diff_confirmed = confirmed - oldData['confirmed']['value']
        diff_deaths = deaths - oldData['deaths']['value']
        diff_recoverd = recovered - oldData['recovered']['value']
    if ((diff_confirmed != confirmed) and (diff_deaths != deaths) and (diff_recoverd != recovered)): 
        if(diff_confirmed > 0 and len(diffTxt) < 280):
            diffTxt += f"{diff_confirmed:,} novos infectados"
        if(diff_deaths > 0 and len(diffTxt) < 280):
            diffTxt += f"\n{diff_deaths:,} novas mortes"
        if(diff_recoverd > 0 and len(diffTxt) < 280):
           diffTxt += f"\n{diff_recoverd:,} novos recuperados\n\n"
    
    return diffTxt
