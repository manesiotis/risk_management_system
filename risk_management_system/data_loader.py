# data_loader.py

import yfinance as yf
import pandas as pd
import numpy as np
def load_price_data(tickers, start_date, end_date):
    """
    Load historical close prices for given tickers
    """
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False)['Close']
    data = data.dropna()
    return data

def calculate_returns(price_data, log_returns=False):
    """
    Calculate daily returns (log or simple)
    """
    if log_returns:
        returns = pd.DataFrame(np.log(price_data / price_data.shift(1)))
    else:
        returns = price_data.pct_change()
    return returns.dropna()
