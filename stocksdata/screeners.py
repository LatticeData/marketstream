from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *

## screeners ###################################################################################################################################

@daily_cache
def conservative_foreign_funds():
    return get_json("/market/screener/conservative-foreign-funds").get("funds")

@daily_cache
def most_actives():
    return get_json("/market/screener/most-actives").get("stocks")

@daily_cache
def most_shorted_stocks():
    return get_json("/market/screener/most-shorted-stocks").get("stocks")

@daily_cache
def undervalued_growth_stocks():
    return get_json("/market/screener/undervalued-growth-stocks").get("stocks")

@daily_cache
def growth_technology_stocks():
    return get_json("/market/screener/growth-technology-stocks").get("stocks")

@daily_cache
def day_gainers():
    return get_json("/market/screener/day-gainers").get("stocks")

@daily_cache
def day_losers():
    return get_json("/market/screener/day-losers").get("stocks")

@daily_cache
def undervalued_large_caps():
    return get_json("/market/screener/undervalued-large-caps").get("stocks")

@daily_cache
def aggresive_small_caps():
    return get_json("/market/screener/aggressive-small-caps").get("stocks")

@daily_cache
def small_cap_gainers():
    return get_json("/market/screener/small-cap-gainers").get("stocks")

@daily_cache
def top_mutual_funds():
    return get_json("/market/screener/top-mutual-funds").get("mutual_funds")

@daily_cache
def portfolio_anchors():
    return get_json("/market/screener/portfolio-anchors").get("stocks")

@daily_cache
def solid_large_growth_funds():
    return get_json("/market/screener/solid-large-growth-funds").get("funds")

@daily_cache
def solid_midcap_growth_funds():
    return get_json("/market/screener/solid-midcap-growth-funds").get("funds")

@daily_cache
def high_yield_bonds():
    return get_json("/market/screener/high-yield-bonds").get("bonds")