import UI as ui
import calc as calc

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

def getData():
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



def calculatePortfolios():
    global min_r
    global max_S

    global min_r_risk
    global min_r_return

    global max_S_risk
    global max_S_return


    print('Getting data...')

    data = getData()

    _mu = data.mean().to_numpy()

    _ones = np.ones_like(_mu)

    _cov = data.cov().to_numpy()

    _inv_cov = np.linalg.pinv(_cov)

    _min_r = calculateMinR(_mu, _ones, _inv_cov)
    _max_S = calculateMaxS(_mu, _ones, _inv_cov)

    min_r_risk = calculateRisk(_min_r, _cov).item()
    min_r_return = calculateReturn(_min_r, _mu).item()

    max_S_risk = calculateRisk(_max_S, _cov).item()
    max_S_return = calculateReturn(_max_S, _mu).item()

    min_r = pd.DataFrame(_min_r, index=data.columns)
    max_S = pd.DataFrame(_max_S, index=data.columns)

    print('calculating...')



while(True):
    ui.printCommands()
    user = input()

    match user:
        case '0':
            break
        case '1':
            tickers = ui.addTicker()
        case '2':
            tickers = ui.addTickers()
        case '3':
            ui.printCurrentTickers()
            tickers = ui.removeTicker()
        case '4':
            ui.printCurrentTickers()
        case '5':
            calculatePortfolios()
        case '6':
            ui.printResults(min_r, min_r_risk, min_r_return, max_S, max_S_risk, max_S_return)

