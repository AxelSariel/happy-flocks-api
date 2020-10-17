import flask
from flask import request, jsonify
from helpers import error, warning, success
import sentiment

app = flask.Flask(__name__)
app.config["DEBUG"] = False

tweets = [
    {
        'id' : 1,
        'text' : 'Hacking at Twitter! #Hack',
        'user' : 'axelsariel',
        'polarity' : 'positive'
    },
    {
        'id' : 2,
        'text' : 'Ultrahacks!',
        'user' : 'twitter',
        'polarity' : 'positive'
    },
    {
        'id' : 3,
        'text' : '#Eat. #Hack. #Repeat.',
        'user' : 'axelsariel',
        'polarity' : 'neutral'
    },
    {
        'id' : 3,
        'text' : 'I don\'t like hacking #Hack',
        'user' : 'someUser',
        'polarity' : 'negative'
    }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello world!</h1>"

@app.route('/api/v1/tweets/all', methods=['GET'])
def api_all():
    return jsonify(tweets)

@app.route('/api/v1/tweets', methods=['GET'])
def get_tweet():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for tweet in tweets:
        if id == tweet['id']:
            results.append(tweet)

    return jsonify(results)

# /api/v1/tweets/search?q=medicine&polarity=positive
@app.route('/api/v1/tweets/search', methods=['GET'])
def search_tweet():
    if 'q' in request.args:
        q = request.args['q']
    else:
        return "Error: No query field provided. Please specify a query."

    if 'polarity' in request.args:
        polarity = request.args['polarity']
    else:
        return "No polarity option given!"

    results = []

    for tweet in tweets:
        if q.lower() in tweet['text'].lower() and polarity == tweet['polarity']:
            results.append(tweet)

    return jsonify(results)

@app.route('/api/v1/tweets/gethappy', methods=['POST'])
def get_happy():
    tweets = request.get_json()
    happyTweets = []
    for tweet in tweets:
        if tweet['polarity'] == 'positive':
            happyTweets.append(tweet)

    return jsonify(happyTweets)

@app.route('/api/v1/echo', methods=['POST'])
def echo():
    content = request.get_json()
    print(content)
    return jsonify(content)

@app.route('/api/v1/tweets/happytest', methods=['GET'])
def get_happy_tweets_test():
    if 'q' in request.args:
        query = request.args['q']
    else:
        query = '#UltraHacks'
    tweets = sentiment.get_happy_tweets(query)
    return jsonify(tweets)

app.run(host='0.0.0.0', port=5000)
