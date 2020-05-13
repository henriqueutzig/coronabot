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
        tweet = "COVID-19 VIRUS NO BRASIL\n\n"
        tweet += f"Infectados: {confirmed:,}\nMortos: {deaths:,}\nRecuperados: {recovered:,}\n\n"
        tweet += "Fonte dos Dados: John Hopkins University CSSE\n"
    
    if((tweet != "") and (len(tweet) <= 280) and (isDuplicated == False)):
        print(tweet + "\ntamanho:" + str(len(tweet)))
        bot.update_status(tweet)


def isDuplicated(tweet):
    isDup = True
    #request old tweets

    #compare old tweets with new and set isDup to True or False

    return isDup

def startup():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    return api