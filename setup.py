import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lattice-stocks-data",
    version="1.0.1",

    description="A simple interface for pulling stock market data through the Lattice Stock Market Data API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://lattice.dev/",
    project_urls={
        "Source": "https://github.com/LatticeData/lattice-stocks-data",
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
