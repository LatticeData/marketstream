import pytest

from stocksdata.valuation import (
    cost_of_equity,
    enterprise_value,
    historical_valuation_measures,
    valuation_measures
)

ticker_symbol = "AAPL"

def test_cost_of_equity():
    data = cost_of_equity(ticker_symbol)
    assert (
        data is not None
        and isinstance(data, float)
    )

def test_enterprise_value():
    data = enterprise_value(ticker_symbol)
    assert (
        data is not None
        and isinstance(data, float)
    )

def test_historical_valuation_measures():
    data = historical_valuation_measures(ticker_symbol)
    assert (
        data is not None
        and len(data) > 5
        and "Market Cap (intraday)" in list(data[0].keys())
    )

def test_valuation_measures():
    data = valuation_measures(ticker_symbol)
    assert (
        data is not None
        and "Market Cap (intraday)" in data
    )
