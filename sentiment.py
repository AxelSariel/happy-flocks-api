
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import config
import json

# Adapted from https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
  
class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = config.consumer_key
        consumer_secret = config.consumer_secret
        access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
  
        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            #self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
  
    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive', analysis.sentiment.polarity
        elif analysis.sentiment.polarity == 0: 
            return 'neutral', analysis.sentiment.polarity
        else: 
            return 'negative', analysis.sentiment.polarity
  
    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 

            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                tweet = tweet
                
                # saving sentiment of tweet 
                #parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
                tweet.sentiment, tweet.polarity = self.get_tweet_sentiment(tweet.text)

                tweet._json['sentiment'] = tweet.sentiment
                tweet._json['polarity'] = tweet.polarity
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if tweet not in tweets: 
                        tweets.append(tweet) 
                else: 
                    tweets.append(tweet) 

            tweets = sorted(tweets, key = lambda i: i.polarity, reverse=True)

            # for tweet in tweets:
            #     print(json.dumps(tweet._json, indent=4))
  
            # return parsed tweets 
            for tweet in tweets:
                printTweet = {}
                printTweet['text'] = tweet.text
                printTweet['polarity'] = tweet.polarity
                printTweet['sentiment'] = tweet.sentiment
                #print(json.dumps(printTweet, indent=4))

            tweetsJsonList = []
            for tweet in tweets:
                tweetsJsonList.append(tweet._json)
            return tweetsJsonList
  
        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 



def get_happy_tweets(query = '#UltraHacks'):
    api = TwitterClient()
    tweets = api.get_tweets(query = query, count = 10)
    tweets = tweets[:3]
    return tweets

  
def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    userQuery = input('Enter your query: ')
    tweets = api.get_tweets(query = userQuery, count = 10)
    tweets = tweets[:3]

    print(json.dumps(tweets, indent=4))
    
    #tweets = api.user_timeline(screen_name = 'normantv_')
  
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
  
if __name__ == "__main__": 
    # calling main function 
    main() 