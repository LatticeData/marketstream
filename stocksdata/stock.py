from stocksdata.util.ttlcache import daily_cache
from stocksdata.util.get import *


## company-info ##################################################################################################################################

@daily_cache
def company_profile(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/company-info", params).get('company_profile')

def company_name(ticker_symbol):
	return company_profile(ticker_symbol).get("Company Name")

def sector(ticker_symbol):
	return company_profile(ticker_symbol).get("Sector")

def industry(ticker_symbol):
	return company_profile(ticker_symbol).get("Industry")

def business_description(ticker_symbol):
	return company_profile(ticker_symbol).get("Description")

def website_url(ticker_symbol):
	return company_profile(ticker_symbol).get("Website")

def full_time_employees(ticker_symbol):
	profile = company_profile(ticker_symbol)
	if "Full Time Employees" in profile:
		return int(profile["Full Time Employees"])
	else:
		return None

def country(ticker_symbol):
	return company_profile(ticker_symbol).get("Country")

def state(ticker_symbol):
	return company_profile(ticker_symbol).get("State")
def city(ticker_symbol):
	return company_profile(ticker_symbol).get("City")

## quote ########################################################################################################################################

@daily_cache
def quote(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/quote", params).get('quote')

## historical-prices ####################################################################################################################################

@daily_cache
def historical_prices(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/historical-prices", params).get('historical prices')

## key-stats #####################################################################################################################################
def key_stats(ticker_symbol):
	params = {"ticker_symbol": ticker_symbol}
	return get_json("/stock/key-stats", params).get('key_statistics')

