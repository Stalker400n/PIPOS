import yfinance as yf

tickers = []

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

    return _returns


def calculatePortfolios():
    data = getData()

    print(data)

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
