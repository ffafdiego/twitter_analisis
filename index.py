import tweepy

consumer_key = 'ixH401t4EpIABVzFtqA164rby'
consumer_secret = '0W1H6Xz4EdsCzsULq55DxHeR8QkdGPlECKuBahgzNhbnkHfn6R'
access_token = '68491634-nQNHDqO6oYPDRFGfnQQqSfTDz3Z6kbVKZmsB7Wo7E'
access_token_secret = 'KhfJx21l4wEX3K2ijvpNg8kvD5LDEgEjKsKkXAyvPaYKA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text