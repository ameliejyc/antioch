#!/usr/bin/env python
from twbot import api
import tweepy

def retweet_hashtag(hashtag):
    retweet = tweepy.Cursor(api.search, q=hashtag).items()
    for tweet in retweet:
        print(tweet.text)

retweet_hashtag('#shecodeslondon')