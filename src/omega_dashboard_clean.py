import streamlit as st
from signal_engine import generate_real_signal, get_price_data
import plotly.express as px

st.set_page_config(page_title="OMEGA BOT ULTRA", layout="wide")
st.title("OMEGA BOT ULTRA Dashboard")

# Nur Gold als Markt
selected_market = "GC=F"  # Yahoo Finance Symbol für Gold Futures

# Daten laden
df = get_price_data(selected_market)

if df is not None and not df.empty and "Close" in df.columns:
    st.subheader(f"📈 Chart für {selected_market}")
    fig = px.line(df, x=df.index, y="Close", title="Kursverlauf (Gold)")
    st.plotly_chart(fig, use_container_width=True)

    # Signal anzeigen
    signal = generate_real_signal(selected_market)
    st.subheader(f"🚨 Signal für {selected_market}:")
    st.success(signal)
rsi_signal = generate_rsi_signal(selected_market)
st.subheader("📊 RSI-Analyse")
st.info(rsi_signal)

else:
    st.error("❌ Keine Daten für Gold gefunden. Bitte später erneut versuchen.")
from signal_engine import generate_real_signal, get_price_data, generate_rsi_signal
