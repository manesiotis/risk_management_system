# 🚨 Project 8: Risk Management System

This project implements core risk management metrics and visualizations for financial assets or trading strategies. It allows the user to evaluate historical and statistical measures of risk using price or return data.

## 🎯 Goal

Build a reusable system to calculate and visualize key risk metrics such as:
- Value at Risk (VaR)
- Conditional VaR (CVaR)
- Maximum Drawdown
- Volatility (optional)

## 🧱 Project Structure

```bash
risk_management_system/
├── data_loader.py           # Load price data and calculate returns
├── risk_metrics.py          # VaR, CVaR, Max Drawdown calculations
├── plotting.py              # Drawdown visualization
├── run_risk_analysis.py     # Main script for risk analysis
├── plots/                   # Folder for saved figures
└── README.md                # Project documentation
```

## 📊 Features

- Historical VaR
- Parametric (Gaussian) VaR
- Conditional Value at Risk (CVaR)
- Maximum Drawdown from price series
- Drawdown chart visualization
- Log or simple returns toggle

## 💾 Dependencies

- `numpy`
- `pandas`
- `matplotlib`
- `yfinance`
- `scipy`

Install them with:

```bash
pip install numpy pandas matplotlib yfinance scipy
```

## ▶️ How to Run

```bash
python run_risk_analysis.py
```

This script will:
- Download price data (e.g. AAPL)
- Calculate returns and risk metrics
- Print risk measures to the console
- Generate and save a drawdown chart in `plots/`

## 📈 Output Example

```
📊 Risk Metrics for AAPL (95% confidence):

Historical VaR:  -0.0295
Parametric VaR:  -0.0312
Conditional VaR: -0.0438
Max Drawdown:    -42.18%
```
### ℹ️ How Drawdown is Calculated

The drawdown chart visualizes the percentage drop in price from the previous peak over time.

- **Drawdown(t) = (P(t) - max(P[:t])) / max(P[:t])**
- It measures how far the asset has declined from its **historical maximum value up to that date**.
- It is **not** relative to the first data point, but dynamically updates as new peaks are reached.

This helps assess the depth and duration of losses during downturns.


Output plot saved at:

```
plots/drawdown_chart.png
```

---

✔️ A solid base for risk dashboards or integration into trading frameworks.
