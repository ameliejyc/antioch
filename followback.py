#!/usr/bin/env python
from twbot import api
import tweepy


for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print(follower.screen_name)
