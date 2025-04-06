import yfinance as yf

def get_price_data(symbol="GC=F", period="7d", interval="1h"):
    data = yf.download(tickers=symbol, period=period, interval=interval)
    return data

def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def generate_real_signal(symbol="GC=F"):
    df = get_price_data(symbol)
    df["RSI"] = calculate_rsi(df)

    last_rsi = df["RSI"].iloc[-1]

    if last_rsi < 30:
        return f"📈 RSI: {last_rsi:.2f} → KAUFEN (Überverkauft)"
    elif last_rsi > 70:
        return f"📉 RSI: {last_rsi:.2f} → VERKAUFEN (Überkauft)"
    else:
        return f"🤝 RSI: {last_rsi:.2f} → NEUTRAL"
