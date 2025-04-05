import streamlit as st
from signal_engine import generate_real_signal, get_price_data
import plotly.express as px

st.set_page_config(page_title="OMEGA BOT ULTRA", layout="wide")
st.title("OMEGA BOT ULTRA Dashboard")

selected_market = st.selectbox("Wähle einen Markt", ["BTC-USD", "ETH-USD"])

# Daten laden
df = get_price_data(selected_market)
st.subheader(f"📊 Chart für {selected_market}")
fig = px.line(df, x=df.index, y="Close", title="Kursverlauf")
st.plotly_chart(fig, use_container_width=True)

# Signal anzeigen
signal = generate_real_signal(selected_market)
st.subheader(f"📈 Signal für {selected_market}:")
st.success(signal)
