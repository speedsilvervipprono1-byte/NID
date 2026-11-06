import streamlit as st
from pathlib import Path
from src.data_loader import fetch_recent_alerts

st.set_page_config(page_title="Alerts Management", layout="wide")

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

st.markdown("## Intrusion Alerts Management")
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.selectbox("Filter Severity", ["All", "Critical", "High", "Medium", "Low"])
with c2:
    st.selectbox("Filter Attack Type", ["All", "DDoS Attack", "SQL Injection", "Port Scan", "XSS Attack", "Brute Force"])
with c3:
    st.text_input("Search IP Address", placeholder="e.g. 192.168.1.105")

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
st.dataframe(fetch_recent_alerts(10), use_container_width=True, hide_index=True)
