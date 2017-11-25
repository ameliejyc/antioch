import tweepy
import configparser

#We are going to access the secret.ini file
config = configparser.ConfigParser()
config.read('secret.ini')

consumer_key = config['DEFAULT']['consumer_key']
consumer_secret = config['DEFAULT']['consumer_secret']
access_token = config['DEFAULT']['access_token']
access_secret = config['DEFAULT']['access_secret']

#Creation of an OAuthHandler instance into which we’ll pass our consumer token and secret.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
