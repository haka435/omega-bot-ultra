import streamlit as st
from signal_engine import generate_real_signal

st.set_page_config(page_title="OMEGA BOT ULTRA", layout="wide")
st.title("OMEGA BOT ULTRA Dashboard")

# Markt auswählen
selected_market = st.selectbox("Wähle einen Markt", ["BTC-USD", "ETH-USD"])

# Signal anzeigen
signal = generate_real_signal(selected_market)
st.subheader(f"📊 Signal für {selected_market}:")
st.success(signal)
