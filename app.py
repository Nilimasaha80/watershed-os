import streamlit as st
import pandas as pd

st.set_page_config(page_title="WatershedOS", layout="wide")

st.title("🌊 WatershedOS - PMKSY-WDC 2.0 Dashboard")

tab1, tab2, tab3 = st.tabs(["💰 Fund Flow", "🗺️ Micro-Watershed Progress", "🏢 Institutional Metrics"])

with tab1:
    st.header("Fund Flow Overview")
    # Placeholder data
    data = {
        "State": ["Uttar Pradesh", "Madhya Pradesh"],
        "Total Fund (Cr)": [150, 180],
        "Released Fund (Cr)": [100, 120],
        "Utilized Fund (Cr)": [85, 110]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.bar_chart(df.set_index("State")[["Utilized Fund (Cr)"]])

with tab2:
    st.header("Progress of Micro-Watersheds")
    data2 = {
        "District": ["Etawah", "Jhansi", "Lalitpur"],
        "Total MW": [120, 90, 70],
        "Completed MW": [60, 45, 40],
        "In Progress": [60, 45, 30]
    }
    st.dataframe(pd.DataFrame(data2))

with tab3:
    st.header("Institutional Metrics")
    st.write("Coming soon: SHG participation, PIA performance, Watershed Committees")
