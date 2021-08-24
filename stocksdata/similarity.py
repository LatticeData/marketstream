from stocksdata.util.ttlcache import daily_cache
from stocksdata.util.get import *

@daily_cache
def business_description_similarity(ticker_symbol1,ticker_symbol2):
    params = {"ticker_symbol1": ticker_symbol1, "ticker_symbol2": ticker_symbol2}
    return get_json("/stock-similarity/business-description-similarity", params).get("similarity")

@daily_cache
def industry_similarity(ticker_symbol1,ticker_symbol2):
    params = {"ticker_symbol1": ticker_symbol1, "ticker_symbol2": ticker_symbol2}
    return get_json("/stock-similarity/industry-similarity", params).get("similarity")

@daily_cache
def stock_price_correlation(ticker_symbol1,ticker_symbol2):
    params = {"ticker_symbol1": ticker_symbol1, "ticker_symbol2": ticker_symbol2}
    return get_json("/stock-similarity/stock-price-correlation", params).get("similarity")

