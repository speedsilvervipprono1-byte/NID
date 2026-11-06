import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Detection Rules", layout="wide")

css_file = Path(__file__).parent.parent / "assets" / "style.css"
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### NIDS Security")
    st.markdown("---")
    st.page_link("app.py", label="Dashboard")
    st.page_link("pages/1_Alerts.py", label="Alerts")
    st.page_link("pages/2_Traffic_Monitor.py", label="Traffic Monitor")
    st.page_link("pages/3_Analysis.py", label="Analysis")
    st.page_link("pages/4_Reports.py", label="Reports")
    st.page_link("pages/5_Rules.py", label="Rules")
    st.page_link("pages/6_System.py", label="System")
    st.page_link("pages/7_Settings.py", label="Settings")
    st.markdown("---")

st.markdown("## Detection Rules & Signatures")
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

st.checkbox("Enable Snort Rule Set v4.2", value=True)
st.checkbox("Enable Suricata Emerging Threats", value=True)
st.checkbox("Custom Rate-Limiting DDoS Rule", value=True)
st.slider("Anomaly Detection Sensitivity", 1, 10, 7)
