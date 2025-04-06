import streamlit as st
from signal_engine import generate_rsi_signal, get_price_data
import plotly.express as px

st.set_page_config(page_title="OMEGA BOT ULTRA", layout="wide")
st.title("OMEGA BOT ULTRA Dashboard")

# Märkte zur Auswahl
selected_market = st.selectbox("Wähle einen Markt", ["BTC-USD", "GC=F"])

# Daten laden
df = get_price_data(selected_market)

# Wenn Daten gültig sind
if df is not None and not df.empty and "Close" in df.columns and df["Close"].dropna().size > 0:
    st.subheader(f"📈 Chart für {selected_market}")
    fig = px.line(df.reset_index(), x="Date", y="Close", title=f"Kursverlauf ({selected_market})")
    st.plotly_chart(fig, use_container_width=True)

    # Signal anzeigen
    signal = generate_rsi_signal(selected_market)
    st.subheader(f"🧠 RSI Signal für {selected_market}:")
    st.success(signal)
else:
    st.error(f"❌ Keine gültigen Daten für {selected_market} gefunden. Vielleicht ist die Börse geschlossen oder YFinance liefert gerade nichts zurück.")
