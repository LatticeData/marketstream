from stocksdata.util.ttlcache import daily_cache
from stocksdata.util.get import *

def wikipedia_url_to_ticker_symbol(wikipedia_url):
    params = {"wikipedia_url": wikipedia_url}
    return get_json("/search/wikpedia-url-to-ticker-symbol", params).get("ticker_symbol")

def stock_screener(param):
    params = param
    return get_json("/screener", params).get("stocks")

def isin_to_ticker_symbol(isin):
    params = {"isin": isin}
    return get_json("/search/isin-to-ticker-symbol", params).get("ticker_symbol")

def company_name_to_ticker_symbol(company_name):
    params = {"company_name": company_name}
    return get_json("/search/company-name-to-ticker-symbol", params).get("ticker_symbol")
