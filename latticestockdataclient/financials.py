from latticestockdataclient.util.ttlcache import daily_cache
from latticestockdataclient.util.get import *

## Basics #########################################################################################################################################

@daily_cache
def annual_balance_sheet(ticker_symbol):
    return get_json("/stock/financials/balance-sheet/annual-historical", {"ticker_symbol": ticker_symbol})

@daily_cache
def quarterly_balance_sheet(ticker_symbol):
    return get_json("/stock/financials/balance-sheet/quarterly-historical", {"ticker_symbol": ticker_symbol})

@daily_cache
def latest_annual_balance_sheet(ticker_symbol):
    return get_json("/stock/financials/balance-sheet/annual-latest", {"ticker_symbol": ticker_symbol})

@daily_cache
def latest_quarterly_balance_sheet(ticker_symbol):
    return get_json("/stock/financials/balance-sheet/quarterly-latest", {"ticker_symbol": ticker_symbol})

@daily_cache
def annual_income_statement(ticker_symbol):
    return get_json("/stock/financials/income-statement/annual-historical", {"ticker_symbol": ticker_symbol})

@daily_cache
def quarterly_income_statement(ticker_symbol):
    return get_json("/stock/financials/income-statement/quarterly-historical", {"ticker_symbol": ticker_symbol})

@daily_cache
def latest_annual_income_statement(ticker_symbol):
    return get_json("/stock/financials/income-statement/annual-latest", {"ticker_symbol": ticker_symbol})

@daily_cache
def latest_quarterly_income_statement(ticker_symbol):
    return get_json("/stock/financials/income-statement/quarterly-latest", {"ticker_symbol": ticker_symbol})


## Income statement line items ####################################################################################################################

def revenue(self, ticker_symbol):
    return latest_annual_income_statement(ticker_symbol).get("Total Revenue", 0.0)

def gross_profit(self, ticker_symbol):
    return latest_annual_income_statement(ticker_symbol).get("Gross Profit", 0.0)


