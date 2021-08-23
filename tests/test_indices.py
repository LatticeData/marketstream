import pytest

from latticestockdataclient.indices import (
    s_and_p_composition,
    nasdaq_composition,
    russel_one_thousand_composition,
    amex_oil_composition,
    djia_composition,
    bbc_global_composition,
    ibovespa_composition,
    ftse100_composition,
    ftse250_composition,
    nifty_fifty_composition,
    djgt_fifty_composition,
    dax_thirty_composition,
    euro100_composition,
    djta_composition,
    djua_composition,
    nasdaq100_composition,
    phlx_semi_composition,
    phlx_gold_composition,
    nikkei225_composition,
    omx_nordic_composition,
    nyse_arca_composition,
    s_and_p_400,
    s_and_p_100,
    s_and_p_global_100,
    russel_2000_composition,
    niftybank
)


def index(data, expected_tickers, min_count=8):
    return (
        len(data) >= min_count
        and sum([ticker in data for ticker in expected_tickers]) == len(expected_tickers)
    )


def test_s_and_p_composition():
    data = s_and_p_composition()
    assert index(data, ["AAPL", "GM"], 450)

def test_nasdaq_composition():
    data = nasdaq_composition()
    assert index(data, ["AAPL", "GOOG"], 90)

def test_russel_one_thousand_composition():
    data = russel_one_thousand_composition()
    assert index(data, ["AAPL", "INTC"], 900)

def test_amex_oil_composition():
    data = amex_oil_composition()
    assert index(data, ["TOT", "VLO"])

def test_djia_composition():
    data = djia_composition()
    assert index(data, ["KO", "JPM"])

def test_bbc_global_composition():
    data = bbc_global_composition()
    assert index(data, ["PG", "RDSA"], 25)

def test_ibovespa_composition():
    data = ibovespa_composition()
    assert index(data, ["VVAR3", "WEGE3"])

def test_ftse100_composition():
    data = ftse100_composition()
    assert index(data, ["AAL", "WTB"], 90)

def test_ftse250_composition():
    data = ftse250_composition()
    assert index(data, ["AAF", "XPP"], 225)

def test_nifty_fifty_composition():
    data = nifty_fifty_composition()
    assert index(data, ["COALINDIA.NS", "NTPC.NS"], 30)

def test_djgt_fifty_composition():
    data = djgt_fifty_composition()
    assert index(data, ["DD", "XOM"], 40)

def test_dax_thirty_composition():
    data = dax_thirty_composition()
    assert index(data, ["MRK.DE", "MTX.DE"], 25)

def test_euro100_composition():
    data = euro100_composition()
    assert index(data, ["AC", "AGN"], 80)

def test_djta_composition():
    data = djta_composition()
    assert index(data, ["LSTR", "LUV"])

def test_djua_composition():
    data = djua_composition()
    assert index(data, ["AES", "ATO"])

def test_nasdaq100_composition():
    data = nasdaq100_composition()
    assert index(data, [], 90)

def test_phlx_semi_composition():
    data = phlx_semi_composition()
    assert index(data, ["MU", "MPWR"])

def test_phlx_gold_composition():
    data = phlx_gold_composition()
    assert index(data, ['BVN', 'CDER'])

def test_nikkei225_composition():
    data = nikkei225_composition()
    assert index(data, ["6103", "6302"], 200)

def test_omx_nordic_composition():
    data = omx_nordic_composition()
    assert index(data, ["NESTE", "ORSTED"], 35)

def test_nyse_arca_composition():
    data = nyse_arca_composition()
    assert index(data, ["MSFT", "PG"])

def test_s_and_p_400():
    data = s_and_p_400()
    assert index(data, ["BXS", "BYD"], 350)

def test_s_and_p_100():
    data = s_and_p_100()
    assert index(data, ["COF", "COP"], 80)

def test_s_and_p_global_100():
    data = s_and_p_global_100()
    assert index(data, ['ALV', 'AAL'], 60)

def test_russel_2000_composition():
    data = russel_2000_composition()
    assert index(data, ["ADTN", "DNLI"])

def test_niftybank():
    data = niftybank()
    assert index(data, ["BANDHANBNK", "BANKBARODA"])
