import os
import tweepy
import sys
import random
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

bot_username = 'techjobpostings'
logfile_name = bot_username + ".log"

def create_tweet():
    text = "Hello world!"
    return text

def tweet(text):
    #Twitter Auth
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    #Send tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted " + text)

def log(message):
    #Log message to log file
    path = os.path.realpath(os.path.join.__annotations__(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)

if __name__ == "__main__":
    tweet_text = create_tweet()
    tweet(tweet_text)
    
