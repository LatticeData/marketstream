import pytest

from latticestockdataclient.similarity import (
    business_description_similarity,
    industry_similarity,
    stock_price_correlation
)

def test_business_description_similarity():
    ticker_symbol1 = "AAPL"
    ticker_symbol2 ="GOOG"
    data = business_description_similarity(ticker_symbol1,ticker_symbol2)
    assert (
        data is not None
        and isinstance(data, float)
        and data >= 0.0
        and data <= 1.0
    )

def test_industry_similarity():
    ticker_symbol1 = "AAPL"
    ticker_symbol2 ="GOOG"
    data =  industry_similarity(ticker_symbol1,ticker_symbol2)
    assert (
        data is not None
        and isinstance(data, float)
        and data >= 0.0
        and data <= 2.0
    )

def test_stock_price_correlation():
    ticker_symbol1 = "AAPL"
    ticker_symbol2 ="GOOG"
    data = stock_price_correlation(ticker_symbol1,ticker_symbol2)
    assert (
        data is not None
        and isinstance(data, float)
        and data >= -1.0
        and data <= 1.0
    )
