import setuptools

setuptools.setup(
    name="lattice-stocks-data",
    version="1.0.21",

    description="An API for gathering RapidAPI stock info",
    long_description=" An easy-to-use library for quick access to stock market information. Complete stock market data is available from Yahoo Finance and many other sources in one convenient package. To successfully use this library you will need an API key for the Lattice Stock Market Data API that powers it. Navigate to RapidAPI to sign up for a free API key and then save it to an environment variable called STOCK_DATA_X_RAPID_API_KEY in your environment. The library will automatically load that environment variable and use it to authenticate API calls made under the hood.",
    long_description_content_type="text/markdown",
    url="https://lattice.dev/products/stock-market-data",
    project_urls={
        "Source": "https://github.com/LatticeData/lattice-stocks-data",
        "Documentation" : "https://github.com/LatticeData/lattice-stocks-data/blob/master/README.md#Usage",
        "Bug Reports" : "https://github.com/LatticeData/lattice-stocks-data/issues",
        "Get your key" : "https://rapidapi.com/lattice-data-lattice-data-default/api/stock-market-data/",


    },
    py_modules = ["algorithms","buzz","economy","exchanges","financials","indices","market","screeners","search","similarity",
                    "stock","valuation","yahoo_finance"],
    
    author="ashkon@lattice.dev",
    package_dir={
        "": "./stocksdata",
    },
    
    tests_require=['pytest'],

    python_requires=">=3.7",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
