import datetime as dt
from stocksdata.util.ttlcache import daily_cache, hourly_cache
from stocksdata.util.get import *


@hourly_cache
def cost_of_equity(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/valuation/cost-of-equity", params).get("cost_of_equity")

@hourly_cache
def enterprise_value(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/valuation/enterprise-value", params).get("enterprise_value")

@hourly_cache
def historical_valuation_measures(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    result = get_json("/stock/valuation/historical-valuation-measures", params).get('historical valuation measures')
    for statement in result:
        statement['Date'] = dt.datetime.strptime(statement['Date'],'%Y-%m-%dT%H:%M:%S')
    return result

@hourly_cache
def valuation_measures(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/stock/valuation/valuation-measures", params).get("valuation_measures")

def forward_pe(ticker_symbol):
    return valuation_measures(ticker_symbol).get("Forward P/E")

def trailing_pe(ticker_symbol):
    return valuation_measures(ticker_symbol).get("Trailing P/E")

def market_cap(ticker_symbol):
    return valuation_measures(ticker_symbol).get("Market Cap (intraday)")

