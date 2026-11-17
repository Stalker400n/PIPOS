tickers = []

user = ''

def printCommands():
    print(' 0. exit\n 1. add ticker\n 2. add tickers\n 3. remove ticker\n 4. current tickers\n 5. calculate portfolios \n 6. show rezults')

def printCurrentTickers():
    print('Current specified tickers:')
    print(tickers)

def addTicker():
    print('enter ticker to add:')
    user = input()
    tickers.append(user)
    print('ticker added')

    return tickers

def addTickers():
    print('enter tickers to add')
    print('seperate the tickers with a space between them')

    user = input()

    user = user.split()

    print(user)

    tickers.extend(user)

    print('tickers added')

    return tickers


def removeTicker():
    print('enter ticker to remove:')
    user = input()
    tickers.remove(user)
    print('ticker removed')

    return tickers

def printResults(min_r, min_r_risk, min_r_return, max_S, max_S_risk, max_S_return):
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
 



