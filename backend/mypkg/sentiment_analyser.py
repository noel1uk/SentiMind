from .tweet_parser import TweetParser
from .twitter_req import *
from .polarity import *
import json

class SentimentAnalyser:
    'Requests tweets, cleans them, assigns sentiment and averages them'

    def populate(self):
      cleaned_tweets = []
      tweet_parser = TweetParser()
      tweets = get_tweets()
      for tweet in tweets:
          cleaned_tweets.append(tweet_parser.parse_tweet(tweet))
      return cleaned_tweets

    def average_sentiment(self):
      avg_sentiment = 0
      tweets = self.populate()
      for tweet in tweets:
          avg_sentiment += round(tweet.sentiment, 2)
      return round(avg_sentiment/len(tweets), 2)

    def general_polarity_result(self):
        result = polarity_result(self.average_sentiment())
        string = '{sentiment: %s}' % result
        return json.load(string)