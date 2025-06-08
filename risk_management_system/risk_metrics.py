# risk_metrics.py

import numpy as np

def historical_var(returns, confidence_level=0.95):
    """
    Historical Value at Risk (VaR) at given confidence level.
    """
    if isinstance(returns, np.ndarray):
        data = returns
    else:
        data = returns.values
    return -np.percentile(data, (1 - confidence_level) * 100)

def parametric_var(returns, confidence_level=0.95):
    """
    Parametric (Gaussian) Value at Risk (VaR)
    """
    mean = np.mean(returns)
    std = np.std(returns)
    from scipy.stats import norm
    z = norm.ppf(1 - confidence_level)
    return -(mean + z * std)

def conditional_var(returns, confidence_level=0.95):
    """
    Conditional Value at Risk (CVaR): Expected shortfall beyond VaR
    """
    if isinstance(returns, np.ndarray):
        data = returns
    else:
        data = returns.values
    var_threshold = np.percentile(data, (1 - confidence_level) * 100)
    return -data[data <= var_threshold].mean()

def max_drawdown(price_series):
    """
    Compute the maximum drawdown from a price series
    """
    cumulative = price_series / price_series.iloc[0]
    rolling_max = cumulative.cummax()
    drawdown = (cumulative - rolling_max) / rolling_max
    return drawdown.min()
