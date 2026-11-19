import external as ext
import calc as calc
import numpy as np
import pandas as pd


class PortfolioManager:
    def __init__(self):
        self.tickers = []
        self.min_r = pd.DataFrame()
        self.max_S = pd.DataFrame()
        self.min_r_risk = 0
        self.min_r_return = 0
        self.max_S_risk = 0
        self.max_S_return = 0

    def addTicker(self, ticker):
        if ticker not in self.tickers:
            self.tickers.append(ticker)

    def removeTicker(self, ticker):
        if ticker in self.tickers:
            self.tickers.remove(ticker)

    def getTickers(self):
        return self.tickers

    def calculatePortfolios(self):
        print('Getting data...')

        data = ext.getData(self.tickers)

        print('calculating...')

        _mu = data.mean().to_numpy()

        _ones = np.ones_like(_mu)

        _cov = data.cov().to_numpy()

        _inv_cov = np.linalg.pinv(_cov)

        _min_r = calc.calculateMinR(_mu, _ones, _inv_cov)
        _max_S = calc.calculateMaxS(_mu, _ones, _inv_cov)

        self.min_r_risk = calc.calculateRisk(_min_r, _cov).item()
        self.min_r_return = calc.calculateReturn(_min_r, _mu).item()

        self.max_S_risk = calc.calculateRisk(_max_S, _cov).item()
        self.max_S_return = calc.calculateReturn(_max_S, _mu).item()

        self.min_r = pd.DataFrame(_min_r, index=data.columns)
        self.max_S = pd.DataFrame(_max_S, index=data.columns)

    def getResults(self):
        return {
            'min_r': self.min_r,
            'max_S': self.max_S,
            'min_r_risk': self.min_r_risk,
            'min_r_return': self.min_r_return,
            'max_S_risk': self.max_S_risk,
            'max_S_return': self.max_S_return,
        }

