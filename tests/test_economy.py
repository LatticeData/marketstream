import pytest

from stocksdata.economy import (
    risk_free_rate,
    last_year_market_return
)

def test_risk_free_rate():
    data = risk_free_rate()
    assert (
        isinstance(data, float)
        and data > 0.0
        and data < 0.05
    )

def test_last_year_market_return():
    data = last_year_market_return()
    assert (
        data is not None
        and isinstance(data, float)
    )
