import json
import tweepy
import config
import requests

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
api = tweepy.API(auth)

tweets = api.search(q = '#UltraHacks', count = 10)

tweetsJsonList = []
for tweet in tweets:
    tweetsJsonList.append(tweet._json)

response = requests.post('http://localhost:5000/api/v1/tweets/filterhappy', json=tweetsJsonList)

print(json.dumps(response.json(), indent=4))