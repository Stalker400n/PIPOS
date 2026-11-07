
from datetime import datetime
import yfinance as yf
import numpy as np
import pandas as pd

tickers = []

min_r = []
max_S = []

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

def getData():
    data = yf.download(tickers, start='2024-01-01', interval='1mo')

    _closing = data["Close"]

    _returns = _closing.pct_change()
    _returns = _returns.dropna()

    current_month = datetime.today().strftime('%Y-%m')

    if _returns.index[-1].strftime('%Y-%m') == current_month:
        _returns = _returns.iloc[:-1]

    return _returns


def calculatePortfolios():
    data = getData()

    _mu = data.mean().to_numpy()

    _ones = np.ones_like(_mu)

    _cov = data.cov().to_numpy()

    _inv_cov = np.linalg.pinv(_cov)

    _inv_cov_x_mu_T = _inv_cov @ _mu.reshape(-1, 1)
    _inv_cov_x_ones_T = _inv_cov @ _ones.reshape(-1, 1)

    _ones_x_inv_cov_x_mu_T = _ones @ _inv_cov @ _mu.reshape(-1, 1)
    _ones_x_inv_cov_x_ones_T = _ones @ _inv_cov @ _ones.reshape(-1, 1)

    min_r = _inv_cov_x_ones_T / _ones_x_inv_cov_x_ones_T
    max_S = _inv_cov_x_mu_T / _ones_x_inv_cov_x_mu_T

    print(_mu)
    print(_ones)
    print(_cov)

    print(_inv_cov.dot(_cov))
    
    print(_inv_cov_x_mu_T)
    print(_inv_cov_x_ones_T)
    

    print(min_r)
    print(max_S)
    print('calculating')



while(True):
    printCommands()
    user = input()

    # later change to match statement

    if user == '0':
        break
    elif user == '1':
        addTicker()
    elif user == '2':
        printCurrentTickers()
        removeTicker()
    elif user == '3':
        printCurrentTickers()
    elif user == '4':
        calculatePortfolios()
    elif user == '5':
        printResults()
