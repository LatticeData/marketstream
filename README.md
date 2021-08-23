# StockData Python Client

An user friendly library to fetch data related to stock market in no time.

## Contents

  - [Overview](#Overview)
  - [Setup](#Setup)
    - [Installation](#Installation)
    - [API Authentication](#API-Authentication)
    - [Dependencies](#Dependencies)
  - [License](#license)
  - [Usage](#Usage)
    - [Category: Buzz](#category-buzz)
      - [Function: news_sentiment](#function-news_sentiment)
      - [Function: news](#function-news)
      - [Function: twitter_sentiment](#function-twitter_sentiment)
      - [Function: fear_and_greed_index](#function-fear_and_greed_index)
      - [Function: wallstreetbets_mentions](#function-wallstreetbets_mentions)
    - [Category: Economy](#category-Economy)
      - [Function: risk_free_rate](#function-risk_free_rate)    
      - [Function: last_year_market_return](#function-last_year_market_return)
    - [Category: Exchanges](#category-Exchanges)
      - [Function: all_public_companies](#function-all_public_companies)
      - [Function: nasdaq_exchange_composition](#function-nasdaq_exchange_composition)
      - [Function: nyse_composition](#function-nyse_composition)
      - [Function: shanghai_exchange_composition](#function-shanghai_exchange_composition)
      - [Function: hong_kong_exchange_composition](#function-hong_kong_exchange_composition)
      - [Function: london_exchange_composition](#function-london_exchange_composition)  
    - [Category: Financials](#category-Financials)
      - [Function: annual_balance_sheet](#function-annual_balance_sheet)
      - [Function: quarterly_balance_sheet](#function-quarterly_balance_sheet)
      - [Function: latest_annual_balance_sheet](#function-latest_annual_balance_sheet)
      - [Function: latest_quarterly_balance_sheet](#function-latest_quarterly_balance_sheet)
      - [Function: annual_income_statement](#function-annual_income_statement)
      - [Function: quarterly_income_statement](#function-quarterly_income_statement)
      - [Function: latest_annual_income_statement](#function-latest_annual_income_statement)
      - [Function: latest_quarterly_income_statement](#function-latest_quarterly_income_statement)
    - [Category: Screeners](#category-Screeners)
      - [Function: conservative_foreign_funds](#function-conservative_foreign_funds)
      - [Function: most_actives](#function-most_actives)
      - [Function: most_shorted_stocks](#function-most_shorted_stocks)
      - [Function: undervalued_growth_stocks](#function-undervalued_growth_stocks)
      - [Function: growth_technology_stocks](#function-growth_technology_stocks)
      - [Function: day_gainers](#function-day_gainers)
      - [Function: day_losers](#function-day_losers)
      - [Function: undervalued_large_caps](#function-undervalued_large_caps)
      - [Function: aggresive_small_caps](#function-aggresive_small_caps)
      - [Function: small_cap_gainers](#function-small_cap_gainers)
      - [Function: top_mutual_funds](#function-top_mutual_funds)
      - [Function: portfolio_anchors](#function-portfolio_anchors)
      - [Function: solid_large_growth_funds](#function-solid_large_growth_funds)
      - [Function: solid_midcap_growth_funds](#function-solid_midcap_growth_funds)
      - [Function: high_yield_bonds](#function-high_yield_bonds)
    - [Category: Search](#category-Search)
      - [Function: wikipedia_url_to_ticker_symbol](#function-wikipedia_url_to_ticker_symbol)
      - [Function: isin_to_ticker_symbol](#function-isin_to_ticker_symbol)
      - [Function: company_name_to_ticker_symbol](#function-company_name_to_ticker_symbol)
    - [Category: Similarity](#category-Similarity)
      - [Function: business_description_similarity](#function-business_description_similarity)
      - [Function: industry_similarity](#function-industry_similarity)
      - [Function: stock_price_correlation](#function-stock_price_correlation)
    - [Category: Stock](#category-Stock)
      - [Function: company_profile](#function-company_profile)
      - [Function: Quote](#function-Quote)
      - [Function: historical_prices](#function-historical_prices)
      - [Function: key_stats](#function-key_stats)
    - [Category: Valuation](#category-Valuation)
      - [Function: cost_of_equity](#function-cost_of_equity)
      - [Function: enterprise_value](#function-enterprise_value)
      - [Function: historical_valuation_measures](#function-historical_valuation_measures)
      - [Function: valuation_measures](#function-valuation_measures)
    - [Category: Yahoo finance](#category-Yahoo_finance)
      - [Function: raw_quote](#function-raw_quote)
      - [Function: raw_historical_prices](#function-raw_historical_prices)
      - [Function: technical_insights](#function-technical_insights)
      - [Function: options_contracts](#function-options_contracts)
      - [Function: price](#function-price)
      - [Function: summary_detail](#function-summary_detail)
      - [Function: key_statistics](#function-key_statistics)
      - [Function: company_profile](#function-company_profile)
      - [Function: earnings](#function-earnings)
      - [Function: financial_data](#function-financial_data)
      - [Function: upgrade_downgrade_history](#function-upgrade_downgrade_history)
      - [Function: esg_scores](#function-esg_scores)
      - [Function: calendar_events](#function-calendar_events)
      - [Function: annual_income_statement](#function-annual_income_statement)
      - [Function: quarterly_income_statement](#function-quarterly_income_statement)
      - [Function: annual_balance_sheet](#function-annual_balance_sheet)
      - [Function: quarterly_balance_sheet](#function-quarterly_balance_sheet)
    - [Category: Indices](#category-Indices)  
      - [Function: s_and_p_composition](#function-s_and_p_composition)
      - [Function: nasdaq_composition](#function-nasdaq_composition)
      - [Function: russel_one_thousand_composition](#function-russel_one_thousand_composition)
      - [Function: amex_oil_composition](#function-amex_oil_composition)
      - [Function: djia_composition](#function-djia_composition)
      - [Function: bbc_global_composition](#function-bbc_global_composition)
      - [Function: ibovespa_composition](#function-ibovespa_composition)
      - [Function: ftse100_composition](#function-ftse100_composition)
      - [Function: ftse250_composition](#function-ftse250_composition)
      - [Function: nifty_fifty_composition](#function-nifty_fifty_composition)
      - [Function: djgt_fifty_composition](#function-djgt_fifty_composition)
      - [Function: dax_thirty_composition](#function-dax_thirty_composition)
      - [Function: euro100_composition](#function-euro100_composition)
      - [Function: djta_composition](#function-djta_composition)
      - [Function: djua_composition](#function-djua_composition)
      - [Function: nasdaq100_composition](#function-nasdaq100_composition)
      - [Function: phlx_semi_composition](#function-phlx_semi_composition)
      - [Function: phlx_gold_composition](#function-phlx_gold_composition)
      - [Function: nikkei225_composition](#function-nikkei225_composition)
      - [Function: omx_nordic_composition](#function-omx_nordic_composition)
      - [Function: nyse_arca_composition](#function-nyse_arca_composition)
      - [Function: s_and_p_400](#function-s_and_p_400)
      - [Function: s_and_p_100](#function-s_and_p_100)
      - [Function: s_and_p_global_100](#function-s_and_p_global_100)
      - [Function: niftybank](#function-niftybank)

## Overview

## Setup

### Installation
The easiest way to install this package is using pip:
```bash
pip install LatticeStockDataClient
```
### API Authentication
To successfully use this library you will need an API key for the [Stock Data API](https://rapidapi.com/lattice-data-lattice-data-default/api/stock-market-data/) that powers it. Navigate to [RapidAPI](https://rapidapi.com/lattice-data-lattice-data-default/api/stock-market-data/) to sign up for a free API key and then save it to an environment variable called `STOCK_DATA_X_RAPID_API_KEY` in your environment. The library will automatically load that environment variable and use it to authenticate API calls made under the hood.

### Dependencies
This library relies on the following Python libraries:
 - numpy
 - python-dotenv
 - lxml
 - xmltodict
 - pytest
 - requests
 - cachetools
 - pymongo
 - pandas

These are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

## License

The Stock Data Python client is licensed under the
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Usage
### Category: Buzz
This package provides online buzz data about stocks, pulled from news outlets and social media.
#### Function: `news_sentiment`
```bash
news_sentiment(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Returns the sentiment for the given stock in recent news articles.
##### Example:
```bash
>>> from buzz import news_sentiment
>>> pprint(news_sentiment("AAPL"))
{
    'sentiment_score': 0.07747582205029015,
    'source_articles': [
        {
            'published_date': '2021-07-29T13:50:23',
            'sentiment_score': 0.0,
            'summary': "AAPL: What's Next for Apple as it Forms a Key Resistance Level?\xa0\xa0StockNews.com",
            'title': "AAPL: What's Next for Apple as it Forms a Key Resistance Level? - StockNews.com",
            'url': 'https://stocknews.com/news/aapl-whats-next-for-apple-as-it-forms-a-key-resistance/',
        },
        ...
      ],
}
```
#### Function: `news`
```bash
news(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`
##### Return value: 
News related to the required stock.
##### Example:
```bash
>>> from buzz import news
>>> pprint(news("AAPL"))
{
    'published_date': '2021-07-24T07:04:03',
    'summary': "What Does Apple Inc.'s (NASDAQ:AAPL) Share Price Indicate?\xa0\xa0Yahoo Finance",
    'title': "What Does Apple Inc.'s (NASDAQ:AAPL) Share Price Indicate? - Yahoo Finance",
    'url': 'https://finance.yahoo.com/news/does-apple-inc-nasdaq-aapl-070403595.html',
},
{
    'published_date': '2021-07-27T22:10:00',
    'summary': 'Apple Profit Sets Record on Strong iPhone Sales\xa0\xa0The Wall Street JournalApple Earnings: What Happened with AAPL\xa0\xa0InvestopediaApple Inc. (AAPL) CEO Tim Cook on Q3 2021 Results - Earnings Call Transcript\xa0\xa0Seeking AlphaApple Earnings (AAPL): 3Q Revenue Hits Record\xa0\xa0BloombergApple says chip shortage reaches iPhone, growth forecast slows\xa0\xa0ReutersView Full Coverage on Google News',
    'title': 'Apple Profit Sets Record on Strong iPhone Sales - The Wall Street Journal',
    'url': 'https://www.wsj.com/articles/apple-aapl-3q-earnings-report-2021-11627347443',
},
...
```
#### Function: `twitter_sentiment`
```bash
twitter_sentiment(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False

##### Return value: 
Twitter Sentiment score of the required stock.
##### Example:
```bash
>>> from buzz import twitter_sentiment
>>> pprint(twitter_sentiment("AAPL"))
{'sentiment_score': 0.0, 'source_tweets': []}
```
#### Function: `fear_and_greed_index`
```bash
fear_and_greed_index()
```
##### Arguments:
NULL
##### Return value: 
Fear and Greed index of the market
##### Example:
```bash
>>> from buzz import fear_and_greed_index
>>> pprint(fear_and_greed_index())        
{   
    '1 Month Ago': {'label': 'Fear', 'score': '43'},
    '1 Week Ago': {'label': 'Extreme Fear', 'score': '25'},    
    '1 Year Ago': {'label': 'Greed', 'score': '64'},
    'Now': {'label': 'Fear', 'score': '30'},
    'Previous Close': {'label': 'Extreme Fear', 'score': '25'},
}
```
#### Function: `wallstreetbets_mentions`
```bash
wallstreetbets_mentions(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`
##### Return value: 
Wallstreetbets mentions of the required stocks required stock.
##### Example:
```bash
>>> from buzz import wallstreetbets_mentions
>>> pprint(wallstreetbets_mentions("AAPL"))
None
```
### Category: Economy
Key economic indicators.
#### Function: `risk_free_rate`
```bash
risk_free_rate()
```
##### Arguments:
None
##### Return value: 
Risk free rate of the market.
##### Example:
```bash
>>> from economy import risk_free_rate
>>> pprint(risk_free_rate())           
0.00043588067008681897
```
#### Function: `last_year_market_return`
```bash
last_year_market_return()
```
##### Arguments:
None
##### Return value:
Last year return of the market.
##### Example:
```bash
>>> from economy import last_year_market_return
>>> pprint(last_year_market_return()) 
0.369336438702895
```
### Category: Exchanges
Data about key stock market exchanges.
#### Function: `all_public_companies`
```bash
all_public_companies()
```
##### Arguments:
None
##### Return value:
Tickers of all public companies.
##### Example:
```bash
>>> from exchanges import all_public_companies
>>> pprint(all_public_companies())    
[    
    'WIX',
    'WIZD',
    'WIZS3',
    'WIZZ',
    'WJA',
    'WJG',
    'WJP',
    'WJX',
    'WK',
    'WKEY',
    'WKG',
    'WKHS',
    'WKL',
    'WKLY',
    ...
]
```
#### Function: `nasdaq_exchange_composition`
```bash
nasdaq_exchange_composition()
```
##### Arguments:
None
##### Return value:
Tickers of all stocks listed in Nasdaq exchange.
##### Example:
```bash
>>> from exchanges import nasdaq_exchange_composition
>>> pprint(nasdaq_exchange_composition())   
[
    'PPH',
    'PPSI',
    'PPTA',
    'PRAA',
    'PRAX',
    'PRCH',
    'PRDO',
    'PRFT',
    'PRFX',
    'PRFZ',
    'PRGS',
    ...
]
```
#### Function: `nyse_composition`
```bash
nyse_composition()
```
##### Arguments: 
None
##### Return value:
Tickers of all stocks listed in New York Stock Exchange.
##### Example:    
```bash
>>> from exchanges import nyse_composition
>>> pprint(nyse_composition())
[    
    'TPH',
    'TPL',
    'TPR',
    'TPVG',
    'TPX',
    'TR',
    'TREX',
    'TRGP',
    'TRI',
    'TRN',
    'TRNO',
    ...
]
```
#### Function: `shanghai_exchange_composition`
```bash
shanghai_exchange_composition()
```
##### Arguments:
None
##### Return value:
Tickers of all stocks listed in Shanghai Stock Exchange
##### Example:
```bash
>>> from exchanges import  shanghai_exchange_composition
>>> pprint(shanghai_exchange_composition()) 
[
    '000001',
    '000002',
    '000003',
    '000010',
    '000016',
    '000132',
    '000300',
    '000852',
    '000905',
    '000991',
    '510050',
    '510300',
    '510440',
    '510500',
    '510810',
    '512660',
    '512710',
    ...
]
```
#### Function: `hong_kong_exchange_composition`
```bash
hong_kong_exchange_composition()
```
##### Arguments:
None
##### Return value:
Tickers of all stocks listed in Hong Kong Stock Exchange
##### Example:
```bash
>>> from exchanges import hong_kong_exchange_composition
>>> pprint(hong_kong_exchange_composition())
[
    '0005',
    '0006',
    '0007',
    '0008',
    '0009',
    '0010',
    '0011',
    '0012',
    '0014',
    '0016',
    '0017',
    '0019',
    '0023',
    '0027',
    '0030',
    '0031',
    '0032',
    '0033',
    '0034',
    '0035',
    ...
]
```
#### Function: `london_exchange_composition`
```bash
london_exchange_composition()
```
##### Arguments:
None
##### Return value:
Tickers of all stocks listed in London Stock Exchange
##### Example:
```bash
>>> from exchanges import london_exchange_composition
>>> pprint(london_exchange_composition())
[
    'GWI',
    'GWMO',
    'GYM',
    'H50E',
    'HAYD',
    'HBR',
    'HCM',
    'HDIV',
    'HDLG',
    'HDLV',
    'HE1',
    'HEAD',
    'HEDF',
    'HEDG',
    'HEIQ',
    'HEMO',
    'HFD',
    'HFEL',
    'HGT',
    'HHI',
    'HHV',
    ...
]
```
### Category: Financials
Company financial statements data.
#### Function: `annual_balance_sheet`
```bash
annual_balance_sheet(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Annual balance sheet of recent years for the required stock
##### Example:
```bash
>>> from financials import annual_balance_sheet
>>> pprint(annual_balance_sheet("AAPL"))
{   
    '1506729600000': {
        'Accounts Payable': 44242000000.0,      
        'Cash': 20289000000.0,
        'Common Stock': 35867000000.0,
        'Inventory': 4855000000.0,
        'Long Term Debt': 97207000000.0,        
        'Long Term Investments': 194714000000.0,
        'Net Receivables': 35673000000.0,       
        'Net Tangible Assets': 134047000000.0,  
        'Other Assets': 18177000000.0,
        'Other Current Assets': 13936000000.0,
        'Other Current Liabilities': 38099000000.0,
        'Other Liabilities': 43251000000.0,
        'Other Stockholder Equity': -150000000.0,
        'Property Plant Equipment': 33783000000.0,
        'Retained Earnings': 98330000000.0,
        'Short Long Term Debt': 6496000000.0,
        'Short Term Investments': 53892000000.0,
        'Total Assets': 375319000000.0,
        'Total Current Assets': 128645000000.0,
        'Total Current Liabilities': 100814000000.0,
        'Total Liabilities': 241272000000.0,
        'Total Stockholder Equity': 134047000000.0,
        'Treasury Stock': -150000000.0,
    },
    ...
}
```
#### Function: `quarterly_balance_sheet`
```bash
quarterly_balance_sheet(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Quarterly balance sheet of recent quarters for the required stock
##### Example:
```bash
>>> from financials import quarterly_balance_sheet
>>> pprint(quarterly_balance_sheet("AAPL"))
{
    '1601078400000': {
        'Accounts Payable': 42296000000.0,
        'Cash': 38016000000.0,
        'Common Stock': 50779000000.0,
        'Inventory': 4061000000.0,
        'Long Term Debt': 98667000000.0,
        'Long Term Investments': 100887000000.0,
        'Net Receivables': 37445000000.0,
        'Net Tangible Assets': 65339000000.0,
        'Other Assets': 33952000000.0,
        'Other Current Assets': 11264000000.0,
        'Other Current Liabilities': 47867000000.0,
        'Other Liabilities': 46108000000.0,
        'Other Stockholder Equity': -406000000.0,
        'Property Plant Equipment': 45336000000.0,
        'Retained Earnings': 14966000000.0,
        'Short Long Term Debt': 8773000000.0,
        'Short Term Investments': 52927000000.0,
        'Total Assets': 323888000000.0,
        'Total Current Assets': 143713000000.0,
        'Total Current Liabilities': 105392000000.0,
        'Total Liabilities': 258549000000.0,
        'Total Stockholder Equity': 65339000000.0,
        'Treasury Stock': -406000000.0,
    },
    ...
}
```
#### Function: `latest_annual_balance_sheet`
```bash
latest_annual_balance_sheet(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Latest annual balance sheet of the required stock.
##### Example:
```bash
>>> from financials import latest_annual_balance_sheet
>>> pprint(latest_annual_balance_sheet("AAPL")) 
{
    'current_annual_balance_sheet': {
        'Accounts Payable': 42296000000.0,
        'Cash': 38016000000.0,
        'Common Stock': 50779000000.0,
        'Inventory': 4061000000.0,
        'Long Term Debt': 98667000000.0,
        'Long Term Investments': 100887000000.0,
        'Net Receivables': 37445000000.0,
        'Net Tangible Assets': 65339000000.0,
        'Other Assets': 33952000000.0,
        'Other Current Assets': 11264000000.0,
        'Other Current Liabilities': 47867000000.0,
        'Other Liabilities': 46108000000.0,
        'Other Stockholder Equity': -406000000.0,
        'Property Plant Equipment': 45336000000.0,
        'Retained Earnings': 14966000000.0,
        'Short Long Term Debt': 8773000000.0,
        'Short Term Investments': 52927000000.0,
        'Total Assets': 323888000000.0,
        'Total Current Assets': 143713000000.0,
        'Total Current Liabilities': 105392000000.0,
        'Total Liabilities': 258549000000.0,
        'Total Stockholder Equity': 65339000000.0,
        'Treasury Stock': -406000000.0,
    },
    'date': '2021-07-30T11:50:11.411845',
    'status': 'success',
}
```
#### Function: `latest_quarterly_balance_sheet`
```bash
latest_quarterly_balance_sheet(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Latest quarterly balance sheet of the required stock
##### Example:
```bash
>>> from financials import latest_quarterly_balance_sheet
>>> pprint(latest_quarterly_balance_sheet("AAPL")) 
{   
    'current_quarterly_balance_sheet': {
        'Accounts Payable': 40409000000.0,
        'Cash': 34050000000.0,
        'Common Stock': 54989000000.0,
        'Inventory': 5178000000.0,
        'Long Term Debt': 105752000000.0,
        'Long Term Investments': 131948000000.0,    
        'Net Receivables': 33908000000.0,
        'Net Tangible Assets': 64280000000.0,       
        'Other Assets': 44854000000.0,
        'Other Current Assets': 13641000000.0,      
        'Other Current Liabilities': 51306000000.0, 
        'Other Liabilities': 38354000000.0,
        'Other Stockholder Equity': 58000000.0,     
        'Property Plant Equipment': 38615000000.0,  
        'Retained Earnings': 9233000000.0,
        'Short Long Term Debt': 8039000000.0,       
        'Short Term Investments': 27646000000.0,    
        'Total Assets': 329840000000.0,
        'Total Current Assets': 114423000000.0,     
        'Total Current Liabilities': 107754000000.0,
        'Total Liabilities': 265560000000.0,        
        'Total Stockholder Equity': 64280000000.0,  
        'Treasury Stock': 58000000.0,
    },
    'date': '2021-07-30T12:10:59.002167',
    'status': 'success',
}
```
#### Funtion: 'annual_income_statement'
```bash
annual_income_statement(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Annual income statement of recent years for the required stock
##### Example:
```bash
>>> from financials import annual_income_statement       
>>> pprint(annual_income_statement("AAPL"))        
{   
    '1506729600000': {
        'Cost Of Revenue': 141048000000.0,
        'Discontinued Operations': 0.0,
        'EBIT': 61344000000.0,
        'Effect of Accounting Charges': 0.0,
        'Extraordinary Items': 0.0,
        'Gross Margin': 0.3846986049,
        'Gross Profit': 88186000000.0,
        'Income Before Tax': 64089000000.0,
        'Income Tax Expense': 15738000000.0,
        'Interest Expense': -2323000000.0,
        'Minority Interest': 0.0,
        'Net Income': 48351000000.0,
        'Net Income Applicable To Common Shares': 48351000000.0,
        'Net Income From Continuing Ops': 48351000000.0,
        'Net Margin': 0.2109242085,
        'Non Recurring': 0.0,
        'Operating Income': 61344000000.0,
        'Operating Margin': 0.2676042821,
        'Other Items': 0.0,
        'Other Operating Expenses': 0.0,
        'Research & Development': 11581000000.0,
        'Selling, General & Administrative': 15261000000.0,
        'Total Operating Expenses': 167890000000.0,
        'Total Other Income Expense Net': 2745000000.0,
        'Total Revenue': 229234000000.0,
    },
    ...
}
```
#### Function: `quarterly_income_statement`
```bash
quarterly_income_statement(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value: 
Quarterly income statement of recent years for the required stock
##### Example:
```bash
>>> from financials import quarterly_income_statement
>>> pprint(quarterly_income_statement("AAPL"))
{
    '1601078400000': {
        'Cost Of Revenue': 40009000000.0,
        'Discontinued Operations': 0.0,
        'EBIT': 14775000000.0,
        'Effect of Accounting Charges': 0.0,
        'Extraordinary Items': 0.0,
        'Gross Margin': 0.381603759,
        'Gross Profit': 24689000000.0,
        'Income Before Tax': 14901000000.0,
        'Income Tax Expense': 2228000000.0,
        'Interest Expense': -634000000.0,
        'Minority Interest': 0.0,
        'Net Income': 12673000000.0,
        'Net Income Applicable To Common Shares': 12673000000.0,
        'Net Income From Continuing Ops': 12673000000.0,
        'Net Margin': 0.1958793162,
        'Non Recurring': 0.0,
        'Operating Income': 14775000000.0,
        'Operating Margin': 0.2283687286,
        'Other Items': 0.0,
        'Other Operating Expenses': 0.0,
        'Research & Development': 4978000000.0,
        'Selling, General & Administrative': 4936000000.0,
        'Total Operating Expenses': 49923000000.0,
        'Total Other Income Expense Net': 126000000.0,
        'Total Revenue': 64698000000.0,
    },
    ...
}
```
#### Function: `latest_annual_income_statement`
```bash
latest_annual_income_statement(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Latest annual income statement for the required stock
##### Example:
```bash
>>> from financials import quarterly_income_statement
>>> pprint(latest_annual_income_statement("AAPL")) 
{
    'current_annual_income_statement': {
        'Cost Of Revenue': 169559000000.0,
        'Discontinued Operations': 0.0,
        'EBIT': 66288000000.0,
        'Effect of Accounting Charges': 0.0,
        'Extraordinary Items': 0.0,
        'Gross Margin': 0.38233247727810865,
        'Gross Profit': 104956000000.0,
        'Income Before Tax': 67091000000.0,
        'Income Tax Expense': 9680000000.0,
        'Interest Expense': -2873000000.0,
        'Minority Interest': 0.0,
        'Net Income': 57411000000.0,
        'Net Income Applicable To Common Shares': 57411000000.0,
        'Net Income From Continuing Ops': 57411000000.0,
        'Net Margin': 0.20913611278072236,
        'Non Recurring': 0.0,
        'Operating Income': 66288000000.0,
        'Operating Margin': 0.24147314354406862,
        'Other Items': 0.0,
        'Other Operating Expenses': 0.0,
        'Research & Development': 18752000000.0,
        'Selling, General & Administrative': 19916000000.0,
        'Total Operating Expenses': 208227000000.0,
        'Total Other Income Expense Net': 803000000.0,
        'Total Revenue': 274515000000.0,
    },
    'date': '2021-07-30T12:19:25.981871',
    'status': 'success',
}
```
#### Function: `latest_quarterly_income_statement`
```bash
latest_quarterly_income_statement(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Latest quarterly income statement for the required stock.
##### Example:
```bash
>>> from financials import latest_quarterly_income_statement
>>> pprint(latest_quarterly_income_statement("AAPL"))
{
    'current_quarterly_income_statement': {
        'Cost Of Revenue': 46179000000.0,
        'Discontinued Operations': 0.0,
        'EBIT': 24126000000.0,
        'Effect of Accounting Charges': 0.0,
        'Extraordinary Items': 0.0,
        'Gross Margin': 0.4329272785323084,
        'Gross Profit': 35255000000.0,
        'Income Before Tax': 24369000000.0,
        'Income Tax Expense': 2625000000.0,
        'Interest Expense': -665000000.0,
        'Minority Interest': 0.0,
        'Net Income': 21744000000.0,
        'Net Income Applicable To Common Shares': 21744000000.0,
        'Net Income From Continuing Ops': 21744000000.0,
        'Net Margin': 0.2670137780288332,
        'Non Recurring': 0.0,
        'Operating Income': 24126000000.0,
        'Operating Margin': 0.296264459562345,
        'Other Items': 0.0,
        'Other Operating Expenses': 0.0,
        'Research & Development': 5717000000.0,
        'Selling, General & Administrative': 5412000000.0,
        'Total Operating Expenses': 57308000000.0,
        'Total Other Income Expense Net': 243000000.0,
        'Total Revenue': 81434000000.0,
    },
    'date': '2021-07-30T12:21:29.676466',
    'status': 'success',
}
```
### Category: Screeners
Stocks listed on Yahoo Finance screeners here: https://finance.yahoo.com/screener/
#### Function: `conservative_foreign_funds`
```bash
conservative_foreign_funds()
```
##### Return value:
Tickers of all conservative foreign funds.
##### Example:
```bash
>>> from screeners import conservative_foreign_funds
>>> pprint(conservative_foreign_funds())
[   
    'RERBX',
    'RERCX',
    'RERGX',
    'AEPGX',
    'VTMNX',
    'VTMGX',
    'VDIPX',
    'VDVIX',
    'MGIAX',
    'MINRX',
    ...
]
```
#### Function: `most_actives`
```bash
most_actives()
```
##### Arguments: 
None
##### Return value:
Tickers of most active stocks.
##### Example:
```bash
>>> from screeners import most_actives              
>>> pprint(most_actives())               
[
    'AMD',
    'PINS',
    'F',
    'NIO',
    'AAPL',
    'AMC',
    'GE',
    'DIDI',
    'VALE',
    'TAL',
    'BAC',
    'ITUB',
    'CCL',
    ...
]
```
#### Function: `most_shorted_stocks`
```bash
most_shorted_stocks()
```
##### Arguments: 
None
##### Return value: 
Tickers of most shorted stocks.
##### Example:
```bash
>>> from screeners import most_shorted_stocks
>>> pprint(most_actives())
[
    'FNMAS',
    'SMFR',
    'LWLG',
    'ENLAY',
    'ALPAU',
    'MUDSW',
    'FFIE',
    'CYDY',
    'IMGO',
    'WFC-PC',
    'CLVT-PA',
    'RLYB',
    'CGXEF',
    'FNMAT',
    'OGZPY',
    'SGSVF',
    'ZTAQU',
    ...
]
```
#### Function: `undervalued_growth_stocks`
```bash
undervalued_growth_stocks()
```
##### Arguments: 
None
##### Return value:
Tickers of stocks having undervalued growth.
##### Example:
```bash
>>> from screeners import undervalued_growth_stocks
>>> pprint(undervalued_growth_stocks()) 
[
    'BAC',
    'VALE',
    'WFC',
    'NYCB',
    'C',
    'GM',
    'KGC',
    'SYF',
    'ET',
    'KEY',
    'UMC',
    'AXP',
    'VIAC',
    ...
]
```
#### Function: `growth_technology_stocks`
```bash
growth_technology_stocks()
```
##### Arguments: 
None
##### Return value:
List of tickers of stocks..
##### Example:
```bash
>>> from screeners import growth_technology_stocks 
>>> pprint(growth_technology_stocks())  
[
    'AMD',
    'AAPL',
    'NVDA',
    'MU',
    'YMM',
    'QCOM',
    'HPQ',
    'GLW',
    'AMAT',
    'DQ',
    'TXN',
    'APH',
    'LOGI',
    'ADI',
    ...
]
```
#### Function: `day_gainers`
```bash
day_gainers()
```
##### Arguments: 
None
##### Return value: 
List of tickers of stocks.
##### Example:
```bash
>>> from screeners import day_gainers             
>>> pprint(day_gainers())              
[
    'CFEIY',
    'TEAM',
    'SFOSF',
    'SIMO',
    'POWI',
    'VCYT',
    'DXCM',
    'CPRI',
    'XMTR',
    'RAFLF',
    'KLAC',
    'LI',
    'SHCR',
    'SPSC',
    'TRQ',
    ...
]
```
#### Function: `day_losers`
```bash
day_losers()
```
##### Arguments: 
None
##### Return value:
List of tickers of stocks.
##### Example:
```bash
>>> from screeners import day_losers 
>>> pprint(day_losers()) 
[
    'SAVA',
    'TBIO',
    'PINS',
    'BAP',
    'NEGG',
    'IGMS',
    'ZEN',
    'PHJMF',
    'WDH',
    'AMEH',
    'CHUC',
    'IFS',
    'UPWK',
    'NWL',
    'YMM',
    'ALPMY',
    ...
]
```
#### Function: `undervalued_large_caps`
```bash
undervalued_large_caps()
```
##### Arguments: 
None
##### Return value:
List of tickers of stocks.
##### Example:
```bash
>>> from screeners import undervalued_large_caps
>>> pprint(undervalued_large_caps()) 
[   
    'F',  
    'CLF',
    'PBR',
    'NLY',
    'FCX',
    'GM',
    'SYF',
    'ET',
    'HBAN',
    ...
]
```
#### Function: `aggresive_small_caps`
```bash
aggresive_small_caps()
```
##### Arguments: 
None
##### Return value:
List of tickers of stocks.
##### Example:
```bash
>>> from screeners import aggresive_small_caps 
>>> pprint(aggresive_small_caps())  
[
    'LC',
    'KNDI',
    'BTU',
    'BEST',
    'KOS',
    'CCO',
    'HUT',
    'SCR',
    'LLNW',
    'LX',
    'DNMR',
    ...
]
```
#### Function: `small_cap_gainers`
```bash
small_cap_gainers()
```
##### Arguments: 
None
##### Return value:
List of tickers of stocks.
##### Example:
```bash
>>> from screeners import small_cap_gainers   
>>> pprint(small_cap_gainers())    
[
    'LLNW',
    'APRN',
    'LHDX',
    'WTRH',
    'BCEL',
    'ASC',
    'HLIT',
    'CRNT',
    'FHS',
    'JBI',
    'DSP',
    ...
]
```
#### Function: `top_mutual_funds`
```bash
top_mutual_funds()
```
##### Arguments:
None
##### Return value:
List of tickers of top mutual funds.
##### Example:
```bash
>>> from screeners import top_mutual_funds
>>> pprint(top_mutual_funds())
[
    'RYLCX',
    'CYPSX',
    'ARYDX',
    'PTIAX',
    'BTTRX',
    'AIGYX',
    'AIAGX',
    'CYPIX',
    'SSIZX',
    'VAIPX',
    'CLDIX',
    'FCNKX',
    'WHOSX',
    'POLIX',
    'SGRHX',
    ...
]
```
#### Function: `portfolio_anchors`
```bash
portfolio_anchors()
```
##### Arguments: 
None
##### Return value:
List of tickers.
##### Example:
```bash
>>> from screeners import portfolio_anchors
>>> pprint(portfolio_anchors())
[
    'VSTSX',
    'VSMPX',
    'VTSMX',
    'VFFSX',
    'VFIAX',
    'VFINX',
    'FXAIX',
    'RFNBX',
    'RICHX',
    'RICEX',
    'CICFX',
    ...
]
```
#### Function: `solid_large_growth_funds`
```bash
solid_large_growth_funds()
```
##### Arguments: 
None
##### Return value:
List of tickers.
##### Example:
```bash
>>> from screeners import solid_large_growth_funds
>>> pprint(solid_large_growth_funds()) 
[
    'RGABX',
    'RGEBX',
    'RGAGX',
    'GFAFX',
    'RGAAX',
    'CGFFX',
    'FCNTX',
    'FCNKX',
    'VIGRX',
    'VPMAX',
    'VIGIX',
    'VIGAX',
    ...
]
```
#### Function: `solid_midcap_growth_funds`
```bash
solid_midcap_growth_funds()
```
##### Arguments: 
None
##### Return value:
List of tickers.
##### Example:
```bash
>> from screeners import solid_midcap_growth_funds
>>> pprint(solid_midcap_growth_funds()) 
[
    'RRMGX',
    'RPMGX',
    'JMGRX',
    'PMAQX',
    'PMBMX',
    'PMBSX',
    'PEMGX',
    'PMSBX',
    'JDMNX',
    'JDMAX',
    ...
]
```
#### Function: `high_yield_bonds`
```bash
high_yield_bonds()
```
##### Arguments: 
None
##### Return value:
List of tickers.
##### Example:
```bash
>>> from screeners import high_yield_bonds         
>>> pprint(high_yield_bonds())             
[
    'BHYSX',
    'BHYAX',
    'BRHYX',
    'MHHRX',
    'MHYRX',
    'MHCAX',
    'PRHIX',
    'PRHYX',
    'AGDRX',
    'AGDAX',
    ...
]
```
### Category: Search
Utilities for searching for stocks based on various dimensions.
#### Function: `wikipedia_url_to_ticker_symbol`
```bash
wikipedia_url_to_ticker_symbol(wikipedia_url)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
wikipedia_url | str | wikipedia url of the stock | False
##### Return value:
Ticker symbol.
##### Example:
```bash
>>> from search import wikipedia_url_to_ticker_symbol
>>> pprint(wikipedia_url_to_ticker_symbol("https://en.wikipedia.org/wiki/Apple_Inc."))
'AAPL'
```
#### Function: `isin_to_ticker_symbol`
```bash
isin_to_ticker_symbol(isin)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
isin | str | isin code | False
##### Return value:
Ticker symbol.
##### Example:
```bash
>>> from search import isin_to_ticker_symbol         
>>> pprint(isin_to_ticker_symbol("US0378331005"))
"AAPL"
```
#### Function: `company_name_to_ticker_symbol`
```bash
company_name_to_ticker_symbol(company_name)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
company_name | str | Name of the company | False
##### Return value:
Ticker symbol.
##### Example:
```bash   
>>> from search import company_name_to_ticker_symbol
>>> pprint(company_name_to_ticker_symbol("Apple"))
"AAPL"
```
### Category: Similarity
Similarity measures for pairs of stocks.
#### Function: `business_description_similarity`
```bash
business_description_similarity(ticker_symbol1,ticker_symbol2)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol1 | str | Ticker symbol | False
ticker_symbol2 | str | Ticker symbol | False
##### Return value:
Similarity score.
##### Example:
```bash   
>>> from similarity import business_description_similarity
>>> business_description_similarity("AAPL","GOOGL")
0.12793313483581853
```
#### Function: `industry_similarity`
```bash
industry_similarity(ticker_symbol1,ticker_symbol2)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol1 | str | Ticker symbol | False
ticker_symbol2 | str | Ticker symbol | False
##### Return value:
Similarity score.
##### Example:
```bash   
>>> from similarity import industry_similarity            
>>> pprint(industry_similarity("AAPL","GOOGL"))     
0.0
```
#### Function: `stock_price_correlation`
```bash
stock_price_correlation(ticker_symbol1,ticker_symbol2)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol1 | str | Ticker symbol | False
ticker_symbol2 | str | Ticker symbol | False
##### Return value:
Similarity score.
##### Example:
```bash   
>>> from similarity import stock_price_correlation
>>> pprint(stock_price_correlation("AAPL","GOOGL")) 
0.87
```
### Category: Stock
Data specific to individual stocks.
#### Function: `company_profile`
```bash
company_profile(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Company profile description.
##### Example:
```bash
>>> from stock import company_profile
>>> pprint(company_profile("AAPL"))
{
    'company_profile': {
        'City': 'Cupertino',
        'Company Name': 'Apple Inc.',
        'Country': 'United States',
        'Description': 'Apple Inc. designs, manufactures, and ---- Cupertino, California.',
        'Exchange': 'NasdaqGS',
        'Full Time Employees': 100000,
        'Industry': 'Consumer Electronics',
        'Sector': 'Technology',
        'Short Company Name': 'Apple Inc.',
        'State': 'CA',
        'Website': 'http://www.apple.com',
    },
    'date': '2021-07-31T10:12:24.849292',
    'status': 'success',
}
```
#### Function: `Quote`
```bash
quote(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Quote description.
##### Example:
```bash
>>> from stock import quote
>>> pprint(quote("AAPL"))           
{
    'date': '2021-07-31T10:14:45.973997',
    'quote': {
        '52-Week Change': -4.1399994,
        '52-Week High': 150.0,
        '52-Week Low': 103.1,
        'Company Name': 'Apple Inc.',
        'Current Price': 145.86,
        'Exchange': 'NasdaqGS',
        'Market Capitalization': 2411094867968.0,
        'Shares Outstanding': 16530199552.0,
        'Short Company Name': 'Apple Inc.',
        "Today's Change": 0.22000122,
        "Today's High": 146.33,
        "Today's Low": 144.1101,
        "Today's Open": 144.38,
        "Today's Volume": 64471899.0,
    },
    'status': 'success',
}
```
#### Function: `historical_prices`
```bash
historical_prices(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Historical prices of the required stock.
##### Example:
```bash
 {
    '1627516800000': {
        'Adj Close': 145.639999,
        'Close': 145.639999,
        'High': 146.550003,
        'Low': 144.580002,
        'Open': 144.690002,
        'Volume': 56699500.0,
    },
    '1627603200000': {
        'Adj Close': 145.860001,
        'Close': 145.860001,
        'High': 146.330002,
        'Low': 144.110001,
        'Open': 144.380005,
        'Volume': 70382000.0,
    },
    ...
}
```
#### Function: `key_stats`
```bash
key_stats(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Key stats of the company.
##### Example:
```bash
>>> from stock import key_stats  
>>> pprint(key_stats("AAPL")) 
{
    'date': '2021-07-31T10:19:45.254202',
    'key_statistics': {
        '% Held by Insiders': 0.0007000000000000001,
        '% Held by Institutions': 0.5854,
        '200-Day Moving Average': 131.27,
        '5 Year Average Dividend Yield': 1.32,
        '50-Day Moving Average': 139.9,
        '52 Week High': 150.0,
        '52 Week Low': 103.1,
        '52-Week Change': 0.3369,
        'Avg Vol (10 day)': 82340000.0,
        'Avg Vol (3 month)': 83750000.0,
        'Beta (5Y Monthly)': 1.21,
        'Book Value Per Share (mrq)': 3.88,
        'Current Ratio (mrq)': 1.06,
        'Diluted EPS (ttm)': 5.11,
        'Dividend Date': '2021-08-11T00:00:00',
        'EBITDA': 110930000000.0,
        ...
    },
    'status': 'success',
}
```
### Category: Valuation
Valuation metrics related to individual stocks.
#### Function: `cost_of_equity`
```bash
cost_of_equity(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
cost of equity of the required ticker.
##### Example:
```bash
>>> from valuation import cost_of_equity
>>> pprint(cost_of_equity("AAPL")) 
0.41513435907161994
```
#### Function: `enterprise_value`
```bash
enterprise_value(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Enterprise value of the required ticker.
##### Example:
```bash
>>> from valuation import enterprise_value
>>> pprint(enterprise_value("AAPL"))
2663567177344.0
```
#### Function: `historical_valuation_measures`
```bash
historical_valuation_measures(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Historical valuation measue of the required ticker.
##### Example:
```bash
>>> from valuation import historical_valuation_measures                
>>> pprint(historical_valuation_measures("AAPL")) 
{   
    '1593475200000': {
        'Enterprise Value': 1580000000000.0,     
        'Enterprise Value/EBITDA': 95.15,        
        'Enterprise Value/Revenue': 26.44,       
        'Forward P/E': 24.33,
        'Market Cap (intraday)': 1560000000000.0,
        'PEG Ratio (5 yr expected)': 2.02,       
        'Price/Book (mrq)': 19.93,
        'Price/Sales (ttm)': 6.12,
        'Trailing P/E': 28.52,
    },
    '1601424000000': {
        'Enterprise Value': 1990000000000.0,     
        'Enterprise Value/EBITDA': 108.89,       
        'Enterprise Value/Revenue': 30.69,       
        'Forward P/E': 30.12,
        'Market Cap (intraday)': 1970000000000.0,
        'PEG Ratio (5 yr expected)': 2.86,       
        'Price/Book (mrq)': 27.2,
        'Price/Sales (ttm)': 7.5,
        'Trailing P/E': 35.12,
    },
    ...
}
```
#### Function: `valuation_measures`
```bash
valuation_measures(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
ticker_symbol | str | Ticker of the stock | False
##### Return value:
Valuation measure of the required ticker.
##### Example:
```bash
>>> from valuation import valuation_measures
>>> pprint(valuation_measures("AAPL"))
{
    'Enterprise Value': 2470000000000.0,
    'Enterprise Value/EBITDA': 21.59,
    'Enterprise Value/Revenue': 7.12,
    'Forward P/E': 26.18,
    'Market Cap (intraday)': 2410000000000.0,
    'PEG Ratio (5 yr expected)': 2.0,
    'Price/Book (mrq)': 37.51,
    'Price/Sales (ttm)': 7.15,
    'Trailing P/E': 28.49,
}
```
### Category: Yahoo_finance
Raw data directly from Yahoo Finance.
#### Function: `raw_quote`
```bash
raw_quote(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Details for the required stock.
##### Example:
```bash
>>> from yahoo_finance import raw_quote
>>> pprint(raw_quote("AAPL"))
{
    'currency': 'USD',
    'exchange': 'NMS',
    'exchangeDataDelayedBy': 0,
    'exchangeTimezoneName': 'America/New_York',
    'exchangeTimezoneShortName': 'EDT',
    'fiftyTwoWeekHigh': {'fmt': '150.00', 'raw': 150},
    'fiftyTwoWeekHighChange': {'fmt': '-4.41', 'raw': -4.407501},
    'fiftyTwoWeekHighChangePercent': {'fmt': '-2.94%', 'raw': -0.02938334},
    'fiftyTwoWeekLow': {'fmt': '103.10', 'raw': 103.1},
    'fiftyTwoWeekLowChange': {'fmt': '42.49', 'raw': 42.4925},
    'fiftyTwoWeekLowChangePercent': {'fmt': '41.21%', 'raw': 0.41214842},
    'fiftyTwoWeekRange': {'fmt': '103.10 - 150.00', 'raw': '103.1 - 150.0'},
    'firstTradeDateMilliseconds': 345479400000,
    'fullExchangeName': 'NasdaqGS',
    ...
}
```
#### Function: `raw_historical_prices`
```bash
raw_historical_prices(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Historical prices for the required stock.
##### Example:
```bash
>>> from yahoo_finance import raw_historical_prices
>>> pprint(raw_historical_prices("AAPL"))
{        
        {
            'Adj Close': 148.479996,
            'Close': 148.479996,
            'High': 150.0,
            'Low': 147.089996,
            'Open': 149.240005,
            'Volume': 106820300.0,
        },
        {
            'Adj Close': 146.389999,
            'Close': 146.389999,
            'High': 149.759995,
            'Low': 145.880005,
            'Open': 148.460007,
            'Volume': 93100300.0,
        },
        ...
}        
```
#### Function: `technical_insights`
```bash
technical_insights(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Technical insights of the required stocks
##### Example:
```bash
>>> from yahoo_finance import technical_insights
>>> pprint(technical_insights("AAPL")) 
{
    'companySnapshot': {
        'company': {
            'dividends': 0.1815,
            'earningsReports': 0.7988,
            'hiring': 0.9534,
            'innovativeness': 0.9983,
            'insiderSentiments': 0.439,
            'sustainability': 0.43329999999999996,
        },
        'sector': {
            'dividends': 0.5,
            'earningsReports': 0.5,
            'hiring': 0.5,
            'innovativeness': 0.5,
            'insiderSentiments': 0.5,
            'sustainability': 0.5,
        },
        ...
}
```

#### Function: `options_contracts`
```bash
options_contracts(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Options contracts of the required stock..
##### Example:
```bash
>>> from yahoo_finance import options_contracts
>>> pprint(options_contracts("AAPL"))
{
            {
                'ask': {'fmt': '0.00', 'raw': 0},
                'bid': {'fmt': '0.00', 'raw': 0},
                'change': {'fmt': '0.00', 'raw': 0},
                'contractSize': 'REGULAR',
                'contractSymbol': 'AAPL210917P00225000',
                'currency': 'USD',
                'expiration': {
                    'fmt': '2021-09-17',
                    'longFmt': '2021-09-17T00:00',
                    'raw': 1631836800,
                },
                'impliedVolatility': {
                    'fmt': '0.00%',
                    'raw': 1.0000000000000003e-05,
                },
                'inTheMoney': True,
                'lastPrice': {'fmt': '106.69', 'raw': 106.69},
                'lastTradeDate': {
                    'fmt': '2020-10-12',
                    'longFmt': '2020-10-12T14:01',
                    'raw': 1602511264,
                },
                'openInterest': {'fmt': '0', 'longFmt': '0', 'raw': 0},
                'percentChange': {'fmt': '0.00%', 'raw': 0},
                'strike': {'fmt': '225.00', 'raw': 225},
                'volume': {'fmt': '12', 'longFmt': '12', 'raw': 12},
            },
            ...
}
```
#### Function: `price`
```bash
price(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Return price of the required stock.
##### Example:
```bash
>>> from yahoo_finance import price            
>>> pprint(price("AAPL"))             
{
    'averageDailyVolume10Day': {
        'fmt': '82.45M',
        'longFmt': '82,452,133',
        'raw': 82452133,
    },
    'averageDailyVolume3Month': {
        'fmt': '83.13M',
        'longFmt': '83,130,919',
        'raw': 83130919,
    },
    ...
}
```
#### Function: `summary_detail`
```bash
summary_detail(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Summary of the required stock.
##### Example:
```bash
>>> from yahoo_finance import summary_detail
>>> pprint(summary_detail("AAPL")) 
{
    'algorithm': None,
    'ask': {'fmt': '145.59', 'raw': 145.59},
    'askSize': {'fmt': '1.2k', 'longFmt': '1,200', 'raw': 1200},
    'averageDailyVolume10Day': {
        'fmt': '82.45M',
        'longFmt': '82,452,133',
        'raw': 82452133,
    },
    'averageVolume': {
        'fmt': '83.13M',
        'longFmt': '83,130,919',
        'raw': 83130919,
    },
    ...
}
```
#### Function: `key_statistics`
```bash
key_statistics(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Statistics of the required stock.
##### Example:
```bash
>>> from yahoo_finance import key_statistics
>>> pprint(key_statistics("AAPL")) 
{
    '52WeekChange': {'fmt': '33.89%', 'raw': 0.33893287},
    'SandP52WeekChange': {'fmt': '33.41%', 'raw': 0.33407593},
    'annualHoldingsTurnover': {},
    'annualReportExpenseRatio': {},
    'beta': {'fmt': '1.21', 'raw': 1.20729},
    'beta3Year': {},
    'bookValue': {'fmt': '3.88', 'raw': 3.882},
    'category': None,
    'dateShortInterest': {'fmt': '2021-07-15', 'raw': 1626307200},
    'earningsQuarterlyGrowth': {'fmt': '93.20%', 'raw': 0.932},
    'enterpriseToEbitda': {'fmt': '22.40', 'raw': 22.399},
    'enterpriseToRevenue': {'fmt': '7.16', 'raw': 7.158},
    ...
}
```
#### Function: `company_profile`
```bash
company_profile(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Company profile of the required stock.
##### Example:
```bash
>> from yahoo_finance import company_profile
>>> pprint(company_profile("AAPL")) 
{
    'address1': 'One Apple Park Way',
    'city': 'Cupertino',
    'companyOfficers': [],
    'country': 'United States',
    'fullTimeEmployees': 100000,
    'industry': 'Consumer Electronics',
    ...
}
```
#### Function: `earnings`
```bash
earnings(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Earnings of the required stock.
##### Example:
```bash
>>> from yahoo_finance import earnings       
>>> pprint(earnings("AAPL"))           
{   
    'earningsChart': {
        'currentQuarterEstimate': {'fmt': '0.99', 'raw': 0.99},
        'currentQuarterEstimateDate': '2Q',
        'currentQuarterEstimateYear': 2021,
        'earningsDate': [
            {'fmt': '2021-10-27', 'raw': 1635292800},
            {'fmt': '2021-11-01', 'raw': 1635724800},
        ],
        'quarterly': [
            {
                'actual': {'fmt': '0.64', 'raw': 0.64},        
                'date': '2Q2020',
                'estimate': {'fmt': '0.51', 'raw': 0.51},      
            },
            ...
}
```
#### Function: `financial_data`
```bash
financial_data(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Financial data of the required stock.
##### Example:
```bash
>>> from yahoo_finance import financial_data
>>> pprint(financial_data("AAPL")) 
{
    'currentPrice': {'fmt': '145.52', 'raw': 145.52},
    'currentRatio': {'fmt': '1.06', 'raw': 1.062},
    'debtToEquity': {'fmt': '210.78', 'raw': 210.782},
    'earningsGrowth': {'fmt': '100.00%', 'raw': 1},
    'ebitda': {
        'fmt': '110.93B',
        'longFmt': '110,934,999,040',
        'raw': 110934999040,
    },
    'ebitdaMargins': {'fmt': '31.96%', 'raw': 0.31955},
    'financialCurrency': 'USD',
    'freeCashflow': {
        'fmt': '80.63B',
        'longFmt': '80,625,876,992',
        'raw': 80625876992,
    },
    ...
}
```
#### Function: `upgrade_downgrade_history`
```bash
upgrade_downgrade_history(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Upgrade downgrade history of the required stock.
##### Example:
```bash
>>> from yahoo_finance import upgrade_downgrade_history
>>> pprint(financial_data("AAPL"))
{        
        {
            'action': 'down',
            'epochGradeDate': 1359040136,
            'firm': 'Hilliard Lyons',
            'fromGrade': 'Buy',
            'toGrade': 'Long-term Buy',
        },
        {
            'action': 'main',
            'epochGradeDate': 1359024467,
            'firm': 'BGC Financial',
            'fromGrade': '',
            'toGrade': 'Hold',
        },
        ...
}
```
#### Function: `esg_scores`
```bash
esg_scores(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
ESG score of the required stock.
##### Example:
```bash
>>> from yahoo_finance import esg_scores    
>>> pprint(esg_scores("AAPL"))                
{
    'adult': False,
    'alcoholic': False,
    'animalTesting': False,
    'catholic': False,
    'coal': False,
    'controversialWeapons': False,
    'environmentPercentile': None,
    'environmentScore': {'fmt': '0.3', 'raw': 0.29},
    'esgPerformance': 'UNDER_PERF',
    'furLeather': False,
    ...
}
```
#### Function: `calendar_events`
```bash
calendar_events(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Events details of the required stock.
##### Example:
```bash
>>> from yahoo_finance import esg_scores    
>>> pprint(esg_scores("AAPL"))                
{
    'adult': False,
    'alcoholic': False,
    'animalTesting': False,
    'catholic': False,
    'coal': False,
    'controversialWeapons': False,
    'environmentPercentile': None,
    'environmentScore': {'fmt': '0.3', 'raw': 0.29},
    'esgPerformance': 'UNDER_PERF',
    'furLeather': False,
    'gambling': False,
    ...
}
```
#### Function: `annual_income_statement`
```bash
annual_income_statement(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Annual income statement of the required stock.
##### Example:
```bash
>>> from yahoo_finance import annual_income_statement
>>> pprint(annual_income_statement("AAPL")) 
[
    {
        'costOfRevenue': {
            'fmt': '169.56B',
            'longFmt': '169,559,000,000',
            'raw': 169559000000,
        },
        'discontinuedOperations': {},
        'ebit': {
            'fmt': '66.29B',
            'longFmt': '66,288,000,000',
            'raw': 66288000000,
        },
        'effectOfAccountingCharges': {},
        ...
]
```
#### Function: `quarterly_income_statement`
```bash
quarterly_income_statement(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Quarterly income statement of the required stock.
##### Example:
```bash
>>> from yahoo_finance import quarterly_income_statement
>>> pprint(quarterly_income_statement("AAPL")) 
[
    {
        'costOfRevenue': {
            'fmt': '46.18B',
            'longFmt': '46,179,000,000',
            'raw': 46179000000,
        },
        'discontinuedOperations': {},
        'ebit': {
            'fmt': '24.13B',
            'longFmt': '24,126,000,000',
            'raw': 24126000000,
        },
        'effectOfAccountingCharges': {},
        ...
]
```
#### Function: `annual_balance_sheet`
```bash
annual_balance_sheet(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Annual balance sheet of the required stock.
##### Example:
```bash
>>> from yahoo_finance import annual_balance_sheet      
>>> pprint(annual_balance_sheet("AAPL"))           
[
    {
        'accountsPayable': {
            'fmt': '42.3B',
            'longFmt': '42,296,000,000',
            'raw': 42296000000,
        },
        'cash': {
            'fmt': '38.02B',
            'longFmt': '38,016,000,000',
            'raw': 38016000000,
        },
        'commonStock': {
            'fmt': '50.78B',
            'longFmt': '50,779,000,000',
            'raw': 50779000000,
        },
        ...
]
```
#### Function: `quarterly_balance_sheet`
```bash
quarterly_balance_sheet(ticker_symbol)
```
##### Arguments:
Name | Type | Description | Optional | Default Vaue
--- | --- | --- | --- |---
`ticker_symbol` | `str` | Ticker of the stock | `False`

##### Return value:
Quarterly balance sheet of the required stock.
##### Example:
```bash
>>> from yahoo_finance import quarterly_balance_sheet
>>> pprint(quarterly_balance_sheet("AAPL")) 
[
    {
        'accountsPayable': {
            'fmt': '40.41B',
            'longFmt': '40,409,000,000',
            'raw': 40409000000,
        },
        'cash': {
            'fmt': '34.05B',
            'longFmt': '34,050,000,000',
            'raw': 34050000000,
        },
        'commonStock': {
            'fmt': '54.99B',
            'longFmt': '54,989,000,000',
            'raw': 54989000000,
        },
        ...
]
```
### Category: Indices
Data about key stock market indices.
#### Function: `s_and_p_composition`
```bash
s_and_p_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import s_and_p_composition          
>>> pprint(s_and_p_composition())            
[
    'A',
    'AAL',
    'AAP',
    'AAPL',
    'ABBV',
    'ABC',
    'ABMD',
    'ABT',
    'ACN',
    'ADBE',
    'ADI',
    'ADM',
    'ADP',
    'ADSK',
    'AEE',
    'AEP',
    'AES',
    'AFL',
    'AIG',
    'AIZ',
    'AJG',
    'AKAM',
    'ALB',
    'ALGN',
    'ALK',
    'ALL',
    'ALLE',
    'AMAT',
    'AMCR',
    ...
 ]   
```
#### Function: `nasdaq_composition`
```bash
nasdaq_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import nasdaq_composition 
>>> pprint(nasdaq_composition())  
[
    'AAPL',
    'ADBE',
    'ADI',
    'ADP',
    'ADSK',
    'AEP',
    'ALGN',
    'AMAT',
    'AMD',
    'AMGN',
    'AMZN',
    'ANSS',
    'ASML',
    'ATVI',
    'AVGO',
    'BIDU',
    'BIIB',
    ...
]
```
#### Function: `russel_one_thousand_composition`
```bash
russel_one_thousand_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import russel_one_thousand_composition
>>> pprint(russel_one_thousand_composition()) 
[   
    'A',   
    'AA',  
    'AAL', 
    'AAP', 
    'AAPL',
    'ABBV',
    'ABC', 
    'ABMD',
    'ABT',
    'ACC',
    'ACGL',
    'ACHC',
    'ACM',
    'ACN',
    'ADBE',
    'ADI',
    'ADM',
    'ADNT',
    'ADP',
    'ADS',
    ...
]
```
#### Function: `amex_oil_composition`
```bash
amex_oil_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import amex_oil_composition
>>> pprint(amex_oil_composition())            
[
    'BP',
    'COP',
    'CVX',
    'EC',
    'EQNR',
    'HES',
    'MPC',
    'MRO',
    'OXY',
    'PBR',
    'PSX',
    ...
]
```
#### Function: `djia_composition`
```bash
djia_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import djia_composition    
>>> pprint(djia_composition())            
[
    'AAPL',
    'AMGN',
    'AXP',
    'BA',
    'CAT',
    'CRM',
    'CSCO',
    'CVX',
    'DIS',
    'DOW',
    'GS',
    ...
]
```
#### Function: `bbc_global_composition`
```bash
bbc_global_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import bbc_global_composition
>>> pprint(bbc_global_composition()) 
[
    '2',
    '4502',
    '6954',
    '7203',
    '7751',
    '9437',
    'AAPL',
    'BAS',
    'BHP',
    'BRK.B',
    'CBA',
    'DD',
    'ENGI',
    ...
]
```
#### Function: `ibovespa_composition`
```bash
ibovespa_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import ibovespa_composition  
>>> pprint(ibovespa_composition())   
[
    'ABEV3',
    'AZUL4',
    'B3SA3',
    'BBAS3',
    'BBDC3',
    'BBDC4',
    'BBSE3',
    'BEEF3',
    'CSAN3',
    'CSNA3',
    'CVCB3',
    ...
]
```
#### Function: `ftse100_composition`
```bash
ftse100_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import ftse100_composition 
>>> pprint(ftse100_composition())  
[
    'AAL',
    'ABDN',
    'ABF',
    'ADM',
    'AHT',
    'ANTO',
    'AUTO',
    'AV.',
    'AVST',
    'AVV',
    'AZN',
    'BA.',
    'BARC',
    'BATS',
    'BDEV',
    'BHP',
    ...
]
```
#### Function: `ftse250_composition`
```bash
ftse250_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import ftse250_composition
>>> pprint(ftse250_composition()) 
[   
    '3IN', 
    '888', 
    'AAF', 
    'AGK', 
    'AGR', 
    'AGT', 
    'AJB', 
    'AML', 
    'AO.', 
    'APAX',
    'ASCL',
    'ASHM',
    'ASL', 
    'ATG', 
    'ATST',
    'ATT', 
    ...
]
```
#### Function: `nifty_fifty_composition`
```bash
nifty_fifty_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import nifty_fifty_composition
>>> pprint(nifty_fifty_composition()) 
[
    'BAJAJ-AUTO.NS',
    'BAJAJFINSV.NS',
    'BAJFINANCE.NS',
    'BHARTIARTL.NS',
    'BRITANNIA.NS',
    'CIPLA.NS',
    'COALINDIA.NS',
    'GRASIM.NS',
    'HDFCLIFE.NS',
    'HEROMOTOCO.NS',
    'HINDALCO.NS',
    ...
]
```
#### Function: `djgt_fifty_composition`
```bash
djgt_fifty_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import djgt_fifty_composition 
>>> pprint(djgt_fifty_composition())  
[
    '7203',
    'AAPL',
    'ABBV',
    'ABI',
    'ALV',
    'AMGN',
    'AMZN',
    'BA',
    'BATS',
    'BHP',
    'BP',
    'C',
    'CSCO',
    'CVX',
    ...
]
```
#### Function: `dax_thirty_composition`
```bash
dax_thirty_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import dax_thirty_composition
>>> pprint(dax_thirty_composition()) 
[
    '1COV.DE',
    'ADS.DE',
    'ALV.DE',
    'BAS.DE',
    'BAYN.DE',
    'BMW.DE',
    'CON.DE',
    'DAI.DE',
    'DB1.DE',
    'DBK.DE',
    'DHER.DE',
    'DPW.DE',
    'DTE.DE',
    'DWNI.DE',
    'ENR.DE',
    ...
]
```
#### Function: `euro100_composition`
```bash
euro100_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import euro100_composition   
>>> pprint(euro100_composition())    
[
    'AC',
    'AGN',
    'ADP',
    'AGS',
    'AIR',
    'AI',
    'AKZA',
    'ABI',
    'AKE',
    'ASML',
    'ATO',
    'CS',
    'BB',
    ...
]
```
#### Function: `djta_composition`
```bash
djta_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import djta_composition   
>>> pprint(djta_composition())    
[   
    'AAL', 
    'ALK', 
    'CAR', 
    'CHRW',
    'CSX', 
    'DAL', 
    'EXPD',
    'FDX',
    'JBHT',
    'JBLU',
    'KEX',
    ...
]
```
#### Function: `djua_composition`
```bash
djua_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import djua_composition
>>> pprint(djua_composition()) 
[
    'AEP',
    'AES',
    'ATO',
    'AWK',
    'D',
    'DUK',
    'ED',
    'EIX',
    'EXC',
    'FE',
    'NEE',
    'PEG',
    'SO',
    'SRE',
    'XEL',
]
```
#### Function: `nasdaq100_composition`
```bash
nasdaq100_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import nasdaq100_composition
>>> pprint(nasdaq100_composition()) 
[
    'AAPL',
    'ADBE',
    'ADI',
    'ADP',
    'ADSK',
    'AEP',
    'ALGN',
    'AMAT',
    'AMD',
    'AMGN',
    'AMZN',
    'ANSS',
    ...
]
```
#### Function: `phlx_semi_composition`
```bash
phlx_semi_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import phlx_semi_composition
>>> pprint(phlx_semi_composition()) 
[
    'ASML',
    'AMD',
    'ADI',
    'AMAT',
    'AVGO',
    'BRKS',
    'CCMP',
    'CREE',
    'ENTG',
    'IPHI',
    'INTC',
    ...
]
```
#### Function: `phlx_gold_composition`
```bash
phlx_gold_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import phlx_gold_composition
>>> pprint(phlx_gold_composition()) 
[
    'ABXXF',
    'AEM',
    'AOD.HA',
    'AUQNYSE',
    'BAAPX',
    'BVN',
    'CDER',
    'EDGA.SG',
    'ELDNYSE',
    'FCXS',
    'FR',
    ...
]
```
#### Function: `nikkei225_composition`
```bash
nikkei225_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import nikkei225_composition
>>> pprint(nikkei225_composition()) 
[
    '1332',
    '1333',
    '1605',
    '1721',
    '1925',
    '1808',
    '1963',
    '1812',
    '1802',
    '1928',
    '1803',
    '1801',
    ...
]
```
#### Function: `omx_nordic_composition`
```bash
omx_nordic_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import omx_nordic_composition
>>> pprint(omx_nordic_composition()) 
[
    'ABB',
    'AMBU',
    'ASSA B',
    'ATCO A',
    'ATCO B',
    'AZN',
    'CARL B',
    'CHR',
    'COLO B',
    'DANSKE',
    'DSV',
    'ELISA',
    ...
]
```
#### Function: `nyse_arca_composition`
```bash
nyse_arca_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices  import nyse_arca_composition 
>>> pprint(nyse_arca_composition())  
[
    'AXP',
    'BA',
    'CVX',
    'DD',
    'DIS',
    ...
]
```
#### Function: `s_and_p_100`
```bash
s_and_p_100()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices import s_and_p_100
>>> pprint(s_and_p_100())
[
    'AAPL',
    'ABBV',
    'ABT',
    'ACN',
    'ADBE',
    'AIG',
    'AMGN',
    'AMT',
    ...
]
```
#### Function: `s_and_p_global_100`
```bash
s_and_p_global_100()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices import s_and_p_global_100
>>> pprint(s_and_p_global_100())
[
    'MMM',
    'ABT',
    'AGN',
    'ALV',
    'AAL',
    'G',
    'AZN',
    ...
]
```
#### Function: `russel_2000_composition`
```bash
russel_2000_composition()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices import russel_2000_composition
>>> pprint(russel_2000_composition())
['ACRX', 'ADTN', 'DNLI', 'DORM', 'ESTE', 'EVER', 'FULT', 'TLYS', 'WK']
```
#### Function: `niftybank`
```bash
niftybank()
```
##### Arguments:
None
##### Return value:
List of tickers of the stocks in the required index.
##### Example:
```bash
>>> from indices import niftybank
>>> pprint(niftybank())
[
    'AXISBANK',
    'BANDHANBNK',
    'BANKBARODA',
    'FEDERALBNK',
    'HDFCBANK',
    'ICICIBANK',
    ...
]
```
