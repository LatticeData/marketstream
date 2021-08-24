from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *


## company-info ##################################################################################################################################

@daily_cache
def company_profile(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/company-info", params)

def company_name(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["Company Name"]

def sector(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["Sector"]

def industry(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["Industry"]

def business_description(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["Description"]

def website_url(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["Website"]

def full_time_employees(ticker_symbol):
	profile = company_profile(ticker_symbol)["company_profile"]
	if "Full Time Employees" in profile:
		return int(profile["Full Time Employees"])
	else:
		return None

def country(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["Country"]

def state(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["State"]
def city(ticker_symbol):
	return company_profile(ticker_symbol)["company_profile"]["City"]

## quote ########################################################################################################################################

@daily_cache
def quote(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/quote", params)

## historical-prices ####################################################################################################################################

@daily_cache
def historical_prices(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/historical-prices", params)

## key-stats #####################################################################################################################################
def key_stats(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/key-stats", params)

