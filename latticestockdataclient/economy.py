from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *

@daily_cache
def risk_free_rate():
    return get_json("/economy/risk-free-rate").get("risk_free_rate")

@daily_cache
def last_year_market_return():
    return get_json("/economy/last-year-market-return").get("last_year_market_return")
