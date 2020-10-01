import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# liking tweets under certain parameters


search_string = "python"
numbers_of_tweets = 2

for tweet in limit_handler(tweepy.Cursor(api.search.search_string).items(numbers_of_tweets)):
    try:
        tweet.retweet()
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# following your followers who are never been followed back

# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     follower.follow()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)