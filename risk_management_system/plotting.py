# plotting.py

import matplotlib.pyplot as plt
import pandas as pd

def compute_drawdown_series(price_series):
    """
    Return drawdown series as percentage
    """
    cumulative = price_series / price_series.iloc[0]
    rolling_max = cumulative.cummax()
    drawdown = (cumulative - rolling_max) / rolling_max
    return drawdown

def plot_drawdown(price_series, title="Drawdown Chart", filename=None, show=True):
    """
    Plot the drawdown over time, with optional saving and showing
    """
    drawdown = compute_drawdown_series(price_series)

    plt.figure(figsize=(10, 5))
    plt.plot(drawdown.index, drawdown.values, color='red', label='Drawdown')
    plt.fill_between(drawdown.index, drawdown.values, color='red', alpha=0.3)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.grid(True)
    plt.legend()

    if filename:
        plt.savefig(filename)
    
    if show:
        plt.show()

