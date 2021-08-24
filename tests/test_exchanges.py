import pytest

from stocksdata.exchanges import (
    all_public_companies,
    nasdaq_exchange_composition,
    nyse_composition,
    shanghai_exchange_composition,
    hong_kong_exchange_composition,
    london_exchange_composition
)

def test_all_public_companies():
    data = all_public_companies()
    min_count = 6000
    assert (
        isinstance(data, list)
        and len(data) > min_count
    )

def test_nasdaq_exchange_composition():
    data = nasdaq_exchange_composition()
    min_count = 3000
    assert (
        isinstance(data, list)
        and len(data) > min_count
    )

def test_nyse_composition():
    data = nyse_composition()
    min_count = 2000
    assert (
        isinstance(data, list)
        and len(data) > min_count
    )

def test_shanghai_exchange_composition():
    data = shanghai_exchange_composition()
    min_count = 500
    assert (
        isinstance(data, list)
        and len(data) > min_count
    )

def test_hong_kong_exchange_composition():
    data = hong_kong_exchange_composition()
    min_count = 1000
    assert (
        isinstance(data, list)
        and len(data) > min_count
    )

def test_london_exchange_composition():
    data = london_exchange_composition()
    min_count = 1000
    assert (
        isinstance(data, list)
        and len(data) > min_count
    )
