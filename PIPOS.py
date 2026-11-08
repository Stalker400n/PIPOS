from datetime import datetime
import yfinance as yf
import numpy as np
import pandas as pd

tickers = []

min_r = pd.DataFrame()
max_S = pd.DataFrame()

user = ''

def printCurrentTickers():
    print('Current specified tickers:')
    print(tickers)

def printCommands():
    print(' 0. exit\n 1. add ticker\n 2. remove ticker\n 3. current tickers\n 4. calculate portfolios \n 5. show rezults')

def addTicker():
    print('enter ticker to add:')
    user = input()
    tickers.append(user)
    print('ticker added')

def removeTicker():
    print('enter ticker to remove:')
    user = input()
    tickers.remove(user)
    print('ticker removed')

def printResults():
    print('results')
    print('min_r:')
    print(min_r)
    print('max_S:')
    print(max_S)


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

def calculatePortfolios():
    global min_r
    global max_S

    print('Getting data...')

    data = getData()

    _mu = data.mean().to_numpy()

    _ones = np.ones_like(_mu)

    _cov = data.cov().to_numpy()

    _inv_cov = np.linalg.pinv(_cov)

    _min_r = calculateMinR(_mu, _ones, _inv_cov)
    _max_S = calculateMaxS(_mu, _ones, _inv_cov)

    min_r = pd.DataFrame(_min_r, index=data.columns)
    max_S = pd.DataFrame(_max_S, index=data.columns)

    print('calculating...')
    printResults()



while(True):
    printCommands()
    user = input()

    match user:
        case '0':
            break
        case '1':
            addTicker()
        case '2':
            printCurrentTickers()
            removeTicker()
        case '3':
            printCurrentTickers()
        case '4':
            calculatePortfolios()
        case '5':
            printResults()

