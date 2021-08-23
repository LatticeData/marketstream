import setuptools

setuptools.setup(
    name="LatticeStockDataClient",
    version="0.0.20",

    description="An API for gathering RapidAPI stock info",
    py_modules = ["algorithms","buzz","economy","exchanges","financials","indices","market","screeners","search","similarity",
                    "stock","valuation","yahoo_finance"],
    
    author="ashkon@lattice.dev",
    package_dir={
        "": "./latticestockdataclient",
    },
    
    tests_require=['pytest'],

    python_requires=">=3.7",

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
