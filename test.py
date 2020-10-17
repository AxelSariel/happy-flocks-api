import sentiment
import json

tweets = sentiment.get_happy_tweets()

print(json.dumps(tweets, indent = 4))