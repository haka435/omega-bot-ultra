import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from signal_engine import get_price_data

st.set_page_config(layout="wide", page_title="Omega Finance Dashboard")

st.title("📈 Omega Finance Dashboard")
st.markdown("Wähle einen Markt aus und analysiere RSI- und MACD-basierte Signale.")

# ✅ Mehr Märkte
markets = {
    "Bitcoin (BTC-USD)": "BTC-USD",
    "Gold (GC=F)": "GC=F",
    "Apple (AAPL)": "AAPL",
    "Tesla (TSLA)": "TSLA",
    "S&P 500 (^GSPC)": "^GSPC",
    "DAX (^GDAXI)": "^GDAXI",
    "Öl (CL=F)": "CL=F",
    "EUR/USD (EURUSD=X)": "EURUSD=X",
}

choice = st.selectbox("📊 Markt auswählen:", options=list(markets.keys()))
symbol = markets[choice]

# 📦 Daten laden
data = get_price_data(symbol)

if data is None:
    st.error("❌ Daten konnten nicht geladen werden. Börse geschlossen oder Symbol ungültig?")
else:
    st.success("✅ Daten erfolgreich geladen.")

    # 🔹 Linechart Preis
    fig_price = px.line(data, x=data.index, y="Close", title=f"Kursverlauf von {symbol}")
    st.plotly_chart(fig_price, use_container_width=True)

    # 🔹 MACD Plot
    macd_fig = go.Figure()
    macd_fig.add_trace(go.Scatter(x=data.index, y=data["MACD"], name="MACD"))
    macd_fig.add_trace(go.Scatter(x=data.index, y=data["MACD_signal"], name="Signal-Linie"))
    macd_fig.update_layout(title="MACD-Indikator", xaxis_title="Datum", yaxis_title="MACD")
    st.plotly_chart(macd_fig, use_container_width=True)

    # 🔹 Signal-Output (aktuellster Tag)
    latest_signal = data["Combined_Signal"].iloc[-1]
    st.markdown(f"### 📢 Trading-Signal: `{latest_signal}`")
