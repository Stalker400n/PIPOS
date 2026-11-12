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

user = ''

def printCurrentTickers():
    print('Current specified tickers:')
    print(tickers)

def printCommands():
    print(' 0. exit\n 1. add ticker\n 2. add tickers\n 3. remove ticker\n 4. current tickers\n 5. calculate portfolios \n 6. show rezults')

def addTicker():
    print('enter ticker to add:')
    user = input()
    tickers.append(user)
    print('ticker added')

def addTickers():
    print('enter tickers to add')
    print('seperate the tickers with a space between them')

    user = input()

    user = user.split()

    print(user)

    tickers.extend(user)

    print('tickers added')


def removeTicker():
    print('enter ticker to remove:')
    user = input()
    tickers.remove(user)
    print('ticker removed')

def printResults():
    print('results')

    print('min_r:')
    print(min_r)
    print('risk: ')
    print(min_r_risk)
    print('return: ')
    print(min_r_return)

    print('max_S:')
    print(max_S)
    print('risk: ')
    print(max_S_risk)
    print('return: ')
    print(max_S_return)
 


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
            addTickers()
        case '3':
            printCurrentTickers()
            removeTicker()
        case '4':
            printCurrentTickers()
        case '5':
            calculatePortfolios()
        case '6':
            printResults()

