# run_risk_analysis.py

import numpy as np
from data_loader import load_price_data, calculate_returns
from risk_metrics import (
    historical_var,
    parametric_var,
    conditional_var,
    max_drawdown
)
from plotting import plot_drawdown
import warnings
warnings.filterwarnings("ignore")

# === 1. Parameters ===
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-12-31'
confidence_level = 0.95
log_returns = True

# === 2. Load data ===
prices = load_price_data([ticker], start_date, end_date)
price_series = prices[ticker]
returns = calculate_returns(prices, log_returns=log_returns)
return_series = returns[ticker]

# === 3. Compute Risk Metrics ===
hist_var = historical_var(return_series, confidence_level)
para_var = parametric_var(return_series, confidence_level)
cvar = conditional_var(return_series, confidence_level)
mdd = max_drawdown(price_series)

# === 4. Display Results ===
print(f"📊 Risk Metrics for {ticker} ({confidence_level*100:.0f}% confidence):\n")
print(f"Historical VaR:  {hist_var:.4f}")
print(f"Parametric VaR:  {para_var:.4f}")
print(f"Conditional VaR: {cvar:.4f}")
print(f"Max Drawdown:    {mdd * 100:.2f}%")

# === 5. Plot Drawdown ===
plot_drawdown(price_series, title=f"{ticker} Drawdown", filename="plots/drawdown_chart.png")

