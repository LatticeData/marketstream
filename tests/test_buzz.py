import pytest

from stocksdata.buzz import (
    wallstreetbets_mentions,
    news_sentiment,
    news,
    twitter_sentiment,
    fear_and_greed_index
)

ticker_symbol = "GME"

#def test_wallstreetbets_mentions():
 #   data = wallstreetbets_mentions(ticker_symbol)
  #  assert (
   #     data is not None
    #    and "mention_count" in data
    #)

def test_news_sentiment():
    data = news_sentiment(ticker_symbol)
    assert (
        data is not None
        and "sentiment_score" in data
        and len(data['source_articles']) > 0
    )
    
def test_news():
    data = news(ticker_symbol)
    assert (
        data is not None
    )

def test_twitter_sentiment():
    data = twitter_sentiment(ticker_symbol)
    assert (
        data is not None
        and "sentiment_score" in data
        and isinstance(data["sentiment_score"], float)
    )

def test_fear_and_greed_index():
    data = fear_and_greed_index()
    assert (
        data is not None
        and "Now" in data
    )
