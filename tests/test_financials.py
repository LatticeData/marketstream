import pytest

from stocksdata.financials import (
    annual_balance_sheet,
    quarterly_balance_sheet,
    latest_annual_balance_sheet,
    latest_quarterly_balance_sheet,
    annual_income_statement,
    quarterly_income_statement,
    latest_annual_income_statement,
    latest_quarterly_income_statement
)

ticker_symbol = "AAPL"

def test_quarterly_balance_sheets():
    data = quarterly_balance_sheet(ticker_symbol)
    assert (
        data is not None
        and "Total Assets" in data[0]
    )

def test_annual_balance_sheets():
    data = annual_balance_sheet(ticker_symbol)
    assert (
        data is not None
        and "Total Assets" in data[0]
    )

def test_quarterly_income_statement():
    data = quarterly_income_statement(ticker_symbol)
    assert (
        data is not None
        and "Net Margin" in data[0]
    )

def test_annual_income_statement():
    data = annual_income_statement(ticker_symbol)
    assert (
        data is not None
        and "Net Margin" in data[0]
    )

def test_latest_quarterly_income_statement():
    data = latest_quarterly_income_statement(ticker_symbol)
    assert (
        data is not None
        and "Net Margin" in data
    )

def test_latest_annual_income_statement():
    data = latest_annual_income_statement(ticker_symbol)
    assert (
        data is not None
        and "Net Margin" in data
    )

def test_latest_quarterly_balance_sheet():
    data = latest_quarterly_balance_sheet(ticker_symbol)
    return (
        data is not None
        and "Total Assets" in data
    )

def test_latest_annual_balance_sheet():
    data = latest_annual_balance_sheet(ticker_symbol)
    return (
        data is not None
        and "Total Assets" in data
    )
