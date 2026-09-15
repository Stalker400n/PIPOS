
# the TUI part of getting all the 25 or less that the users wants to specify

tickers = []

user = ''

def printCurrentTickers():
    print('Current specified tickers:')
    print(tickers)

def printCommands():
    print(' 0. exit\n 1. add ticker\n 2. remove ticker\n 3. current tickers')

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


while(True):
    printCommands()
    user = input()
    if user == '0':
        break
    elif user == '1':
        addTicker()
    elif user == '2':
        printCurrentTickers()
        removeTicker()
    elif user == '3':
        printCurrentTickers()

