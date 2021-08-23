import pytest

from latticestockdataclient.screeners import (
    conservative_foreign_funds,
    most_actives,
    most_shorted_stocks,
    undervalued_growth_stocks,
    growth_technology_stocks,
    day_gainers,
    day_losers,
    undervalued_large_caps,
    aggresive_small_caps,
    small_cap_gainers,
    top_mutual_funds,
    portfolio_anchors,
    solid_large_growth_funds,
    solid_midcap_growth_funds,
    high_yield_bonds

)

def test_conservative_foreign_funds():
    data = conservative_foreign_funds()
    assert (
        data is not None
        and len(data) > 0
    )

def test_most_actives():
    data = most_actives()
    assert (
        data is not None
        and len(data) > 0
    )

def test_most_shorted_stocks():
    data = most_shorted_stocks()
    assert (
        data is not None
        and len(data) > 0
    )


def test_undervalued_growth_stocks():
    data = undervalued_growth_stocks()
    assert (
        data is not None
        and len(data) > 0
    )


def test_growth_technology_stocks():
    data = growth_technology_stocks()
    assert (
        data is not None
        and len(data) > 0
    )


def test_day_gainers():
    data = day_gainers()
    assert (
        data is not None
        and len(data) > 0
    )


def test_day_losers():
    data = day_losers()
    assert (
        data is not None
        and len(data) > 0
    )


def test_undervalued_large_caps():
    data = undervalued_large_caps()
    assert (
        data is not None
        and len(data) > 0
    )


def test_aggresive_small_caps():
    data = aggresive_small_caps()
    assert (
        data is not None
        and len(data) > 0
    )


def test_small_cap_gainers():
    data = small_cap_gainers()
    assert (
        data is not None
        and len(data) > 0
    )


def test_top_mutual_funds():
    data = top_mutual_funds()
    assert (
        data is not None
        and len(data) > 0
    )


def test_portfolio_anchors():
    data = portfolio_anchors()
    assert (
        data is not None
        and len(data) > 0
    )


def test_solid_large_growth_funds():
    data = solid_large_growth_funds()
    assert (
        data is not None
        and len(data) > 0
    )


def test_solid_midcap_growth_funds():
    data = solid_midcap_growth_funds()
    assert (
        data is not None
        and len(data) > 0
    )


def test_high_yield_bonds():
    data = high_yield_bonds()
    assert (
        data is not None
        and len(data) > 0
    )
