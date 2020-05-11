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

    if(os.path.isfile('data.json')):
        with open('data.json', 'r') as rj:
            rj_file = rj.read()
        oldData = json.loads(rj_file)
        diff_confirmed = confirmed - oldData['confirmed']['value']
        diff_deaths = deaths - oldData['deaths']['value']
        diff_recoverd = recovered - oldData['recovered']['value']


    

    if(confirmed > 0 and deaths > 0 and recovered > 0):
        tweet = "CORONA VIRUS NO BRASIL: \n"
        tweet += f"Infectados: {confirmed:,} \nMortos: {deaths:,} \nRecuperados: {recovered:,} \n"
        if(diff_confirmed > 0 and len(tweet) < 280):
            tweet += f"\n{diff_confirmed:,} novos infectados"
        if(diff_deaths > 0 and len(tweet) < 280):
            tweet += f"\n{diff_deaths:,} novas mortes"
        if(diff_recoverd > 0 and len(tweet) < 280):
           tweet += f"\n{diff_recoverd:,} novos recuperados"

    if((tweet != "") and (len(tweet) <= 280)):
        print(tweet + "\ntamanho:" + str(len(tweet)))
        bot.update_status(tweet)



def startup():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    return api