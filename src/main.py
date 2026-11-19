import UI as ui
import portfolio_logic as pm

def main():
    manager = pm.PortfolioManager()

    global tickers

    while(True):
        ui.printCommands()
        user = input()

        match user:
            case '0':
                break
            case '1':
                new_tickers = ui.addTicker()
                manager.addTicker(new_tickers)
            case '2':
                new_tickers = ui.addTickers()
                for t in new_tickers:
                    manager.addTicker(t)
            case '3':
                ui.printCurrentTickers(manager.getTickers())
                ticker = ui.removeTicker()
                manager.removeTicker(ticker)
            case '4':
                ui.printCurrentTickers(manager.getTickers())
            case '5':
                manager.calculatePortfolios()
            case '6':
                res = manager.getResults()
                ui.printResults(res['min_r'], res['min_r_risk'], res['min_r_return'], res['max_S'], res['max_S_risk'], res['max_S_return'])

if __name__ == '__main__':
    main()
