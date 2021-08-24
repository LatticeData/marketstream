import pytest

from stocksdata.yahoo_finance import (
    raw_quote,
    raw_historical_prices,
    technical_insights,
    options_contracts,
    price,
    summary_detail,
    key_statistics,
    company_profile,
    earnings,
    financial_data,
    upgrade_downgrade_history,
    esg_scores,
    calendar_events,
    annual_income_statement,
    quarterly_income_statement,
    annual_balance_sheet,
    quarterly_balance_sheet

)

ticker_symbol = "AAPL"

def test_raw_quote():
    
    data = raw_quote(ticker_symbol)
    assert (
        data["symbol"] == "AAPL"
        and data["regularMarketOpen"] is not None
        and isinstance(data["regularMarketOpen"]["raw"], float) 
    )

def test_raw_historical_prices():
    data = raw_historical_prices(ticker_symbol)
    resp_key = 'historical prices'
    assert (
        len(data[resp_key]) > 0
        and "Open" in list(data[resp_key][0].keys())
        and data[resp_key][0] is not None
        and isinstance(data[resp_key][0]["Open"], float)
    )

def test_technical_insights():
    data = technical_insights(ticker_symbol)
    assert (
        data is not None
        and data["symbol"] == "AAPL"
        and "companySnapshot" in list(data.keys())
        and data["companySnapshot"] is not None
        and "company" in list(data["companySnapshot"].keys())
        and "dividends" in list(data["companySnapshot"]["company"].keys())
        and isinstance(data["companySnapshot"]["company"]["dividends"], float)
    )

def test_options_contracts():
    data = options_contracts(ticker_symbol)
    assert (
        data["status"] == "success"
        and "options" in data
        and data["options"] is not None
        and "puts" in data["options"]
        and data["options"]["puts"] is not None
        and "calls" in data["options"]
        and data["options"]["calls"] is not None
        and "change" in list(data["options"]["calls"][0].keys())
        and data["options"]["calls"][0]["change"] is not None
        and isinstance(data["options"]["calls"][0]["change"]["fmt"], str)
        and "lastPrice" in list(data["options"]["calls"][0].keys())
        and data["options"]["calls"][0]["lastPrice"] is not None
        and isinstance(data["options"]["calls"][0]["lastPrice"]["raw"], float)
    )

def test_price():
    data = price(ticker_symbol)
    assert (
        data is not None
        and "symbol" in list(data.keys())
        and data["symbol"] == "AAPL"
        and "regularMarketOpen" in list(data.keys())
        and data["regularMarketOpen"] is not None
        and isinstance(data["regularMarketOpen"]["raw"], float) 
    )

def test_summary_detail():
    data = summary_detail(ticker_symbol)
    assert (
        data is not None
        and "regularMarketOpen" in list(data.keys())
        and data["regularMarketOpen"] is not None
        and isinstance(data["regularMarketOpen"]["raw"], float) 
    )

def test_key_statistics():
    data = key_statistics(ticker_symbol)
    assert (
        data is not None
        and "enterpriseToRevenue" in list(data.keys())
        and data["enterpriseToRevenue"] is not None
        and isinstance(data["enterpriseToRevenue"]["raw"], float) 
    )

def test_company_profile():
    data = company_profile(ticker_symbol)
    assert (
        data is not None
        and "zip" in list(data.keys())
        and data["zip"] is not None
        and isinstance(data["zip"], str)
    )

def test_earnings():
    data = earnings(ticker_symbol)
    assert (
        data is not None
        and "earningsChart" in list(data.keys())
        and data["earningsChart"] is not None
        and data["earningsChart"]["quarterly"] is not None
        and data["earningsChart"]["quarterly"][0]["actual"] is not None
        and isinstance(data["earningsChart"]["quarterly"][0]["actual"]["raw"], float)
    )

def test_financial_data():
    data = financial_data(ticker_symbol)
    assert (
        data is not None
        and "profitMargins" in list(data.keys())
        and data["profitMargins"] is not None
        and isinstance(data["profitMargins"]["raw"], float)
    )

def test_upgrade_downgrade_history():
    data = upgrade_downgrade_history(ticker_symbol)
    assert (
        data is not None
        and "history" in list(data.keys())
        and isinstance(data["history"], list)
        and "epochGradeDate" in list(data["history"][0].keys())
        and isinstance(data["history"][0]["epochGradeDate"], int)
    )

def test_esg_scores():
    data = esg_scores(ticker_symbol)
    assert (
        data is not None
        and "peerSocialPerformance" in list(data.keys())
        and data["peerSocialPerformance"] is not None
        and isinstance(data["peerSocialPerformance"]["min"], float)
    )

def test_calendar_events():
    data = calendar_events(ticker_symbol)
    assert (
        data is not None
        and "earnings" in list(data.keys())
        and data["earnings"] is not None
        and "earningsAverage" in list(data["earnings"].keys())
        and data["earnings"]["earningsAverage"] is not None
    )
    

def test_annual_income_statement():
    data = annual_income_statement(ticker_symbol)
    assert (
        isinstance(data, list)
        and len(data) == 4
        and "researchDevelopment" in list(data[0].keys())
        and data[0]["researchDevelopment"] is not None
        and isinstance(data[0]["researchDevelopment"]["raw"], int)
    )

def test_quarterly_income_statement():
    data = quarterly_income_statement(ticker_symbol)
    assert (
        isinstance(data, list)
        and len(data) == 4
        and "researchDevelopment" in list(data[0].keys())
        and data[0]["researchDevelopment"] is not None
        and isinstance(data[0]["researchDevelopment"]["raw"], int)
    )

def test_annual_balance_sheet():
    data = annual_balance_sheet(ticker_symbol)
    assert (
        isinstance(data, list)
        and len(data) == 4
        and "totalLiab" in list(data[0].keys())
        and data[0]["totalLiab"] is not None
        and isinstance(data[0]["totalLiab"]["raw"], int)
    )

def test_quarterly_balance_sheet():
    data = quarterly_balance_sheet(ticker_symbol)
    assert (
        isinstance(data, list)
        and len(data) == 4
        and "totalLiab" in list(data[0].keys())
        and data[0]["totalLiab"] is not None
        and isinstance(data[0]["totalLiab"]["raw"], int)
    )
