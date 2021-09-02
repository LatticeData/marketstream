from stocksdata.util.ttlcache import daily_cache
from stocksdata.util.get import *

@daily_cache
def sma(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/sma",params).get("SMA")


@daily_cache
def smav(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/smav",params).get("SMAV")

@daily_cache
def so(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/so",params).get("SO")

@daily_cache
def wilder(ticker_symbol,period):
    params = {"ticker_symbol":ticker_symbol,"period":period}
    return get_json("/stock/indicator/wilder",params).get("Wilder")

@daily_cache
def adx(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/adx",params).get("ADX")

@daily_cache
def rsi(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/rsi",params).get("RSI")

@daily_cache
def bb(ticker_symbol,period):
    params = {"ticker_symbol":ticker_symbol,"period":period}
    return get_json("/stock/indicator/bb",params).get("BB")

@daily_cache
def roc(ticker_symbol,period):
    params = {"ticker_symbol":ticker_symbol,"period":period}
    return get_json("/stock/indicator/roc",params).get("ROC")

@daily_cache
def macd(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/macd",params).get("MACD")

@daily_cache
def atr(ticker_symbol,short_period,long_period):
    params = {"ticker_symbol":ticker_symbol,"short_period":short_period,"long_period":long_period}
    return get_json("/stock/indicator/atr",params).get("ATR")

