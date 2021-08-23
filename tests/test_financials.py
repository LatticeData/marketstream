import pytest
import sys
sys.path.insert(0, '../latticestockdataclient/')

from latticestockdataclient.financials import (
    annual_balance_sheet,
    quarterly_balance_sheet,
    latest_annual_balance_sheet,
    latest_quarterly_balance_sheet,
    annual_income_statement,
    quarterly_income_statement,
    latest_annual_income_statement,
    latest_quarterly_income_statement
)

ticker_symbol = "AAPl"

def test_quarterly_balance_sheets():
    data = quarterly_balance_sheet(ticker_symbol)
    assert (
        data["status"] == "success"
        and data["quarterly_historical_balance_sheets"] is not None
        and "Total Assets" in data["quarterly_historical_balance_sheets"][0]
    )

def test_annual_balance_sheets():
    data = annual_balance_sheet(ticker_symbol)
    assert (
        data["status"] == "success"
        and data["annual_historical_balance_sheets"] is not None
        and "Total Assets" in data["annual_historical_balance_sheets"][0]
    )

def test_quarterly_income_statement():
    data = quarterly_income_statement(ticker_symbol)
    assert (
        data["status"] == "success"
        and data["quarterly_historical_income_statements"] is not None
        and "Net Margin" in data["quarterly_historical_income_statements"][0]
    )

def test_annual_income_statement():
    data = annual_income_statement(ticker_symbol)
    assert (
        data["status"] == "success"
        and data["annual_historical_income_statements"] is not None
        and "Net Margin" in data["annual_historical_income_statements"][0]
    )

def test_latest_quarterly_income_statement():
    data = latest_quarterly_income_statement(ticker_symbol)
    assert (
        data["status"] == "success"
        and data["current_quarterly_income_statement"] is not None
        and "Net Margin" in data["current_quarterly_income_statement"]
    )

def test_latest_annual_income_statement():
    data = latest_annual_income_statement(ticker_symbol)
    assert (
        data["status"] == "success"
        and data["current_annual_income_statement"] is not None
        and "Net Margin" in data["current_annual_income_statement"]
    )

def test_latest_quarterly_balance_sheet():
    data = latest_quarterly_balance_sheet(ticker_symbol)
    return (
        data["status"] == "success"
        and data["current_quarterly_balance_sheet"] is not None
        and "Total Assets" in data["current_quarterly_balance_sheet"]
    )

def test_latest_annual_balance_sheet():
    data = latest_annual_balance_sheet(ticker_symbol)
    return (
        data["status"] == "success"
        and data["current_annual_balance_sheet"] is not None
        and "Total Assets" in data["current_annual_balance_sheet"]
    )