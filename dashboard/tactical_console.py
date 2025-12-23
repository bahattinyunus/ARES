import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# Page Config
st.set_page_config(
    page_title="ARES Tactical Command Console",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #00d2ff;
    }
    .metric-card {
        background-color: #1a1c24;
        border: 1px solid #00d2ff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Courier New', Courier, monospace;
    }
</style>
""", unsafe_allow_stdio=True)

# Sidebar
st.sidebar.title("🛡️ ARES NODE CONTROL")
node_id = st.sidebar.text_input("NODE ID", "ARES-ALPHA-01")
status = st.sidebar.selectbox("OPERATIONAL STATUS", ["ACTIVE", "SILENT", "ENGAGED", "MAINTENANCE"])
st.sidebar.divider()
st.sidebar.info("Mesh Network: P2P Tunneling Active")

# Header
st.title("🛡️ PROJECT ARES: TACTICAL CONSOLE")
st.subheader("Decentralized Tactical Mesh Intelligence (DTMI)")

# Dashboard Layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="metric-card"><h3>PEERS DETECTED</h3><h1>14</h1></div>', unsafe_allow_stdio=True)

with col2:
    st.markdown('<div class="metric-card"><h3>THREAT SCORE</h3><h1>0.12</h1></div>', unsafe_allow_stdio=True)

with col3:
    st.markdown('<div class="metric-card"><h3>NETWORK LATENCY</h3><h1>4ms</h1></div>', unsafe_allow_stdio=True)

st.divider()

# Simulation View
st.subheader("🌐 MESH NETWORK TOPOLOGY (LIVE)")

# Mock Data for Mesh
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [39.9334, 32.8597], # Centered around Ankara
    columns=['lat', 'lon']
)
st.map(map_data)

# Auction Engine Visualization
st.divider()
st.subheader("📊 AUCTION-BASED TASK ALLOCATION")

auction_col1, auction_col2 = st.columns([1, 2])

with auction_col1:
    st.write("**CURRENT AUCTION: TARGET-ZULU-91**")
    st.write("Priority: **CRITICAL**")
    st.write("Type: **ARMORED UNIT**")

with auction_col2:
    chart_data = pd.DataFrame(
        np.random.rand(5, 1),
        columns=['Bid Cost'],
        index=['Drone A', 'Drone B', 'Drone C', 'Artillery-1', 'Infantry-Unit']
    )
    st.bar_chart(chart_data)

# Log Stream
st.divider()
st.subheader("📟 TACTICAL LOG STREAM")
log_placeholder = st.empty()

logs = [
    "[INFO] Peer discovery initiated via Zero-Conf...",
    "[CRYPTO] Session key rotated (PFS Active)",
    "[AI] Object detected manually: Tank-T72",
    "[MESH] Gossip protocol: Syncing global state",
    "[AUCTION] Task assigned to Drone-04 (Cost: 0.12)"
]

for i in range(5):
    log_text = "\n".join(logs[:i+1])
    log_placeholder.code(log_text)
    time.sleep(0.5)

st.success("TACTICAL CONSOLE RUNNING IN OBSERVER MODE")
