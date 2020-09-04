# 'https://realpython.com/twitter-bot-python-tweepy/'
import tweepy

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
        if(len(text) <= 280 and text != ""):
            print(text + "\ntamanho:" + str(len(text)))
            self.api.update_status(text)

    def getOldTweets(self):
        return self.api.user_timeline(tweet_mode='extended')
        