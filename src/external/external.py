from datetime import datetime
import yfinance as yf

def getData(tickers):
    data = yf.download(tickers, start='2024-01-01', interval='1mo')

    _closing = data["Close"]

    _returns = _closing.pct_change()
    _returns = _returns.dropna()

    current_month = datetime.today().strftime('%Y-%m')

    if _returns.index[-1].strftime('%Y-%m') == current_month:
        _returns = _returns.iloc[:-1]

    return _returns


