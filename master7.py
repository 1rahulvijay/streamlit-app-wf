"""
BizView Executive Dashboard - ULTRA PREMIUM EDITION v4.0
Restored Aesthetics (master6.py) + Layout Fixes + Loading Screen
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime
import time

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="BizView Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# LOADING SYSTEM
# ============================================================================
if 'app_loaded' not in st.session_state:
    st.session_state.app_loaded = False

if not st.session_state.app_loaded:
    with st.empty():
        # Premium Loading Screen
        st.markdown("""
        <style>
            .stApp { background: #0f172a !important; }
            .loading-container {
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                text-align: center;
                z-index: 9999;
            }
            .loading-logo {
                font-size: 80px;
                animation: pulse 2s infinite;
                margin-bottom: 20px;
            }
            .loading-text {
                font-family: 'Outfit', sans-serif;
                color: #ffffff;
                font-size: 24px;
                font-weight: 300;
                letter-spacing: 4px;
                margin-top: 20px;
            }
            .loading-bar {
                width: 300px;
                height: 4px;
                background: rgba(255,255,255,0.1);
                border-radius: 2px;
                margin: 20px auto;
                overflow: hidden;
            }
            .loading-progress {
                width: 0%;
                height: 100%;
                background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4);
                animation: load 2s ease-in-out forwards;
            }
            @keyframes pulse {
                0% { transform: scale(1); opacity: 1; filter: drop-shadow(0 0 0 rgba(59,130,246,0)); }
                50% { transform: scale(1.1); opacity: 0.8; filter: drop-shadow(0 0 30px rgba(59,130,246,0.5)); }
                100% { transform: scale(1); opacity: 1; filter: drop-shadow(0 0 0 rgba(59,130,246,0)); }
            }
            @keyframes load {
                0% { width: 0%; }
                50% { width: 70%; }
                100% { width: 100%; }
            }
        </style>
        <div class="loading-container">
            <div class="loading-logo">📊</div>
            <div class="loading-text">BIZVIEW</div>
            <div class="loading-bar">
                <div class="loading-progress"></div>
            </div>
            <div style="color: #64748b; font-family: 'Inter'; font-size: 14px; margin-top: 10px;">Initializing Enterprise Modules...</div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(2.5)
        st.session_state.app_loaded = True
        st.rerun()

# ============================================================================
# PREMIUM CSS - RESTORED FROM MASTER6.PY
# ============================================================================
st.markdown(
    """
<style>
    /* ========== 8K PREMIUM FONTS ========== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    /* ========== CSS VARIABLES ========== */
    :root {
        --navy-950: #020617;
        --navy-900: #0f172a;
        --navy-800: #1e293b;
        --blue-500: #3b82f6;
        --blue-600: #2563eb;
        --cyan-500: #06b6d4;
        --emerald-500: #10b981;
        --amber-500: #f59e0b;
        --rose-500: #f43f5e;
        --violet-500: #8b5cf6;
        --white: #ffffff;
        --gray-50: #f8fafc;
        --gray-100: #f1f5f9;
        --gray-400: #94a3b8;
        
        --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        --shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        --gradient-mesh: radial-gradient(at 0% 0%, rgba(59, 130, 246, 0.15) 0%, transparent 50%),
                         radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
                         radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.15) 0%, transparent 50%),
                         radial-gradient(at 0% 100%, rgba(16, 185, 129, 0.15) 0%, transparent 50%);
    }

    /* ========== GLOBAL RESETS ========== */
    * {
        font-family: 'Inter', sans-serif !important;
        -webkit-font-smoothing: antialiased !important;
    }

    #MainMenu, footer, .stDeployButton { visibility: hidden !important; height: 0 !important; }
    [data-testid="stToolbar"] { display: none !important; }
    [data-testid="stHeader"] { background: transparent !important; pointer-events: none !important; }
    [data-testid="stHeader"] button { pointer-events: auto !important; }

    /* ========== MAIN APP BACKGROUND ========== */
    .stApp {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%) !important;
    }
    .stApp::before {
        content: ''; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
        background: var(--gradient-mesh); pointer-events: none; opacity: 0.5; z-index: 0;
    }

    /* ========== LAYOUT FIX: ZERO PADDING ========== */
    .main .block-container {
        padding-top: 0 !important;
        padding-bottom: 2rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 1920px !important;
        margin: 0 auto !important;
    }
    .main > div:first-child { padding-top: 0 !important; margin-top: 0 !important; }
    [data-testid="stVerticalBlock"] { gap: 1rem !important; }

    /* ========== SIDEBAR STYLING ========== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #050a14 0%, #0a1628 30%, #0f172a 60%, #0a1628 100%) !important;
        border-right: 1px solid rgba(59, 130, 246, 0.2) !important;
        box-shadow: 4px 0 32px rgba(0, 0, 0, 0.3) !important;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] p {
        color: rgba(255, 255, 255, 0.92) !important;
    }
    [data-testid="stSidebar"] .stButton > button {
        background: rgba(255, 255, 255, 0.03) !important;
        color: #94a3b8 !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        justify-content: flex-start !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(59, 130, 246, 0.12) !important;
        color: #f8fafc !important;
        border-color: rgba(59, 130, 246, 0.35) !important;
        transform: translateX(6px) !important;
    }
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.25) 0%, rgba(59, 130, 246, 0.08) 100%) !important;
        color: #ffffff !important;
        border-left: 3px solid #3b82f6 !important;
        border-radius: 3px 10px 10px 3px !important;
    }

    /* ========== SIDEBAR TOGGLE BUTTON ========== */
    [data-testid="collapsedControl"] {
        position: fixed !important; top: 0.875rem !important; left: 0.875rem !important;
        z-index: 999999 !important;
        background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%) !important;
        border: 1px solid rgba(59, 130, 246, 0.4) !important;
        border-radius: 12px !important;
        width: 2.75rem !important; height: 2.75rem !important;
        display: flex !important; align-items: center !important; justify-content: center !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.4s ease !important;
    }
    [data-testid="collapsedControl"]:hover {
        transform: scale(1.1) rotate(3deg) !important;
        box-shadow: 0 0 32px rgba(59, 130, 246, 0.5) !important;
    }
    [data-testid="collapsedControl"] svg {
        color: white !important; width: 1.4rem !important; height: 1.4rem !important;
    }

    /* ========== TYPOGRAPHY ========== */
    h1, h2, h3 { font-family: 'Outfit', sans-serif !important; font-weight: 700 !important; color: var(--navy-900) !important; }
    h1 { 
        font-size: 2.25rem !important; 
        background: linear-gradient(135deg, #0f172a 0%, #334155 100%); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important; padding-top: 0 !important;
    }

    /* ========== KPI CARDS (RESTORED) ========== */
    .kpi-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.97) 0%, rgba(255, 255, 255, 0.9) 100%);
        backdrop-filter: blur(40px);
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 18px;
        padding: 1.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
        transition: all 0.5s ease;
        animation: kpiEntrance 0.6s backwards;
    }
    .kpi-card::after {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #06b6d4, #10b981);
        opacity: 0; transition: opacity 0.4s ease;
    }
    .kpi-card:hover { transform: translateY(-10px) scale(1.02); box-shadow: 0 20px 50px rgba(59, 130, 246, 0.2); }
    .kpi-card:hover::after { opacity: 1; }
    
    .kpi-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        background: linear-gradient(145deg, #0f172a 0%, #475569 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
        animation: valueReveal 0.8s ease;
    }
    
    .kpi-icon-wrapper {
        width: 56px; height: 56px; border-radius: 16px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        transition: transform 0.4s ease;
    }
    .kpi-card:hover .kpi-icon-wrapper { transform: scale(1.1) rotate(5deg); }
    .kpi-icon { font-size: 1.6rem; animation: float 4s ease-in-out infinite; }
    
    .success { background: linear-gradient(145deg, #d1fae5 0%, #a7f3d0 100%); box-shadow: 0 8px 20px rgba(16, 185, 129, 0.3); }
    .warning { background: linear-gradient(145deg, #fed7aa 0%, #fdba74 100%); box-shadow: 0 8px 20px rgba(245, 158, 11, 0.3); }
    .kpi-change { font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.6rem; border-radius: 100px; display: inline-flex; align-items: center; gap: 4px; }
    .kpi-change.up { background: #dcfce7; color: #166534; }
    .kpi-change.down { background: #fee2e2; color: #991b1b; }

    /* ========== CHART CARDS ========== */
    .chart-card {
        background: linear-gradient(145deg, rgba(255, 255, 255, 0.97) 0%, rgba(255, 255, 255, 0.92) 100%);
        backdrop-filter: blur(40px);
        border: 1px solid rgba(255, 255, 255, 0.7);
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
        transition: all 0.5s ease;
        margin-bottom: 1.5rem;
    }
    .chart-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 16px 48px rgba(59, 130, 246, 0.12);
        border-color: rgba(59, 130, 246, 0.25);
    }
    .chart-card-header {
        padding: 1.25rem 1.5rem;
        background: linear-gradient(180deg, rgba(248, 250, 252, 0.95) 0%, rgba(255, 255, 255, 0.6) 100%);
        border-bottom: 1px solid rgba(226, 232, 240, 0.6);
    }
    .chart-card-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.825rem !important;
        font-weight: 800 !important;
        color: #0f172a !important;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }

    /* ========== ANIMATIONS ========== */
    @keyframes kpiEntrance { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes valueReveal { from { opacity: 0; filter: blur(5px); } to { opacity: 1; filter: blur(0); } }
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
    
</style>
    """,
    unsafe_allow_html=True,
)

# ============================================================================
# MOCK DATA
# ============================================================================
kpi_data = {
    "workflow_count": {"value": 1247, "change": 12.5, "trend": "up", "label": "Total Workflows", "icon": "📊"},
    "volume_gearing_ratio": {"value": 2.45, "change": 8.3, "trend": "up", "label": "Volume Gearing Ratio", "icon": "📈"},
    "productivity": {"value": 87.3, "change": 5.2, "trend": "up", "label": "Productivity Score", "icon": "👥"},
    "tech_adoption": {"value": 76.8, "change": -2.1, "trend": "down", "label": "Tech Adoption Rate", "icon": "💻"},
}

workflow_trend_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Completed": [145, 162, 178, 195, 210, 225, 198, 235, 248, 262, 278, 290],
    "Pending": [23, 18, 25, 20, 15, 22, 28, 19, 16, 21, 17, 24],
    "Failed": [5, 8, 4, 6, 3, 7, 9, 4, 5, 6, 3, 8],
})

department_breakdown = pd.DataFrame({
    "Department": ["Engineering", "Sales", "Marketing", "Operations", "Other"],
    "Value": [35, 25, 15, 15, 10],
})

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def get_chart_config():
    return {
        "displayModeBar": False,
        "responsive": True,
        "displaylogo": False,
    }

def get_chart_layout(title="", height=350):
    return {
        "title": {"text": title, "font": {"family": "Outfit, sans-serif", "size": 14}, "y": 0.95},
        "margin": {"l": 40, "r": 20, "t": 40, "b": 40},
        "plot_bgcolor": "rgba(0,0,0,0)",
        "paper_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Inter, sans-serif", "size": 11, "color": "#64748b"},
        "xaxis": {"showgrid": False, "showline": True, "linecolor": "#e2e8f0"},
        "yaxis": {"showgrid": True, "gridcolor": "#f1f5f9", "zeroline": False},
        "height": height
    }

def render_kpi_card(label, value, change, trend, format_type="number", icon="📊"):
    display_value = f"{value}%" if format_type == "percentage" else f"{value}"
    trend_type = "up" if trend == "up" else "down"
    icon_bg = "success" if trend == "up" else "warning"
    
    st.markdown(f"""
    <div class="kpi-card">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <div class="kpi-label" style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase;">{label}</div>
                <div class="kpi-value">{display_value}</div>
                <div class="kpi-change {trend_type}">
                    <span>{trend_type.upper()} {abs(change)}%</span>
                </div>
            </div>
            <div class="kpi-icon-wrapper {icon_bg}">
                <div class="kpi-icon">{icon}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_workflow_bar_chart(data):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data["Month"], y=data["Completed"], name="Completed", marker_color="#10b981"))
    fig.add_trace(go.Bar(x=data["Month"], y=data["Pending"], name="Pending", marker_color="#f59e0b"))
    fig.add_trace(go.Bar(x=data["Month"], y=data["Failed"], name="Failed", marker_color="#ef4444"))
    fig.update_layout(barmode='stack', **get_chart_layout(height=350))
    return fig

def create_donut_chart(data):
    fig = go.Figure(data=[go.Pie(
        labels=data["Department"], 
        values=data["Value"], 
        hole=0.7,
        marker=dict(colors=["#3b82f6", "#8b5cf6", "#06b6d4", "#10b981", "#f59e0b"])
    )])
    fig.update_layout(showlegend=False, 
                      annotations=[dict(text=f"{data['Value'].sum()}%", x=0.5, y=0.5, font_size=24, showarrow=False)],
                      **get_chart_layout(height=350))
    return fig

# ============================================================================
# SIDEBAR
# ============================================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <div style="font-size: 3rem; filter: drop-shadow(0 0 20px rgba(59,130,246,0.6)); animation: pulse 3s infinite;">📊</div>
        <h2 style="color:white !important; margin-top: 1rem;">BizView</h2>
        <p style="color: #94a3b8; font-size: 0.8rem; letter-spacing: 2px;">ULTRA PREMIUM</p>
    </div>
    <hr style="border: 0; height: 1px; background: rgba(255,255,255,0.1); margin: 0 0 2rem 0;">
    """, unsafe_allow_html=True)
    
    if st.button("🏠 Dashboard", type="primary", use_container_width=True): pass
    if st.button("📊 Analytics", use_container_width=True): pass
    if st.button("💰 Finance", use_container_width=True): pass
    if st.button("⚙️ Settings", use_container_width=True): pass

# ============================================================================
# MAIN DASHBOARD
# ============================================================================
st.markdown("# 🏠 Executive Dashboard")
st.markdown("<p style='color: #64748b; margin-top: -10px; margin-bottom: 2rem;'>Real-time enterprise analytics and performance metrics.</p>", unsafe_allow_html=True)

# KPI ROW
col1, col2, col3, col4 = st.columns(4)
with col1: render_kpi_card(**kpi_data["workflow_count"])
with col2: render_kpi_card(**kpi_data["volume_gearing_ratio"])
with col3: render_kpi_card(**kpi_data["productivity"])
with col4: render_kpi_card(**kpi_data["tech_adoption"])

st.markdown("<div style='height: 2rem;'></div>", unsafe_allow_html=True)

# CHARTS ROW
c1, c2 = st.columns([2, 1])

with c1:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-header"><div class="chart-card-title">WORKFLOW VELOCITY</div></div>', unsafe_allow_html=True)
    st.plotly_chart(create_workflow_bar_chart(workflow_trend_data), use_container_width=True, config=get_chart_config())
    st.markdown("</div>", unsafe_allow_html=True)

with c2:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown('<div class="chart-card-header"><div class="chart-card-title">DEPARTMENT SPLIT</div></div>', unsafe_allow_html=True)
    st.plotly_chart(create_donut_chart(department_breakdown), use_container_width=True, config=get_chart_config())
    st.markdown("</div>", unsafe_allow_html=True)
