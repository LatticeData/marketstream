from stocksdata.util.ttlcache import daily_cache
from stocksdata.util.get import *

@daily_cache
def raw_quote(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/quote", params).get("quote")

@daily_cache
def raw_historical_prices(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/historical-prices", params)

@daily_cache
def technical_insights(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/technical-insights", params).get("technical_insights")

@daily_cache
def options_contracts(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/options-contracts", params)

@daily_cache
def price(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/price", params).get("price")

@daily_cache
def summary_detail(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/summary-detail", params).get("summary_detail")

@daily_cache
def key_statistics(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/stats", params).get("stats")

@daily_cache
def company_profile(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/company-profile", params).get("company_profile")

@daily_cache
def earnings(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/earnings", params).get("earnings")

@daily_cache
def financial_data(ticker_symbol):
    params = {"ticker_symbol":ticker_symbol}
    return get_json("/yfinance/financial-data", params).get("financial_data")

@daily_cache
def upgrade_downgrade_history(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/upgrade-downgrade-history", params).get("upgrade_downgrade_history")

@daily_cache
def esg_scores(ticker_symbol):
    params = {"ticker_symbol":ticker_symbol}
    return get_json("/yfinance/esg-scores", params).get("esg")

@daily_cache
def calendar_events(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/calendar-events", params).get("calendar_events")

@daily_cache
def annual_income_statement(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/annual-income-statements", params).get("annual_income_statements")

@daily_cache
def quarterly_income_statement(ticker_symbol):
    params = {"ticker_symbol":ticker_symbol}
    return get_json("/yfinance/quarterly-income-statements", params).get("quarterly_income_statements")

@daily_cache
def annual_balance_sheet(ticker_symbol):
    params = {"ticker_symbol":ticker_symbol}
    return get_json("/yfinance/annual-balance-sheets", params).get("annual_balance_sheets")

@daily_cache
def quarterly_balance_sheet(ticker_symbol):
    params = {"ticker_symbol": ticker_symbol}
    return get_json("/yfinance/quarterly-balance-sheets", params).get("quarterly_balance_sheets")