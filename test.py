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

#url = 'http://localhost:5000/api/v1/tweets/filterhappy'
# url = 'http://35.192.117.152:5000/api/v1/tweets/filterhappy'
url = 'http://localhost:5000/api/v1/tweets/happytest'
# response = requests.post(url, json=tweetsJsonList)
response = requests.get(url)

print(response.json())

# print(json.dumps(response.json(), indent=4))