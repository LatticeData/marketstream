import setuptools

setuptools.setup(
    name="LatticeStockDataClient",
    version="0.0.18",

    description="An API for gathering RapidAPI stock info",
    py_modules = ["algorithms","buzz","economy","exchanges","financials","indices","market","screeners","search","similarity",
                    "stock","valuation","yahoo_finance"],
    package_dir={
        "": "./latticestockdataclient",

    },
)