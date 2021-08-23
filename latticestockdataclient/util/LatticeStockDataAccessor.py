import os
import json
import logging
import requests
import settings
import pandas as pd
from io import StringIO
from latticestockdataclient.util.LatticeStockDataPayloadFactory import LatticeStockDataPayloadFactory


class LatticeStockDataAccessor:
    def __init__(self, host=None, key=None, payloadfactory=None):
        self.host=host or os.environ["STOCK_DATA_X_RAPID_API_HOST"]
        self.key=key or os.environ["STOCK_DATA_X_RAPID_API_KEY"]
        self.payloadfactory=payloadfactory or \
                LatticeStockDataPayloadFactory(self.host, self.key)

    def get(self, endpoint, params=None):
        if not params: params = {}
        return requests.get(self.payloadfactory.url(endpoint),      \
                    headers=self.payloadfactory.headers, params=params).text

    def get_json(self, endpoint, params=None):
        return json.loads(self.get(endpoint, params=params))

    def get_df(self, endpoint, params=None):
        params["format"] = "csv"
        return pd.read_csv(StringIO(self.get(endpoint, params=params)),\
                                            index_col=0, parse_dates=True)
