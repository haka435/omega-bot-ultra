import streamlit as st
from signal_engine import generate_rsi_signal, get_price_data
import plotly.express as px

# Setup
st.set_page_config(page_title="OMEGA BOT ULTRA", layout="wide")
st.title("OMEGA BOT ULTRA Dashboard")

# Marktwahl
selected_market = st.selectbox("Wähle einen Markt", ["BTC-USD", "GC=F"])

# Daten holen
df = get_price_data(selected_market)

# Spaltennamen vereinheitlichen (kleinschreiben)
if df is not None:
    df.columns = [col[0].lower() if isinstance(col, tuple) else col.lower() for col in df.columns]

# Wenn Daten vorhanden & gültig
if df is not None and not df.empty and "close" in df.columns and df["close"].dropna().size > 0:
    # Chart anzeigen
    st.subheader(f"📈 Chart für {selected_market}")
    fig = px.line(df.reset_index(), x=df.index.name or "date", y="close", title=f"Kursverlauf ({selected_market})")
    st.plotly_chart(fig, use_container_width=True)

    # RSI-Signal anzeigen
    signal = generate_rsi_signal(selected_market)
    st.subheader(f"📊 RSI Signal für {selected_market}:")
    st.success(signal)
else:
    st.error(f"❌ Keine gültigen Daten für {selected_market} gefunden. "
             f"Vielleicht ist die Börse geschlossen oder YFinance liefert keine Daten.")
