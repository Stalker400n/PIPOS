import UI as ui
import calc as calc

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

def calculatePortfolios():
    global min_r
    global max_S

    global min_r_risk
    global min_r_return

    global max_S_risk
    global max_S_return

    print('Getting data...')

    data = calc.getData(tickers)

    print('calculating...')

    _mu = data.mean().to_numpy()

    _ones = np.ones_like(_mu)

    _cov = data.cov().to_numpy()

    _inv_cov = np.linalg.pinv(_cov)

    _min_r = calc.calculateMinR(_mu, _ones, _inv_cov)
    _max_S = calc.calculateMaxS(_mu, _ones, _inv_cov)

    min_r_risk = calc.calculateRisk(_min_r, _cov).item()
    min_r_return = calc.calculateReturn(_min_r, _mu).item()

    max_S_risk = calc.calculateRisk(_max_S, _cov).item()
    max_S_return = calc.calculateReturn(_max_S, _mu).item()

    min_r = pd.DataFrame(_min_r, index=data.columns)
    max_S = pd.DataFrame(_max_S, index=data.columns)





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

