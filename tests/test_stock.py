import pytest

from latticestockdataclient.stock import (
    company_profile,
    quote,
    historical_prices,
    key_stats
)

ticker_symbol = "AAPl"

def test_company_profile():
    symbol = ticker_symbol
    data = company_profile(symbol)
    assert (
        data["status"] == "success"
        and data["company_profile"]["Sector"] == "Technology"
        and data["company_profile"]["Company Name"] == "Apple Inc."
        and data["company_profile"]["Industry"] == "Consumer Electronics"
        and data["company_profile"]["Full Time Employees"] > 99999
        and data["company_profile"]["Description"] is not None
        and data["company_profile"]["Website"] == "http://www.apple.com"
        and data["company_profile"]["Country"] == "United States"
        and data["company_profile"]["State"] == "CA"
        and data["company_profile"]["City"] == "Cupertino"
    )

def test_quote():
    data = quote(ticker_symbol)
    assert (
        data["status"] == "success"
        and "Current Price" in data["quote"]
        and isinstance(data["quote"]["Current Price"], float)
    )

def test_historical_prices():
    data = historical_prices(ticker_symbol)
    resp_key = 'historical prices'
    assert (
        len(data[resp_key]) > 0
        and "Open" in list(data[resp_key][0].keys())
        and data[resp_key][0] is not None
        and isinstance(data[resp_key][0]["Open"], float)
    )

def test_key_stats():
    data = key_stats(ticker_symbol)
    assert (
        data["status"] == "success"
        and "52-Week Change" in data["key_statistics"]
        and isinstance(data["key_statistics"]["52-Week Change"], float)
        and "Float" in data["key_statistics"]
    )
