import pytest

from stocksdata.stock import (
    company_profile,
    quote,
    historical_prices,
    key_stats
)

ticker_symbol = "AAPL"

def test_company_profile():
    symbol = ticker_symbol
    data = company_profile(symbol)
    assert (
        data["Sector"] == "Technology"
        and data["Company Name"] == "Apple Inc."
        and data["Industry"] == "Consumer Electronics"
        and data["Full Time Employees"] > 99999
        and data["Description"] is not None
        and data["Website"] == "http://www.apple.com"
        and data["Country"] == "United States"
        and data["State"] == "CA"
        and data["City"] == "Cupertino"
    )

def test_quote():
    data = quote(ticker_symbol)
    assert (
        "Current Price" in data
        and isinstance(data["Current Price"], float)
    )

def test_historical_prices():
    data = historical_prices(ticker_symbol)
    assert (
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_key_stats():
    data = key_stats(ticker_symbol)
    assert (
        "52-Week Change" in data
        and isinstance(data["52-Week Change"], float)
        and "Float" in data
    )
