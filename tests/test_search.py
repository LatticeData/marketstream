import pytest

from latticestockdataclient.search import (
    wikipedia_url_to_ticker_symbol,
    #stock_screener,
    isin_to_ticker_symbol,
    company_name_to_ticker_symbol
)

def test_wikipedia_url_to_ticker_symbol():
    wikipedia_url= "https://en.wikipedia.org/wiki/Apple_Inc."
    data = wikipedia_url_to_ticker_symbol(wikipedia_url)
    return (
        data == "AAPL"
    )

#def test_stock_screener():
 #   param = {"country": "United States"}
  #  data = stock_screener(param)
   # assert (
    #    isinstance(data, list)
    #)

def test_isin_to_ticker_symbol():
    isin = "US0378331005"
    data = isin_to_ticker_symbol(isin)
    return (
        data == "AAPL"
    )

def test_company_name_to_ticker_symbol():
    company_name = "Apple"
    data = company_name_to_ticker_symbol(company_name)
    return(
        data == "AAPL"
    )
