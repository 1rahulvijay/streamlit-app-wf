"""
BizView Executive Dashboard - Complete Streamlit Application
A full replica of the React Executive Dashboard
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta
import io
import base64

# ============ PAGE CONFIGURATION ============
st.set_page_config(
    page_title="BizView Executive Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============ CUSTOM CSS - EXACT REACT REPLICA ============
st.markdown(
    """
<style>
    /* Import Fonts - Same as React */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Hide Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    header {visibility: hidden;}
    
    /* Root variables matching React */
    :root {
        --navy: #0F172A;
        --navy-light: #1E293B;
        --blue: #3B82F6;
        --cyan: #0EA5E9;
        --slate: #94A3B8;
        --amber: #D97706;
        --success: #10B981;
        --warning: #F59E0B;
        --error: #EF4444;
        --background: #F8FAFC;
        --card-bg: #FFFFFF;
        --border: #E2E8F0;
        --muted: #64748B;
    }
    
    /* Main app background */
    .stApp {
        background-color: var(--background) !important;
    }
    
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    
    /* Sidebar - Navy Theme */
    [data-testid="stSidebar"] {
        background-color: var(--navy) !important;
        padding-top: 0;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0;
    }
    
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.1) !important;
    }
    
    /* Sidebar navigation buttons */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        text-align: left !important;
        justify-content: flex-start !important;
        background-color: transparent !important;
        color: rgba(255, 255, 255, 0.7) !important;
        border: none !important;
        border-radius: 0 !important;
        padding: 0.75rem 1.5rem !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background-color: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border-right: 3px solid var(--amber) !important;
    }
    
    /* Sidebar select boxes */
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stSelectbox label {
        color: rgba(255, 255, 255, 0.6) !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    
    /* Headers - Outfit font */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif !important;
        color: var(--navy) !important;
        font-weight: 600 !important;
    }
    
    h1 { font-size: 1.5rem !important; }
    h2 { font-size: 1.25rem !important; }
    h3 { font-size: 1rem !important; }
    
    /* Body text - Inter font */
    p, span, div, label {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* KPI Card Styles */
    .kpi-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 0.5rem;
        padding: 1.5rem;
        transition: all 0.2s ease;
        height: 100%;
    }
    
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
    }
    
    .kpi-icon {
        width: 48px;
        height: 48px;
        border-radius: 0.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        font-size: 1.25rem;
    }
    
    .kpi-icon-up { background-color: #DCFCE7; }
    .kpi-icon-down { background-color: #FEE2E2; }
    
    .kpi-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: var(--navy) !important;
        line-height: 1.2;
        margin: 0;
    }
    
    .kpi-label {
        font-size: 0.875rem;
        color: var(--muted);
        margin-top: 0.25rem;
    }
    
    .kpi-change {
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        font-size: 0.75rem;
        font-weight: 600;
        margin-top: 0.5rem;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
    }
    
    .kpi-change-positive {
        background-color: #DCFCE7;
        color: #166534;
    }
    
    .kpi-change-negative {
        background-color: #FEE2E2;
        color: #991B1B;
    }
    
    /* Chart Card Styles */
    .chart-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 0.5rem;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    
    .chart-card-header {
        padding: 1rem 1.5rem;
        border-bottom: 1px solid #F1F5F9;
    }
    
    .chart-card-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 600 !important;
        color: var(--navy) !important;
        text-transform: uppercase;
        letter-spacing: 0.025em;
        margin: 0 !important;
    }
    
    .chart-card-subtitle {
        font-size: 0.75rem;
        color: var(--muted);
        margin-top: 0.25rem;
    }
    
    .chart-card-content {
        padding: 1.5rem;
    }
    
    /* Summary Card - Navy gradient */
    .summary-card {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: white;
        border-radius: 0.5rem;
        padding: 1.5rem;
        height: 100%;
    }
    
    .summary-card-title {
        color: var(--amber) !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 0.75rem;
    }
    
    .summary-card-content {
        font-size: 0.875rem;
        line-height: 1.75;
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Data Table Styles */
    .dataframe {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.875rem !important;
    }
    
    .dataframe th {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.75rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        color: var(--muted) !important;
        background-color: var(--background) !important;
    }
    
    /* Badge Styles */
    .badge {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        font-size: 0.75rem;
        font-weight: 600;
        border-radius: 9999px;
    }
    
    .badge-success { background-color: #DCFCE7; color: #166534; }
    .badge-warning { background-color: #FEF3C7; color: #92400E; }
    .badge-error { background-color: #FEE2E2; color: #991B1B; }
    .badge-navy { background-color: var(--navy); color: white; }
    
    /* Progress Bar */
    .progress-bar {
        height: 8px;
        background-color: var(--border);
        border-radius: 4px;
        overflow: hidden;
    }
    
    .progress-bar-fill {
        height: 100%;
        border-radius: 4px;
        transition: width 0.3s ease;
    }
    
    /* Header bar */
    .header-bar {
        background: var(--card-bg);
        border-bottom: 1px solid var(--border);
        padding: 1rem 0;
        margin-bottom: 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .header-title {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: var(--navy) !important;
        margin: 0 !important;
    }
    
    /* Filter bar */
    .filter-bar {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 0.5rem;
        padding: 1rem 1.5rem;
        margin-bottom: 1.5rem;
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
        align-items: center;
    }
    
    /* Button Styles */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 500 !important;
        border-radius: 0.375rem !important;
        transition: all 0.2s ease !important;
    }
    
    /* Primary button - Navy */
    .primary-btn > button {
        background-color: var(--navy) !important;
        color: white !important;
        border: none !important;
    }
    
    .primary-btn > button:hover {
        background-color: var(--navy-light) !important;
    }
    
    /* Secondary button - Outline */
    .secondary-btn > button {
        background-color: white !important;
        color: var(--navy) !important;
        border: 1px solid var(--border) !important;
    }
    
    .secondary-btn > button:hover {
        background-color: var(--background) !important;
    }
    
    /* Insight cards */
    .insight-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 0.5rem;
        padding: 1.5rem;
    }
    
    .insight-card h4 {
        font-size: 0.875rem !important;
        color: var(--muted) !important;
        margin-bottom: 0.5rem !important;
    }
    
    .insight-value {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.75rem !important;
        font-weight: 700 !important;
    }
    
    .insight-label {
        font-size: 0.875rem;
        color: var(--muted);
        margin-top: 0.25rem;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.3s ease-out forwards;
    }
    
    /* Print styles */
    @media print {
        [data-testid="stSidebar"] { display: none !important; }
        .no-print { display: none !important; }
        .stApp { background: white !important; }
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--background);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: rgba(100, 116, 139, 0.3);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(100, 116, 139, 0.5);
    }
    
    /* Metric override */
    [data-testid="stMetricValue"] {
        font-family: 'Outfit', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: var(--navy) !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: var(--muted) !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        color: var(--muted);
        border-bottom: 2px solid transparent;
    }
    
    .stTabs [aria-selected="true"] {
        color: var(--navy) !important;
        border-bottom-color: var(--navy) !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============ MOCK DATA (Same as React) ============

# KPI Data
kpi_data = {
    "workflow_count": {
        "value": 1247,
        "change": 12.5,
        "trend": "up",
        "label": "Total Workflows",
        "icon": "📊",
    },
    "volume_gearing_ratio": {
        "value": 2.45,
        "change": 8.3,
        "trend": "up",
        "label": "Volume Gearing Ratio",
        "icon": "📈",
    },
    "productivity": {
        "value": 87.3,
        "change": 5.2,
        "trend": "up",
        "label": "Productivity Score",
        "icon": "👥",
    },
    "tech_adoption": {
        "value": 76.8,
        "change": -2.1,
        "trend": "down",
        "label": "Tech Adoption Rate",
        "icon": "💻",
    },
}

# Workflow Trend Data
workflow_trend_data = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        "Completed": [145, 162, 178, 195, 210, 225, 198, 235, 248, 262, 278, 290],
        "Pending": [23, 18, 25, 20, 15, 22, 28, 19, 16, 21, 17, 24],
        "Failed": [5, 8, 4, 6, 3, 7, 9, 4, 5, 6, 3, 8],
    }
)

# Volume Gearing Data
volume_gearing_data = pd.DataFrame(
    {
        "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
        "Ratio": [2.12, 2.28, 2.35, 2.45],
        "Volume": [485000, 512000, 548000, 592000],
        "Benchmark": [2.0, 2.1, 2.15, 2.2],
    }
)

# Productivity Data
productivity_data = pd.DataFrame(
    {
        "Department": [
            "Engineering",
            "Sales",
            "Marketing",
            "Operations",
            "Finance",
            "HR",
        ],
        "Score": [92.5, 88.2, 85.7, 91.3, 89.1, 83.4],
        "Target": [90, 85, 82, 88, 87, 80],
        "Employees": [45, 32, 18, 28, 15, 12],
    }
)

# Tech Adoption Data
tech_adoption_data = pd.DataFrame(
    {
        "Tool": [
            "CRM System",
            "Project Management",
            "Analytics Platform",
            "Collaboration Suite",
            "AI Assistant",
            "Automation Tools",
            "Cloud Storage",
            "Security Tools",
        ],
        "Adoption": [94, 89, 76, 92, 45, 68, 98, 85],
        "Category": [
            "Core",
            "Core",
            "Analytics",
            "Communication",
            "Emerging",
            "Process",
            "Core",
            "Security",
        ],
    }
)

# Department Breakdown
department_breakdown = pd.DataFrame(
    {
        "Department": ["Engineering", "Sales", "Marketing", "Operations", "Other"],
        "Value": [35, 25, 15, 15, 10],
    }
)

# Recent Workflows
recent_workflows = pd.DataFrame(
    {
        "ID": [
            "WF-001",
            "WF-002",
            "WF-003",
            "WF-004",
            "WF-005",
            "WF-006",
            "WF-007",
            "WF-008",
        ],
        "Workflow Name": [
            "Customer Onboarding",
            "Invoice Processing",
            "Lead Qualification",
            "Support Ticket Routing",
            "Employee Onboarding",
            "Report Generation",
            "Data Sync",
            "Contract Review",
        ],
        "Department": [
            "Sales",
            "Finance",
            "Marketing",
            "Operations",
            "HR",
            "Engineering",
            "Engineering",
            "Legal",
        ],
        "Status": [
            "Completed",
            "Completed",
            "Pending",
            "Completed",
            "Failed",
            "Completed",
            "Pending",
            "Completed",
        ],
        "Duration": [
            "2h 15m",
            "45m",
            "1h 30m",
            "15m",
            "3h 45m",
            "30m",
            "55m",
            "4h 20m",
        ],
        "Date": [
            "2024-12-15",
            "2024-12-15",
            "2024-12-14",
            "2024-12-14",
            "2024-12-13",
            "2024-12-13",
            "2024-12-12",
            "2024-12-12",
        ],
    }
)

# Executive Summaries
executive_summaries = [
    {
        "title": "Operational Excellence",
        "content": "Workflow completion rates have increased by 12.5% compared to last quarter, driven primarily by process automation initiatives in the Engineering and Operations departments. The average workflow duration has decreased by 18%, indicating improved efficiency across all business units.",
        "metric": "+12.5%",
        "metric_label": "Workflow Efficiency",
        "icon": "📈",
    },
    {
        "title": "Financial Performance",
        "content": "Volume gearing ratio has improved to 2.45, exceeding the industry benchmark of 2.2. This indicates optimal resource utilization and scalable growth patterns. Operating leverage continues to strengthen as automation reduces variable costs.",
        "metric": "2.45",
        "metric_label": "Gearing Ratio",
        "icon": "💰",
    },
    {
        "title": "Workforce Productivity",
        "content": "Overall productivity score stands at 87.3%, with Engineering leading at 92.5%. Cross-departmental collaboration initiatives have contributed to a 5.2% increase in overall productivity metrics. Focus areas include Marketing and HR departments.",
        "metric": "87.3%",
        "metric_label": "Avg Productivity",
        "icon": "👥",
    },
    {
        "title": "Technology Transformation",
        "content": "Core technology adoption remains strong at 90%+, while emerging technologies like AI assistants show 45% adoption. Priority focus on AI integration training programs expected to boost adoption rates by 20% in Q1 2025.",
        "metric": "76.8%",
        "metric_label": "Tech Adoption",
        "icon": "💻",
    },
]

# Monthly Performance
monthly_performance = pd.DataFrame(
    {
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        "Revenue": [
            125000,
            132000,
            145000,
            152000,
            168000,
            175000,
            162000,
            185000,
            198000,
            210000,
            225000,
            242000,
        ],
        "Costs": [
            98000,
            102000,
            108000,
            112000,
            118000,
            122000,
            115000,
            128000,
            135000,
            142000,
            148000,
            155000,
        ],
        "Profit": [
            27000,
            30000,
            37000,
            40000,
            50000,
            53000,
            47000,
            57000,
            63000,
            68000,
            77000,
            87000,
        ],
    }
)

# ============ CHART COLORS (Same as React) ============
NAVY = "#0F172A"
NAVY_LIGHT = "#1E293B"
BLUE = "#3B82F6"
CYAN = "#0EA5E9"
SLATE = "#94A3B8"
AMBER = "#D97706"
SUCCESS = "#10B981"
WARNING = "#F59E0B"
ERROR = "#EF4444"

chart_colors = [NAVY, BLUE, CYAN, SLATE, AMBER]

# ============ COMPONENT FUNCTIONS ============


def render_kpi_card(label, value, change, trend, format_type="number", icon="📊"):
    """Render KPI card matching React design"""
    if format_type == "percentage":
        display_value = f"{value}%"
    elif format_type == "ratio":
        display_value = f"{value:.2f}"
    elif format_type == "currency":
        display_value = f"${value:,.0f}"
    else:
        display_value = f"{value:,}"

    icon_class = "kpi-icon-up" if trend == "up" else "kpi-icon-down"
    change_class = "kpi-change-positive" if trend == "up" else "kpi-change-negative"
    change_icon = "↑" if trend == "up" else "↓"

    st.markdown(
        f"""
    <div class="kpi-card animate-fade-in">
        <div class="kpi-icon {icon_class}">{icon}</div>
        <div class="kpi-value">{display_value}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-change {change_class}">
            {change_icon} {abs(change)}% <span style="font-weight: normal; opacity: 0.75; margin-left: 4px;">vs last period</span>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chart_card(title, subtitle=""):
    """Render chart card header"""
    st.markdown(
        f"""
    <div class="chart-card-header">
        <div class="chart-card-title">{title}</div>
        <div class="chart-card-subtitle">{subtitle}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_summary_card(summary):
    """Render executive summary card"""
    st.markdown(
        f"""
    <div class="summary-card">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
            <span style="font-size: 1.25rem;">{summary["icon"]}</span>
            <span class="summary-card-title">{summary["title"]}</span>
        </div>
        <p class="summary-card-content">{summary["content"]}</p>
        <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);">
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700;">{summary["metric"]}</div>
            <div style="font-size: 0.75rem; opacity: 0.7; margin-top: 0.25rem;">{summary["metric_label"]}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============ CHART FUNCTIONS ============


def create_workflow_bar_chart(data):
    """Create workflow trends bar chart"""
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="Completed", x=data["Month"], y=data["Completed"], marker_color=NAVY
        )
    )
    fig.add_trace(
        go.Bar(name="Pending", x=data["Month"], y=data["Pending"], marker_color=BLUE)
    )
    fig.add_trace(
        go.Bar(name="Failed", x=data["Month"], y=data["Failed"], marker_color=ERROR)
    )
    fig.update_layout(
        barmode="group",
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=11),
        ),
        margin=dict(l=40, r=20, t=40, b=40),
        xaxis=dict(gridcolor="#E2E8F0", showgrid=False),
        yaxis=dict(gridcolor="#E2E8F0", gridwidth=1),
        bargap=0.15,
        bargroupgap=0.1,
    )
    return fig


def create_department_pie_chart(data):
    """Create department distribution donut chart"""
    fig = go.Figure(
        data=[
            go.Pie(
                labels=data["Department"],
                values=data["Value"],
                hole=0.5,
                marker=dict(colors=chart_colors),
                textposition="outside",
                textinfo="label+percent",
                textfont=dict(size=11, family="Inter, sans-serif"),
            )
        ]
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
    )
    return fig


def create_gearing_area_chart(data):
    """Create volume gearing ratio area chart with benchmark"""
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Ratio"],
            name="Gearing Ratio",
            fill="tozeroy",
            fillcolor="rgba(15, 23, 42, 0.15)",
            line=dict(color=NAVY, width=3),
            mode="lines+markers",
            marker=dict(size=8),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Benchmark"],
            name="Benchmark",
            line=dict(color=AMBER, width=2, dash="dash"),
            mode="lines+markers",
            marker=dict(size=6),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=40, r=20, t=40, b=40),
        xaxis=dict(gridcolor="#E2E8F0", showgrid=False),
        yaxis=dict(gridcolor="#E2E8F0", range=[0, 3]),
    )
    return fig


def create_productivity_bar_chart(data):
    """Create horizontal productivity comparison chart"""
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="Score",
            y=data["Department"],
            x=data["Score"],
            orientation="h",
            marker_color=NAVY,
        )
    )
    fig.add_trace(
        go.Bar(
            name="Target",
            y=data["Department"],
            x=data["Target"],
            orientation="h",
            marker_color=AMBER,
        )
    )
    fig.update_layout(
        barmode="group",
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=100, r=20, t=40, b=40),
        xaxis=dict(gridcolor="#E2E8F0", range=[0, 100]),
        yaxis=dict(gridcolor="#E2E8F0", showgrid=False),
        bargap=0.3,
    )
    return fig


def create_tech_adoption_chart(data):
    """Create tech adoption bar chart with color coding"""
    colors = [
        SUCCESS if a >= 80 else NAVY if a >= 60 else ERROR for a in data["Adoption"]
    ]
    fig = go.Figure(
        go.Bar(
            x=data["Tool"],
            y=data["Adoption"],
            marker_color=colors,
            text=data["Adoption"].astype(str) + "%",
            textposition="outside",
            textfont=dict(size=10),
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        margin=dict(l=40, r=20, t=40, b=100),
        xaxis=dict(gridcolor="#E2E8F0", tickangle=-45, showgrid=False),
        yaxis=dict(gridcolor="#E2E8F0", range=[0, 110]),
    )
    return fig


def create_performance_area_chart(data):
    """Create revenue/profit area chart"""
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Revenue"],
            name="Revenue",
            fill="tozeroy",
            fillcolor="rgba(15, 23, 42, 0.15)",
            line=dict(color=NAVY, width=2),
            mode="lines",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Profit"],
            name="Profit",
            fill="tozeroy",
            fillcolor="rgba(16, 185, 129, 0.15)",
            line=dict(color=SUCCESS, width=2),
            mode="lines",
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=60, r=20, t=40, b=40),
        xaxis=dict(gridcolor="#E2E8F0", showgrid=False),
        yaxis=dict(gridcolor="#E2E8F0", tickformat="$,.0f"),
    )
    return fig


def create_line_chart(data, x_col, y_col, name, color=NAVY):
    """Create simple line chart"""
    fig = go.Figure(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            name=name,
            mode="lines+markers",
            line=dict(color=color, width=3),
            marker=dict(size=8, color=color),
            fill="tozeroy",
            fillcolor=f"rgba{tuple(int(color.lstrip('#')[i : i + 2], 16) for i in (0, 2, 4)) + (0.1,)}",
        )
    )
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(family="Inter, sans-serif", size=12, color="#64748B"),
        margin=dict(l=40, r=20, t=20, b=40),
        xaxis=dict(gridcolor="#E2E8F0", showgrid=False),
        yaxis=dict(gridcolor="#E2E8F0"),
    )
    return fig


# ============ PDF/REPORT GENERATION ============


def generate_html_report():
    """Generate comprehensive HTML report for download"""
    current_date = datetime.now().strftime("%B %d, %Y")

    # Build productivity table rows
    prod_rows = ""
    for _, row in productivity_data.iterrows():
        status = "On Target" if row["Score"] >= row["Target"] else "Below Target"
        status_color = "#166534" if row["Score"] >= row["Target"] else "#92400E"
        prod_rows += f"""
        <tr>
            <td style="font-weight: 500;">{row["Department"]}</td>
            <td style="font-family: 'JetBrains Mono', monospace; font-weight: 600;">{row["Score"]}%</td>
            <td style="font-family: 'JetBrains Mono', monospace; color: #64748B;">{row["Target"]}%</td>
            <td><span style="background: {"#DCFCE7" if status == "On Target" else "#FEF3C7"}; color: {status_color}; padding: 4px 12px; border-radius: 9999px; font-size: 11px; font-weight: 600;">{status}</span></td>
            <td>{row["Employees"]}</td>
        </tr>
        """

    # Build tech adoption table rows
    tech_rows = ""
    for _, row in tech_adoption_data.iterrows():
        tech_rows += f"""
        <tr>
            <td style="font-weight: 500;">{row["Tool"]}</td>
            <td><span style="background: #0F172A; color: white; padding: 4px 12px; border-radius: 9999px; font-size: 11px;">{row["Category"]}</span></td>
            <td style="font-family: 'JetBrains Mono', monospace; font-weight: 600;">{row["Adoption"]}%</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>BizView Executive Dashboard Report</title>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Inter:wght@400;500&family=JetBrains+Mono&display=swap" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Inter', sans-serif; color: #0F172A; line-height: 1.6; background: #F8FAFC; }}
            .container {{ max-width: 1000px; margin: 0 auto; padding: 40px; background: white; }}
            h1, h2, h3 {{ font-family: 'Outfit', sans-serif; }}
            h1 {{ font-size: 28px; font-weight: 700; }}
            h2 {{ font-size: 18px; font-weight: 600; margin: 30px 0 15px 0; color: #0F172A; }}
            
            .header {{ border-bottom: 3px solid #0F172A; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: flex-start; }}
            .header-left p {{ color: #64748B; margin-top: 5px; }}
            .header-right {{ text-align: right; }}
            .header-right p {{ color: #64748B; font-size: 14px; }}
            .header-right strong {{ color: #0F172A; }}
            
            .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-bottom: 40px; }}
            .kpi-box {{ background: #F8FAFC; padding: 20px; border-radius: 8px; text-align: center; }}
            .kpi-value {{ font-family: 'Outfit', sans-serif; font-size: 28px; font-weight: 700; color: #0F172A; }}
            .kpi-label {{ color: #64748B; font-size: 13px; margin-top: 5px; }}
            .kpi-change {{ font-size: 12px; margin-top: 8px; font-weight: 600; }}
            .kpi-change.positive {{ color: #166534; }}
            .kpi-change.negative {{ color: #991B1B; }}
            
            table {{ width: 100%; border-collapse: collapse; margin: 15px 0 30px 0; }}
            th {{ background: #F8FAFC; text-align: left; padding: 12px 16px; border-bottom: 2px solid #E2E8F0; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: #64748B; font-weight: 600; }}
            td {{ padding: 14px 16px; border-bottom: 1px solid #F1F5F9; font-size: 14px; }}
            tr:hover td {{ background: #F8FAFC; }}
            
            .summary-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin: 20px 0; }}
            .summary-box {{ background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); color: white; padding: 24px; border-radius: 8px; }}
            .summary-title {{ color: #D97706; font-family: 'Outfit', sans-serif; font-weight: 600; margin-bottom: 12px; }}
            .summary-content {{ font-size: 14px; line-height: 1.7; opacity: 0.9; }}
            .summary-metric {{ margin-top: 20px; padding-top: 15px; border-top: 1px solid rgba(255,255,255,0.1); }}
            .summary-metric-value {{ font-family: 'Outfit', sans-serif; font-size: 24px; font-weight: 700; }}
            .summary-metric-label {{ font-size: 12px; opacity: 0.7; margin-top: 4px; }}
            
            .footer {{ text-align: center; color: #64748B; font-size: 12px; margin-top: 40px; padding-top: 20px; border-top: 1px solid #E2E8F0; }}
            
            @media print {{
                body {{ background: white; }}
                .container {{ padding: 20px; }}
                .kpi-grid {{ grid-template-columns: repeat(4, 1fr); }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <div class="header-left">
                    <h1>📊 Executive Dashboard Report</h1>
                    <p>BizView Analytics Platform</p>
                </div>
                <div class="header-right">
                    <p>Report Generated</p>
                    <p><strong>{current_date}</strong></p>
                </div>
            </div>
            
            <h2>Key Performance Indicators</h2>
            <div class="kpi-grid">
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["workflow_count"]["value"]:,}</div>
                    <div class="kpi-label">Total Workflows</div>
                    <div class="kpi-change positive">↑ {kpi_data["workflow_count"]["change"]}%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["volume_gearing_ratio"]["value"]}</div>
                    <div class="kpi-label">Gearing Ratio</div>
                    <div class="kpi-change positive">↑ {kpi_data["volume_gearing_ratio"]["change"]}%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["productivity"]["value"]}%</div>
                    <div class="kpi-label">Productivity</div>
                    <div class="kpi-change positive">↑ {kpi_data["productivity"]["change"]}%</div>
                </div>
                <div class="kpi-box">
                    <div class="kpi-value">{kpi_data["tech_adoption"]["value"]}%</div>
                    <div class="kpi-label">Tech Adoption</div>
                    <div class="kpi-change negative">↓ {abs(kpi_data["tech_adoption"]["change"])}%</div>
                </div>
            </div>
            
            <h2>Department Productivity</h2>
            <table>
                <thead>
                    <tr><th>Department</th><th>Score</th><th>Target</th><th>Status</th><th>Employees</th></tr>
                </thead>
                <tbody>{prod_rows}</tbody>
            </table>
            
            <h2>Technology Adoption</h2>
            <table>
                <thead>
                    <tr><th>Tool</th><th>Category</th><th>Adoption Rate</th></tr>
                </thead>
                <tbody>{tech_rows}</tbody>
            </table>
            
            <h2>Executive Summaries</h2>
            <div class="summary-grid">
                <div class="summary-box">
                    <div class="summary-title">📈 {executive_summaries[0]["title"]}</div>
                    <div class="summary-content">{executive_summaries[0]["content"]}</div>
                    <div class="summary-metric">
                        <div class="summary-metric-value">{executive_summaries[0]["metric"]}</div>
                        <div class="summary-metric-label">{executive_summaries[0]["metric_label"]}</div>
                    </div>
                </div>
                <div class="summary-box">
                    <div class="summary-title">💰 {executive_summaries[1]["title"]}</div>
                    <div class="summary-content">{executive_summaries[1]["content"]}</div>
                    <div class="summary-metric">
                        <div class="summary-metric-value">{executive_summaries[1]["metric"]}</div>
                        <div class="summary-metric-label">{executive_summaries[1]["metric_label"]}</div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>Generated by BizView Analytics Platform | Confidential</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html


# ============ SESSION STATE ============
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ============ SIDEBAR ============
with st.sidebar:
    # Logo Header
    st.markdown(
        """
    <div style="padding: 1.5rem 1.5rem 1rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <div style="display: flex; align-items: center; gap: 12px;">
            <span style="font-size: 28px;">📊</span>
            <span style="font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.25rem; color: white;">BizView</span>
        </div>
        <p style="font-size: 12px; color: rgba(255,255,255,0.5); margin-top: 8px;">Executive Analytics</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    # Navigation
    nav_items = [
        ("📊", "Dashboard"),
        ("🔄", "Workflow Analytics"),
        ("💰", "Financial Metrics"),
        ("👥", "Productivity"),
        ("💻", "Tech Adoption"),
        ("📋", "Executive Summary"),
        ("📥", "Reports & Export"),
    ]

    for icon, name in nav_items:
        btn_type = "primary" if st.session_state.current_page == name else "secondary"
        if st.button(
            f"{icon}  {name}",
            key=f"nav_{name}",
            type=btn_type,
            use_container_width=True,
        ):
            st.session_state.current_page = name
            st.rerun()

    st.markdown(
        "<hr style='margin: 1.5rem 0; border-color: rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

    # Filters Section
    st.markdown(
        "<p style='font-size: 11px; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.5); margin-bottom: 0.75rem; padding: 0 1.5rem;'>Filters</p>",
        unsafe_allow_html=True,
    )

    department = st.selectbox(
        "Department",
        [
            "All Departments",
            "Engineering",
            "Sales",
            "Marketing",
            "Operations",
            "Finance",
            "HR",
        ],
        key="filter_dept",
    )
    date_range = st.selectbox(
        "Date Range",
        ["Last 30 Days", "Last 7 Days", "Last 90 Days", "Year to Date"],
        key="filter_date",
    )
    status = st.selectbox(
        "Status", ["All Status", "Completed", "Pending", "Failed"], key="filter_status"
    )

    st.markdown(
        "<hr style='margin: 1.5rem 0; border-color: rgba(255,255,255,0.1);'>",
        unsafe_allow_html=True,
    )

    # Footer
    st.markdown(
        """
    <div style="padding: 0 1.5rem; color: rgba(255,255,255,0.4); font-size: 12px;">
        <p>⚙️ Settings</p>
        <p style="margin-top: 0.5rem;">v1.0.0</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============ MAIN CONTENT AREA ============

# Header Bar
col_header, col_actions = st.columns([3, 1])
with col_header:
    st.markdown(
        f"<h1 style='margin: 0; padding: 0;'>{st.session_state.current_page}</h1>",
        unsafe_allow_html=True,
    )
with col_actions:
    col_print, col_download = st.columns(2)
    with col_print:
        if st.button("🖨️ Print", use_container_width=True, key="print_btn"):
            st.toast("Use Ctrl+P / Cmd+P to print", icon="🖨️")
    with col_download:
        html_report = generate_html_report()
        st.download_button(
            "📥 Download",
            data=html_report,
            file_name=f"BizView_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
        )

st.markdown("<hr style='margin: 1rem 0 1.5rem 0;'>", unsafe_allow_html=True)

# ============ PAGE: DASHBOARD ============
if st.session_state.current_page == "Dashboard":
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            kpi_data["workflow_count"]["label"],
            kpi_data["workflow_count"]["value"],
            kpi_data["workflow_count"]["change"],
            kpi_data["workflow_count"]["trend"],
            "number",
            "📊",
        )
    with col2:
        render_kpi_card(
            kpi_data["volume_gearing_ratio"]["label"],
            kpi_data["volume_gearing_ratio"]["value"],
            kpi_data["volume_gearing_ratio"]["change"],
            kpi_data["volume_gearing_ratio"]["trend"],
            "ratio",
            "📈",
        )
    with col3:
        render_kpi_card(
            kpi_data["productivity"]["label"],
            kpi_data["productivity"]["value"],
            kpi_data["productivity"]["change"],
            kpi_data["productivity"]["trend"],
            "percentage",
            "👥",
        )
    with col4:
        render_kpi_card(
            kpi_data["tech_adoption"]["label"],
            kpi_data["tech_adoption"]["value"],
            kpi_data["tech_adoption"]["change"],
            kpi_data["tech_adoption"]["trend"],
            "percentage",
            "💻",
        )

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    # Charts Row 1
    col_chart1, col_chart2 = st.columns([2, 1])
    with col_chart1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("WORKFLOW TRENDS", "Monthly workflow completion rates")
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            use_container_width=True,
            key="wf_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col_chart2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("DEPARTMENT DISTRIBUTION", "Workflow allocation by team")
        st.plotly_chart(
            create_department_pie_chart(department_breakdown),
            use_container_width=True,
            key="dept_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Charts Row 2
    col_chart3, col_chart4 = st.columns(2)
    with col_chart3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("MONTHLY PERFORMANCE", "Revenue vs Profit trend")
        st.plotly_chart(
            create_performance_area_chart(monthly_performance),
            use_container_width=True,
            key="perf_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col_chart4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("COMPLETION RATE TREND", "Workflow completion over time")
        st.plotly_chart(
            create_line_chart(workflow_trend_data, "Month", "Completed", "Completed"),
            use_container_width=True,
            key="trend_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Executive Summaries
    st.markdown("### Executive Summaries")
    col_sum1, col_sum2 = st.columns(2)
    with col_sum1:
        render_summary_card(executive_summaries[0])
    with col_sum2:
        render_summary_card(executive_summaries[1])

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    # Recent Workflows Table
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_card("RECENT WORKFLOWS", "Latest workflow executions")
    st.dataframe(recent_workflows, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============ PAGE: WORKFLOW ANALYTICS ============
elif st.session_state.current_page == "Workflow Analytics":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Workflows", 1247, 12.5, "up", "number", "📊")
    with col2:
        render_kpi_card("Completed", 1098, 15.2, "up", "number", "✅")
    with col3:
        render_kpi_card("Pending", 89, -8.3, "up", "number", "⏳")
    with col4:
        render_kpi_card("Failed", 60, -12.1, "up", "number", "❌")

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("WORKFLOW STATUS DISTRIBUTION", "Monthly breakdown by status")
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            use_container_width=True,
            key="wf_status",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("COMPLETION TREND", "Workflows completed over time")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data, "Month", "Completed", "Completed", SUCCESS
            ),
            use_container_width=True,
            key="wf_trend",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_card("WORKFLOW DETAILS", "Complete workflow execution log")
    st.dataframe(recent_workflows, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============ PAGE: FINANCIAL METRICS ============
elif st.session_state.current_page == "Financial Metrics":
    total_revenue = monthly_performance["Revenue"].sum()
    total_profit = monthly_performance["Profit"].sum()
    profit_margin = total_profit / total_revenue * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Volume Gearing Ratio", 2.45, 8.3, "up", "ratio", "📈")
    with col2:
        render_kpi_card("Annual Revenue", total_revenue, 18.5, "up", "currency", "💰")
    with col3:
        render_kpi_card("Annual Profit", total_profit, 24.2, "up", "currency", "📊")
    with col4:
        render_kpi_card(
            "Profit Margin", round(profit_margin, 1), 5.8, "up", "percentage", "📉"
        )

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card(
            "VOLUME GEARING RATIO TREND", "Quarterly performance vs benchmark"
        )
        st.plotly_chart(
            create_gearing_area_chart(volume_gearing_data),
            use_container_width=True,
            key="gearing",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("REVENUE BY DEPARTMENT", "Department contribution")
        st.plotly_chart(
            create_department_pie_chart(department_breakdown),
            use_container_width=True,
            key="rev_dept",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_card("MONTHLY FINANCIAL PERFORMANCE", "Revenue and profit trends")
    st.plotly_chart(
        create_performance_area_chart(monthly_performance),
        use_container_width=True,
        key="fin_perf",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_card("QUARTERLY FINANCIAL SUMMARY", "Volume and gearing metrics")
    display_df = volume_gearing_data.copy()
    display_df["Variance"] = (
        (display_df["Ratio"] - display_df["Benchmark"]) / display_df["Benchmark"] * 100
    ).round(1).astype(str) + "%"
    display_df["Volume"] = display_df["Volume"].apply(lambda x: f"${x:,}")
    st.dataframe(display_df, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ============ PAGE: PRODUCTIVITY ============
elif st.session_state.current_page == "Productivity":
    avg_score = productivity_data["Score"].mean()
    on_target = (productivity_data["Score"] >= productivity_data["Target"]).sum()
    total_employees = productivity_data["Employees"].sum()
    top_performer = productivity_data.loc[productivity_data["Score"].idxmax()]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Productivity Score", round(avg_score, 1), 5.2, "up", "percentage", "📈"
        )
    with col2:
        render_kpi_card("Teams on Target", on_target, 16.7, "up", "number", "🎯")
    with col3:
        render_kpi_card("Total Employees", total_employees, 8.4, "up", "number", "👥")
    with col4:
        render_kpi_card(
            "Top Performer", top_performer["Score"], 3.1, "up", "percentage", "🏆"
        )

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("DEPARTMENT PRODUCTIVITY", "Score vs Target by department")
        st.plotly_chart(
            create_productivity_bar_chart(productivity_data),
            use_container_width=True,
            key="prod_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("PRODUCTIVITY TREND", "Overall completion metrics")
        st.plotly_chart(
            create_line_chart(workflow_trend_data, "Month", "Completed", "Output"),
            use_container_width=True,
            key="prod_trend",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_card(
        "DEPARTMENT PERFORMANCE DETAILS", "Comprehensive productivity breakdown"
    )
    prod_display = productivity_data.copy()
    prod_display["Status"] = prod_display.apply(
        lambda x: "✅ On Target" if x["Score"] >= x["Target"] else "⚠️ Below Target",
        axis=1,
    )
    st.dataframe(prod_display, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Insight Cards
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>Top Performing Team</h4>
            <div class="insight-value" style="color: {NAVY};">{top_performer["Department"]}</div>
            <div class="insight-label">{top_performer["Score"]}% productivity score</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>Target Achievement</h4>
            <div class="insight-value" style="color: {SUCCESS};">{int(on_target / len(productivity_data) * 100)}%</div>
            <div class="insight-label">{on_target} of {len(productivity_data)} teams on target</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>Workforce Size</h4>
            <div class="insight-value" style="color: {BLUE};">{total_employees}</div>
            <div class="insight-label">Employees across all departments</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============ PAGE: TECH ADOPTION ============
elif st.session_state.current_page == "Tech Adoption":
    avg_adoption = tech_adoption_data["Adoption"].mean()
    high_adoption = (tech_adoption_data["Adoption"] >= 80).sum()
    low_adoption = (tech_adoption_data["Adoption"] < 60).sum()
    emerging = (tech_adoption_data["Category"] == "Emerging").sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Tech Adoption",
            round(avg_adoption, 1),
            -2.1,
            "down",
            "percentage",
            "💻",
        )
    with col2:
        render_kpi_card(
            "High Adoption Tools", high_adoption, 12.5, "up", "number", "✅"
        )
    with col3:
        render_kpi_card("Low Adoption Tools", low_adoption, -25.0, "up", "number", "⚠️")
    with col4:
        render_kpi_card("Emerging Tech", emerging, 100, "up", "number", "🚀")

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("TECH ADOPTION BY TOOL", "Adoption rates across all tools")
        st.plotly_chart(
            create_tech_adoption_chart(tech_adoption_data),
            use_container_width=True,
            key="tech_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        category_counts = (
            tech_adoption_data.groupby("Category").size().reset_index(name="Value")
        )
        category_counts.columns = ["Department", "Value"]
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_card("TOOLS BY CATEGORY", "Distribution of tech categories")
        st.plotly_chart(
            create_department_pie_chart(category_counts),
            use_container_width=True,
            key="cat_chart",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_card("TECHNOLOGY ADOPTION DETAILS", "Complete breakdown by tool")
    tech_display = tech_adoption_data.copy()
    tech_display["Status"] = tech_display["Adoption"].apply(
        lambda x: "🟢 High" if x >= 80 else "🟡 Medium" if x >= 60 else "🔴 Low"
    )
    st.dataframe(tech_display, use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Recommendations
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        low_tools = tech_adoption_data[tech_adoption_data["Adoption"] < 60]
        st.markdown(
            f"""
        <div class="summary-card">
            <div class="summary-card-title">⚠️ Focus Areas</div>
            <div style="margin-top: 1rem;">
                {"".join(f'<p style="font-size: 14px; margin: 8px 0; color: rgba(255,255,255,0.9);">• {row["Tool"]} - {row["Adoption"]}% adoption</p>' for _, row in low_tools.iterrows())}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    with col2:
        high_tools = tech_adoption_data[tech_adoption_data["Adoption"] >= 90]
        st.markdown(
            f"""
        <div class="insight-card">
            <h4 style="color: {NAVY};">✅ Top Performers</h4>
            <div style="margin-top: 0.5rem;">
                {"".join(f'<p style="font-size: 14px; margin: 8px 0; color: {SUCCESS};">• {row["Tool"]} - {row["Adoption"]}% adoption</p>' for _, row in high_tools.iterrows())}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# ============ PAGE: EXECUTIVE SUMMARY ============
elif st.session_state.current_page == "Executive Summary":
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    # Header Card
    st.markdown(
        f"""
    <div style="background: {NAVY}; color: white; border-radius: 0.5rem; padding: 2rem; margin-bottom: 2rem;">
        <p style="color: {AMBER}; font-size: 14px; margin-bottom: 10px;">📅 {current_date}</p>
        <h2 style="color: white; margin-bottom: 15px; font-size: 1.5rem;">Monthly Executive Report</h2>
        <p style="color: rgba(255,255,255,0.7); max-width: 800px; line-height: 1.6;">
            Comprehensive overview of organizational performance metrics, highlighting key achievements, 
            areas of improvement, and strategic recommendations for continued growth.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("📈", kpi_data["workflow_count"]["value"], "Total Workflows", NAVY),
        ("📄", kpi_data["volume_gearing_ratio"]["value"], "Gearing Ratio", BLUE),
        ("👥", f"{kpi_data['productivity']['value']}%", "Productivity", SUCCESS),
        ("💻", f"{kpi_data['tech_adoption']['value']}%", "Tech Adoption", AMBER),
    ]
    for col, (icon, value, label, color) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
            <div class="insight-card" style="text-align: center;">
                <span style="font-size: 1.5rem;">{icon}</span>
                <div class="insight-value" style="color: {color}; margin-top: 0.5rem;">{value if isinstance(value, str) else f"{value:,}"}</div>
                <div class="insight-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    # Executive Summaries Grid
    st.markdown("### Key Insights & Analysis")
    for i in range(0, 4, 2):
        col1, col2 = st.columns(2)
        with col1:
            render_summary_card(executive_summaries[i])
        with col2:
            if i + 1 < len(executive_summaries):
                render_summary_card(executive_summaries[i + 1])
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    # Recommendations
    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Strategic Priorities")
        priorities = [
            (
                "Accelerate AI Adoption",
                "Implement training programs to increase AI assistant adoption from 45% to 70%.",
            ),
            (
                "Scale Automation",
                "Expand workflow automation to reduce manual processing by 30%.",
            ),
            (
                "Department Alignment",
                "Focus on HR and Marketing departments to bring productivity above target.",
            ),
        ]
        for i, (title, desc) in enumerate(priorities, 1):
            st.markdown(
                f"""
            <div style="display: flex; gap: 15px; padding: 15px; background: #F8FAFC; border-radius: 8px; margin-bottom: 10px;">
                <div style="width: 32px; height: 32px; background: {NAVY}; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-weight: 700;">{i}</div>
                <div>
                    <h5 style="margin: 0; color: {NAVY}; font-size: 14px;">{title}</h5>
                    <p style="margin: 5px 0 0 0; color: #64748B; font-size: 13px;">{desc}</p>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with col2:
        st.markdown("### Key Achievements")
        achievements = [
            (
                "12.5% Workflow Growth",
                "Exceeded quarterly targets with significant efficiency gains.",
            ),
            (
                "Gearing Ratio Above Benchmark",
                "Achieved 2.45 vs 2.2 industry standard.",
            ),
            (
                "Engineering Excellence",
                "Engineering department achieved 92.5% productivity score.",
            ),
        ]
        for title, desc in achievements:
            st.markdown(
                f"""
            <div style="display: flex; gap: 15px; padding: 15px; background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 8px; margin-bottom: 10px;">
                <div style="width: 8px; height: 8px; background: {SUCCESS}; border-radius: 50%; margin-top: 6px; flex-shrink: 0;"></div>
                <div>
                    <h5 style="margin: 0; color: {NAVY}; font-size: 14px;">{title}</h5>
                    <p style="margin: 5px 0 0 0; color: #64748B; font-size: 13px;">{desc}</p>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

# ============ PAGE: REPORTS & EXPORT ============
elif st.session_state.current_page == "Reports & Export":
    st.markdown("### Export Options")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <div style="width: 48px; height: 48px; background: {NAVY}; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 24px;">📄</span>
                </div>
                <div>
                    <h4 style="margin: 0; color: {NAVY}; font-size: 16px;">Full Report</h4>
                    <p style="margin: 0; color: #64748B; font-size: 12px;">Complete dashboard PDF</p>
                </div>
            </div>
            <p style="color: #64748B; font-size: 14px;">Export the complete executive dashboard including all KPIs, charts, and data tables.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        html_report = generate_html_report()
        st.download_button(
            "📥 Download Full Report",
            data=html_report,
            file_name=f"BizView_Full_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
            key="dl_full",
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <div style="width: 48px; height: 48px; background: {BLUE}; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 24px;">📊</span>
                </div>
                <div>
                    <h4 style="margin: 0; color: {NAVY}; font-size: 16px;">Data Export</h4>
                    <p style="margin: 0; color: #64748B; font-size: 12px;">Excel spreadsheet</p>
                </div>
            </div>
            <p style="color: #64748B; font-size: 14px;">Export all data tables for further analysis and custom reporting.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            workflow_trend_data.to_excel(
                writer, sheet_name="Workflow Trends", index=False
            )
            productivity_data.to_excel(writer, sheet_name="Productivity", index=False)
            tech_adoption_data.to_excel(writer, sheet_name="Tech Adoption", index=False)
            monthly_performance.to_excel(writer, sheet_name="Financial", index=False)
            recent_workflows.to_excel(
                writer, sheet_name="Recent Workflows", index=False
            )

        st.download_button(
            "📥 Download Excel",
            data=buffer.getvalue(),
            file_name=f"BizView_Data_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
            key="dl_excel",
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card">
            <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 15px;">
                <div style="width: 48px; height: 48px; background: {SUCCESS}; border-radius: 8px; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 24px;">📋</span>
                </div>
                <div>
                    <h4 style="margin: 0; color: {NAVY}; font-size: 16px;">CSV Export</h4>
                    <p style="margin: 0; color: #64748B; font-size: 12px;">Raw data files</p>
                </div>
            </div>
            <p style="color: #64748B; font-size: 14px;">Export individual datasets as CSV for integration with other tools.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.download_button(
            "📥 Download CSV",
            data=productivity_data.to_csv(index=False),
            file_name=f"BizView_Productivity_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True,
            key="dl_csv",
        )

    st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)

    # Report Preview
    st.markdown("### Report Preview")
    current_date = datetime.now().strftime("%B %d, %Y")

    st.markdown(
        f"""
    <div style="background: white; border: 1px solid #E2E8F0; border-radius: 8px; padding: 2rem;">
        <div style="border-bottom: 3px solid {NAVY}; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between;">
            <div>
                <h2 style="color: {NAVY}; margin: 0; font-size: 1.5rem;">📊 Executive Dashboard Report</h2>
                <p style="color: #64748B; margin-top: 5px;">BizView Analytics Platform</p>
            </div>
            <div style="text-align: right;">
                <p style="color: #64748B; font-size: 14px;">Report Generated</p>
                <p style="color: {NAVY}; font-weight: 600;">{current_date}</p>
            </div>
        </div>
        
        <h3 style="color: {NAVY}; font-size: 1rem; margin-bottom: 1rem;">Key Performance Indicators</h3>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin-bottom: 2rem;">
            <div style="background: #F8FAFC; padding: 15px; border-radius: 8px; text-align: center;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; color: {NAVY}; margin: 0;">1,247</p>
                <p style="color: #64748B; font-size: 12px; margin: 5px 0 0 0;">Total Workflows</p>
                <p style="color: #166534; font-size: 11px; margin: 3px 0 0 0;">↑ 12.5%</p>
            </div>
            <div style="background: #F8FAFC; padding: 15px; border-radius: 8px; text-align: center;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; color: {NAVY}; margin: 0;">2.45</p>
                <p style="color: #64748B; font-size: 12px; margin: 5px 0 0 0;">Gearing Ratio</p>
                <p style="color: #166534; font-size: 11px; margin: 3px 0 0 0;">↑ 8.3%</p>
            </div>
            <div style="background: #F8FAFC; padding: 15px; border-radius: 8px; text-align: center;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; color: {NAVY}; margin: 0;">87.3%</p>
                <p style="color: #64748B; font-size: 12px; margin: 5px 0 0 0;">Productivity</p>
                <p style="color: #166534; font-size: 11px; margin: 3px 0 0 0;">↑ 5.2%</p>
            </div>
            <div style="background: #F8FAFC; padding: 15px; border-radius: 8px; text-align: center;">
                <p style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 700; color: {NAVY}; margin: 0;">76.8%</p>
                <p style="color: #64748B; font-size: 12px; margin: 5px 0 0 0;">Tech Adoption</p>
                <p style="color: #991B1B; font-size: 11px; margin: 3px 0 0 0;">↓ 2.1%</p>
            </div>
        </div>
        
        <p style="text-align: center; color: #64748B; font-size: 12px; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #E2E8F0;">
            Generated by BizView Analytics Platform | Confidential
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )
