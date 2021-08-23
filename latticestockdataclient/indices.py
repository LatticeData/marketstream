from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *

## indices ####################################################################################################################################

@daily_cache
def s_and_p_composition():
    return get_json("/market/index/s-and-p-five-hundred").get("stocks")

@daily_cache
def nasdaq_composition():
    return get_json("/market/index/nasdaq-composite").get("stocks")

@daily_cache
def russel_one_thousand_composition():
    return get_json("/market/index/russel-one-thousand").get("stocks")
    
@daily_cache
def amex_oil_composition():
    return get_json("/market/index/amex-oil-index").get("stocks")

@daily_cache
def djia_composition():
    return get_json("/market/index/djia").get("stocks")

@daily_cache
def bbc_global_composition():
    return get_json("/market/index/bbc-global-thirty").get("stocks")

@daily_cache
def ibovespa_composition():
    return get_json("/market/index/ibovespa").get("stocks")
@daily_cache
def ftse100_composition():
    return get_json("/market/index/ftse-one-hundred").get("stocks")

@daily_cache
def ftse250_composition():
    return get_json("/market/index/ftse-two-fifty").get("stocks")

@daily_cache
def nifty_fifty_composition():
    return get_json("/market/index/nifty-fifty").get("stocks")

@daily_cache
def djgt_fifty_composition():
    return get_json("/market/index/dow-jones-global-titans-fifty").get("stocks")

@daily_cache
def dax_thirty_composition():
    return get_json("/market/index/dax-thirty").get("stocks")

@daily_cache
def euro100_composition():
    return get_json("/market/index/euro-next-one-hundred").get("stocks")

@daily_cache
def djta_composition():
    return get_json("/market/index/down-jones-transportation-average").get("stocks")

@daily_cache
def djua_composition():
    return get_json("/market/index/down-jones-utility-average").get("stocks")

@daily_cache
def nasdaq100_composition():
    return get_json("/market/index/nasdaq-one-hundred").get("stocks")

@daily_cache
def phlx_semi_composition():
    return get_json("/market/index/phlx-semiconductor").get("stocks")

@daily_cache
def phlx_gold_composition():
    return get_json("/market/index/phlx-gold-and-silver").get("stocks")

@daily_cache
def nikkei225_composition():
    return get_json("/market/index/nikkei-two-twenty-five").get("stocks")

@daily_cache
def omx_nordic_composition():
    return get_json("/market/index/omx-nordic-forty").get("stocks")

@daily_cache
def nyse_arca_composition():
    return get_json("/market/index/nyse-arca-major-market-index").get("stocks")

@daily_cache
def s_and_p_400():
    return get_json("/market/index/s-and-p-four-hundred").get("stocks")

@daily_cache
def s_and_p_100():
    return get_json("/market/index/s-and-p-one-hundred").get("stocks")

@daily_cache
def s_and_p_global_100():
    return get_json("/market/index/s-and-p-global-one-hundred").get("stocks")

@daily_cache
def russel_2000_composition():
    return get_json("/market/index/russel-two-thousand").get("stocks")

@daily_cache
def niftybank():
    return get_json("/market/index/niftybank").get("stocks")
