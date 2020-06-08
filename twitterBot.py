# 'https://realpython.com/twitter-bot-python-tweepy/'
import tweepy
import json
import os

#getting twitter keys
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_TOKEN = environ['ACCESS_KEY']
ACCESS_TOKEN_SECRET = environ['ACCESS_SECRET']


def postTweet(bot, data):   
    tweet = ""

    confirmed = data['confirmed']['value']
    deaths = data['deaths']['value']
    recovered = data['recovered']['value']

    if(confirmed > 0 and deaths > 0 and recovered > 0):
        tweet = "COVID-19 NO BRASIL\n\n"
        tweet += f"Infectados: {confirmed:,}\nMortos: {deaths:,}\nRecuperados: {recovered:,}\n\n"
        tweet += "Fonte dos Dados: John Hopkins University CSSE\n"
        tweet += "#FiqueEmCasa"
    if((tweet != "") and (len(tweet) <= 280) and (isDuplicated(tweet, bot) == False)):
        print(tweet + "\ntamanho:" + str(len(tweet)))
        bot.update_status(tweet)


def isDuplicated(tweet, api):
    isDup = True
    # gets old tweets
    oldTweets = api.user_timeline()
    tweetList = []
    # creating an array with all the contents 
    for t in oldTweets:            
        tweetList.append(str(t.text))
    # compare old tweets with new and set isDup to True or False
    if (tweet not in tweetList):
        isDup = False
    print("isDuplicated: " + str(isDup)) # print for debugging
    return isDup

# function that gets the difference between the current Data and
# the data stored in 'data.json' and return a stg to be added on the tweet
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

# startup twitters api calling 
def startup():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    return api