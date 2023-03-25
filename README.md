# Benjamin Graham Stock Valuation Calculator

---
## Introduction
This is a Python script that calculates the intrinsic value of a stock based on the Benjamin Graham formula. It takes in various input parameters such as the stock ticker, zero growth PE ratio, growth multiplier, and safety margin, and scrapes data from Yahoo Finance and FRED to calculate the intrinsic value.

## Getting Started
To run the script, you will need to install the following Python libraries:
- Streamlit
- yahoo_fin
- pandas_datareader

Once you have installed the libraries, simply run the script in your Python environment or you can requirements.txt file to install all the required libraries:

`python3 -m pip install -r requirements.txt`

Once you have installed the required libraries, you can run the script using the following command:

`streamlit run benjamin_graham_valuation.py`

## Data
The script scrapes the following data:

- Stock price and EPS from Yahoo Finance using 

`yahoo_fin.stock_info.get_quote_table()`
- Growth estimate from Yahoo Finance using 

`yahoo_fin.stock_info.get_analysts_info()`
- Latest current yield of the AAA Corporate Bond from FRED using 

`pandas_datareader.get_data_fred()`
## Conclusion
This script provides a simple way to calculate the intrinsic value of a stock based on the Benjamin Graham formula. It is a useful tool for investors looking to make informed investment decisions based on fundamental analysis.
