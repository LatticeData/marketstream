from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *

@daily_cache
def wallstreetbets_mentions(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/buzz/wall-street-bets-mentions", params).get("wsb_mentions")

@daily_cache    
def news_sentiment(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/buzz/news-sentiment", params).get("sentiment")

@daily_cache    
def news(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/buzz/news", params).get("news")

@daily_cache
def twitter_sentiment(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/buzz/twitter-sentiment", params).get("sentiment")

@daily_cache
def fear_and_greed_index():
    return get_json("/buzz/fear-and-greed-index").get("fear_and_greed_index")
