import streamlit as st
import plotly.express as px
from pathlib import Path
from src.data_loader import fetch_attack_distribution

st.set_page_config(page_title="Traffic Analysis", layout="wide")

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

st.markdown("## Deep Traffic & Attack Analysis")
st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

df = fetch_attack_distribution()
fig = px.bar(df, x='Type', y='Count', color='Type', color_discrete_sequence=['#3b82f6', '#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981'])
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#9ca3af'), showlegend=False)
st.plotly_chart(fig, use_container_width=True)
