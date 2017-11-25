from twbot import api
import tweepy
import click

@click.command()
@click.option('--hashtag', prompt='Hashtag to search (include #)', help='What hashtag do you want to find tweets for?')
def run_search(hashtag):
    """Simple program that returns any tweets with the specified hashtag."""
    retweet = tweepy.Cursor(api.search, q=hashtag).items()
    for tweet in retweet:
        click.echo(click.style(tweet.user.screen_name, fg='red') + ': ' + tweet.text)  

if __name__ == '__main__':
    run_search()