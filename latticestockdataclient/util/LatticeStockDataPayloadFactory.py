import os
import logging


class LatticeStockDataPayloadFactory:
    def __init__(self, host=None, key=None):
        self.x_rapidapi_host=host or os.environ["STOCK_DATA_X_RAPID_API_HOST"]
        self.x_rapidapi_key=key or os.environ["STOCK_DATA_X_RAPID_API_KEY"]
        self._url=None

    def url(self, endpoint):
        self._url = "https://%s/%s" % (self.x_rapidapi_host.rstrip("/"), endpoint.lstrip("/"))
        return self._url

    @property
    def headers(self):
        headers = {
            'x-rapidapi-key': self.x_rapidapi_key,
            'x-rapidapi-host': self.x_rapidapi_host
        }
        return headers
