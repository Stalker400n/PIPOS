from datetime import datetime
import yfinance as yf
import math as math
import numpy as np
import pandas as pd

tickers = []

min_r = pd.DataFrame()
max_S = pd.DataFrame()

min_r_risk = 0
min_r_return = 0

max_S_risk = 0
max_S_return = 0

def getData(tickers):
    data = yf.download(tickers, start='2024-01-01', interval='1mo')

    _closing = data["Close"]

    _returns = _closing.pct_change()
    _returns = _returns.dropna()

    current_month = datetime.today().strftime('%Y-%m')

    if _returns.index[-1].strftime('%Y-%m') == current_month:
        _returns = _returns.iloc[:-1]

    return _returns


def calculateMinR(_mu, _ones, _inv_cov):
    _inv_cov_x_ones_T = _inv_cov @ _ones.reshape(-1, 1)

    _ones_x_inv_cov_x_ones_T = _ones @ _inv_cov @ _ones.reshape(-1, 1)

    return _inv_cov_x_ones_T / _ones_x_inv_cov_x_ones_T

def calculateMaxS(_mu, _ones, _inv_cov):
    _inv_cov_x_mu_T = _inv_cov @ _mu.reshape(-1, 1)

    _ones_x_inv_cov_x_mu_T = _ones @ _inv_cov @ _mu.reshape(-1, 1)

    return _inv_cov_x_mu_T / _ones_x_inv_cov_x_mu_T

def calculateRisk(port, cov):
    return np.sqrt(port.reshape(1, -1) @ cov @ port)

def calculateReturn(port, mu):
    return mu @ port

