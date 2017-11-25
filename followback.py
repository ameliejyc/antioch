#!/usr/bin/env python
import tweepy
from .twbot import api



for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print(follower.screen_name)
