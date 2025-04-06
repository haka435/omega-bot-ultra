import yfinance as yf
import pandas as pd

def get_price_data(symbol, period="3mo", interval="1d"):
    try:
        data = yf.download(symbol, period=period, interval=interval)
        if data.empty:
            return None
        data['RSI'] = calculate_rsi(data['Close'])
        data['MACD'], data['MACD_signal'] = calculate_macd(data['Close'])
        data['Combined_Signal'] = generate_combined_signal(data)
        return data
    except Exception as e:
        return None

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(series, short=12, long=26, signal=9):
    ema_short = series.ewm(span=short, adjust=False).mean()
    ema_long = series.ewm(span=long, adjust=False).mean()
    macd = ema_short - ema_long
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line

def generate_combined_signal(df):
    signals = []
    for rsi, macd, macd_signal in zip(df['RSI'], df['MACD'], df['MACD_signal']):
        if pd.isna(rsi) or pd.isna(macd) or pd.isna(macd_signal):
            signals.append("Keine Daten")
        elif rsi < 30 and macd > macd_signal:
            signals.append(f"KAUFEN ✅ (RSI: {round(rsi,1)}, MACD cross)")
        elif rsi > 70 and macd < macd_signal:
            signals.append(f"VERKAUFEN ❌ (RSI: {round(rsi,1)}, MACD cross)")
        else:
            signals.append("NEUTRAL ⚠️")
    return signals
