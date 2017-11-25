#!/usr/bin/env python
from twbot import api
import tweepy
import time

def reply():
    '''Reply feature that tweets a custom message to every person that mentions the bot.
    It checks every 60 seconds for mentions  or 300s if the server gets overwhelmed'''
    for tweet in tweepy.Cursor(api.mentions_timeline).items():
        try:
            #print('tweet from @' + tweet.user.screen_name + ':' + tweet.text)
            api.update_status('@' + tweet.user.screen_name + ' cheers, love!', in_reply_to_status_id = tweet.id)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break


while True:
    try:

        reply()
        time.sleep(60)

    except KeyboardInterrupt as e:
        break
    #rate limiting exception, we back off
    except tweepy.TweepError as e:
        if e.api_code == 429:
            time.sleep(300)
        else:
            raise
