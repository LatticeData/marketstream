import pytest

from stocksdata.indicators import (
    sma,
    smav,
    so,
    wilder,
    adx,
    rsi,
    bb,
    macd,
    roc,
    atr
)

ticker_symbol = "NFLX"
short_period = "5"
long_period = "15"
period= "5"

def test_sma():
    data  = sma(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_smav():
    data  = smav(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_so():
    data  = so(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_wilder():
    data = wilder(ticker_symbol,period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )
    
def test_adx():
    data  = adx(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_rsi():
    data  = rsi(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_bb():
    data = bb(ticker_symbol,period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_roc():
    data = roc(ticker_symbol,period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_macd():
    data  = macd(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )

def test_atr():
    data  = atr(ticker_symbol,short_period,long_period)
    assert(
        len(data) > 0
        and "Open" in list(data[0].keys())
        and data[0] is not None
        and isinstance(data[0]["Open"], float)
    )