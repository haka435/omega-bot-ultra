import yfinance as yf

def get_price_data(symbol="BTC-USD", period="7d", interval="1h"):
    data = yf.download(tickers=symbol, period=period, interval=interval)
    return data

def generate_real_signal(symbol="BTC-USD"):
    df = get_price_data(symbol)
    df["SMA_5"] = df["Close"].rolling(window=5).mean()
    df["SMA_10"] = df["Close"].rolling(window=10).mean()

    if df["SMA_5"].iloc[-1] > df["SMA_10"].iloc[-1]:
        return f"Signal für {symbol}: 📈 KAUFEN"
    else:
        return f"Signal für {symbol}: 📉 VERKAUFEN"
