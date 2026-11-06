import streamlit as st
import plotly.express as px
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

from src.data_loader import (
    fetch_traffic_overview, 
    fetch_attack_distribution, 
    fetch_recent_alerts, 
    fetch_system_metrics,
    fetch_top_metrics
)

st.set_page_config(
    page_title="NIDS Security Console",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st_autorefresh(interval=3000, key="nids_realtime_refresh")

css_file = Path(__file__).parent / "assets" / "style.css"
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
    st.markdown("<div style='font-size: 12px; color: #6b7280;'>System Status<br>🟢 All systems operational</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 11px; color: #4b5563; margin-top: 8px;'>Version 2.1.0</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns([3, 1, 1])
with c1:
    st.markdown("## Network Intrusion Detection System")
with c2:
    st.selectbox("Timeframe", ["Live Stream", "Last 24 Hours", "Last 7 Days"], label_visibility="collapsed")
with c3:
    st.button("Export Report", use_container_width=True)

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

cols = st.columns(5)
metrics = fetch_top_metrics()

for idx, (title, val, change) in enumerate(metrics):
    with cols[idx]:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">{title}</div>
                <div class="metric-value">{val}</div>
                <div class="metric-change-pos">↑ {change}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

col_chart1, col_chart2 = st.columns([7, 4])

with col_chart1:
    st.markdown("### Traffic Overview")
    df_traffic = fetch_traffic_overview()
    fig_line = px.line(
        df_traffic, x='Date', y=['Normal Traffic', 'Suspicious Traffic', 'Malicious Traffic'],
        color_discrete_map={'Normal Traffic': '#3b82f6', 'Suspicious Traffic': '#f59e0b', 'Malicious Traffic': '#ef4444'}
    )
    fig_line.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#9ca3af'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=0, r=0, t=20, b=0),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='#1f2937')
    )
    st.plotly_chart(fig_line, use_container_width=True)

with col_chart2:
    st.markdown("### Top Attack Types")
    df_attacks = fetch_attack_distribution()
    fig_donut = px.pie(
        df_attacks, names='Type', values='Count', hole=0.7,
        color_discrete_sequence=['#3b82f6', '#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981']
    )
    total_attacks = df_attacks['Count'].sum()
    fig_donut.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#9ca3af'),
        showlegend=True,
        legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1),
        margin=dict(l=0, r=0, t=10, b=10),
        annotations=[dict(text=f'<b>{total_attacks:,}</b><br>Total', x=0.5, y=0.5, font_size=14, font_color='white', showarrow=False)]
    )
    st.plotly_chart(fig_donut, use_container_width=True)

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

col_table, col_status = st.columns([7, 4])

with col_table:
    st.markdown("### Recent Alerts")
    st.dataframe(fetch_recent_alerts(5), use_container_width=True, hide_index=True)

with col_status:
    st.markdown("### System Status")
    sys_metrics = fetch_system_metrics()
    
    st.markdown(f"<div style='font-size: 13px; color: #9ca3af;'>CPU Usage <span style='float: right; color: white;'>{sys_metrics['cpu']}%</span></div>", unsafe_allow_html=True)
    st.progress(sys_metrics['cpu'])
    
    st.markdown(f"<div style='font-size: 13px; color: #9ca3af; margin-top: 12px;'>Memory Usage <span style='float: right; color: white;'>{sys_metrics['memory']}%</span></div>", unsafe_allow_html=True)
    st.progress(sys_metrics['memory'])
    
    st.markdown(f"<div style='font-size: 13px; color: #9ca3af; margin-top: 12px;'>Disk Usage <span style='float: right; color: white;'>{sys_metrics['disk']}%</span></div>", unsafe_allow_html=True)
    st.progress(sys_metrics['disk'])
    
    st.markdown(f"<div style='font-size: 13px; color: #9ca3af; margin-top: 12px;'>Network I/O <span style='float: right; color: white;'>{sys_metrics['network']}%</span></div>", unsafe_allow_html=True)
    st.progress(sys_metrics['network'])
