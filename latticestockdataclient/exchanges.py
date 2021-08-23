from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *

## exchanges #####################################################################################################################################

@daily_cache
def all_public_companies():
    return get_json("/market/all-public-companies").get("stocks")

@daily_cache
def nasdaq_exchange_composition():
    return get_json("/market/exchange/nasdaq").get("stocks")

@daily_cache
def nyse_composition():
    return get_json("/market/exchange/nyse").get("stocks")

@daily_cache
def shanghai_exchange_composition():
    return get_json("/market/exchange/shanghai-stock-exchange").get("stocks")

@daily_cache
def hong_kong_exchange_composition():
    return get_json("/market/exchange/hong-kong-stock-exchange").get("stocks")

@daily_cache
def london_exchange_composition():
    return get_json("/market/exchange/london-stock-exchange").get("stocks")