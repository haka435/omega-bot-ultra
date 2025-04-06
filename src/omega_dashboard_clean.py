import streamlit as st
from signal_engine import generate_real_signal, get_price_data
import plotly.express as px

st.set_page_config(page_title="OMEGA BOT ULTRA", layout="wide")
st.title("OMEGA BOT ULTRA Dashboard")

# Nur Gold (GC=F) als Markt
selected_market = "GC=F"

# Daten abrufen
df = get_price_data(selected_market)

# Wenn Daten da sind → Chart + Signal
if df is not None and not df.empty and "Close" in df.columns:
    st.subheader(f"📈 Chart für {selected_market}")
    fig = px.line(df, x=df.index, y="Close", title="Kursverlauf (Gold)")
    st.plotly_chart(fig, use_container_width=True)

    # RSI-Signal anzeigen
    signal = generate_real_signal(selected_market)
    st.subheader(f"📊 RSI Signal für {selected_market}:")
    st.success(signal)
else:
    st.error("❌ Keine Daten für Gold gefunden. Bitte später erneut versuchen.")
