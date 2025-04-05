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
def calculate_rsi(df, period=14):
    delta = df["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
def generate_rsi_signal(symbol="BTC-USD"):
    df = get_price_data(symbol)
    df["RSI"] = calculate_rsi(df)

    last_rsi = df["RSI"].iloc[-1]

    if last_rsi < 30:
        return f"RSI: {last_rsi:.2f} → 📈 KAUFEN (überverkauft)"
    elif last_rsi > 70:
        return f"RSI: {last_rsi:.2f} → 📉 VERKAUFEN (überkauft)"
    else:
        return f"RSI: {last_rsi:.2f} → 🟡 NEUTRAL"
