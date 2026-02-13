"""
BizView Executive Dashboard - Professional Clean Edition
Modern, Efficient, and Beautiful
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime
import io

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
# CLEAN PROFESSIONAL CSS
# ============================================================================
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700&display=swap');

    /* ========== GLOBAL STYLES ========== */
    * {
        margin: 0;
        padding: 0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Hide Streamlit Branding */
    #MainMenu, footer, header, .stDeployButton {display: none !important;}
    
    /* ========== MAIN APP - CLEAN WHITE ========== */
    .stApp {
        background: #ffffff !important;
    }

    .main .block-container {
        padding: 1.5rem 2rem !important;
        max-width: 1600px !important;
    }

    /* ========== SIDEBAR - PERFECT DARK NAVY ========== */
    [data-testid="stSidebar"] {
        background: #0a1929 !important;
        border-right: none !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding: 1.5rem 1rem;
    }

    /* Sidebar Text Colors */
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: rgba(255, 255, 255, 0.85) !important;
    }

    /* Sidebar Buttons */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: transparent !important;
        color: rgba(255, 255, 255, 0.7) !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 1rem !important;
        margin: 0.25rem 0 !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        text-align: left !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        color: white !important;
    }

    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: rgba(59, 130, 246, 0.15) !important;
        color: white !important;
        font-weight: 600 !important;
        border-left: 3px solid #3b82f6 !important;
        border-radius: 0 8px 8px 0 !important;
    }

    /* Sidebar Divider */
    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.1) !important;
        margin: 1rem 0 !important;
    }

    /* ========== TYPOGRAPHY ========== */
    h1, h2, h3, h4 {
        font-family: 'Poppins', sans-serif !important;
        color: #1a202c !important;
        font-weight: 700 !important;
    }

    h1 { font-size: 1.75rem !important; margin-bottom: 0.5rem !important; }
    h2 { font-size: 1.5rem !important; margin-bottom: 0.5rem !important; }
    h3 { font-size: 1.25rem !important; margin-bottom: 0.75rem !important; }
    h4 { font-size: 1rem !important; }

    p {
        color: #64748b !important;
        line-height: 1.6 !important;
    }

    /* ========== KPI CARDS - CLEAN & COMPACT ========== */
    .kpi-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        height: 100%;
    }

    .kpi-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        transform: translateY(-2px);
        border-color: #cbd5e1;
    }

    .kpi-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 0.75rem;
    }

    .kpi-icon {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
    }

    .kpi-icon.success { background: #dcfce7; }
    .kpi-icon.warning { background: #fef3c7; }
    .kpi-icon.info { background: #dbeafe; }
    .kpi-icon.error { background: #fee2e2; }

    .kpi-value {
        font-family: 'Poppins', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #1a202c !important;
        line-height: 1 !important;
        margin: 0.5rem 0 !important;
    }

    .kpi-label {
        font-size: 0.875rem;
        color: #64748b;
        font-weight: 500;
    }

    .kpi-change {
        display: inline-flex;
        align-items: center;
        gap: 0.25rem;
        padding: 0.25rem 0.625rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }

    .kpi-change.positive {
        background: #dcfce7;
        color: #166534;
    }

    .kpi-change.negative {
        background: #fee2e2;
        color: #991b1b;
    }

    /* ========== CHART CARDS - CLEAN DESIGN ========== */
    .chart-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
    }

    .chart-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    .chart-header {
        padding: 1rem 1.25rem;
        border-bottom: 1px solid #f1f5f9;
        background: #fafbfc;
    }

    .chart-title {
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 700 !important;
        color: #1a202c !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .chart-subtitle {
        font-size: 0.75rem;
        color: #64748b;
        margin-top: 0.25rem;
    }

    /* ========== SUMMARY CARDS ========== */
    .summary-card {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-radius: 12px;
        padding: 1.5rem;
        color: white;
        height: 100%;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .summary-icon {
        font-size: 2rem;
        margin-bottom: 0.75rem;
    }

    .summary-title {
        font-size: 1rem;
        font-weight: 700;
        color: #fbbf24;
        margin-bottom: 0.75rem;
    }

    .summary-content {
        font-size: 0.875rem;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.85);
        margin-bottom: 1rem;
    }

    .summary-metric {
        font-size: 1.75rem;
        font-weight: 700;
        color: white;
    }

    .summary-label {
        font-size: 0.75rem;
        color: rgba(255, 255, 255, 0.6);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* ========== INSIGHT CARDS ========== */
    .insight-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        height: 100%;
    }

    .insight-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        border-color: #cbd5e1;
    }

    .insight-label {
        font-size: 0.75rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .insight-value {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #1a202c;
        line-height: 1;
    }

    .insight-desc {
        font-size: 0.875rem;
        color: #64748b;
        margin-top: 0.5rem;
    }

    /* ========== DATA TABLES ========== */
    .dataframe {
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        overflow: hidden !important;
    }

    .dataframe thead tr th {
        background: #f8fafc !important;
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 0.75rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        padding: 0.75rem 1rem !important;
        border-bottom: 2px solid #e2e8f0 !important;
    }

    .dataframe tbody tr td {
        padding: 0.75rem 1rem !important;
        border-bottom: 1px solid #f1f5f9 !important;
        font-size: 0.875rem !important;
    }

    .dataframe tbody tr:hover {
        background: #f8fafc !important;
    }

    /* ========== BUTTONS ========== */
    .stButton > button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.625rem 1.25rem !important;
        transition: all 0.2s ease !important;
    }

    .stDownloadButton > button {
        background: #0a1929 !important;
        color: white !important;
        border: none !important;
    }

    .stDownloadButton > button:hover {
        background: #1e293b !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15) !important;
    }

    /* ========== SPACING UTILITIES ========== */
    .spacing-sm { margin-bottom: 1rem; }
    .spacing-md { margin-bottom: 1.5rem; }
    .spacing-lg { margin-bottom: 2rem; }

    /* ========== BADGES ========== */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .badge-success { background: #dcfce7; color: #166534; }
    .badge-warning { background: #fef3c7; color: #92400e; }
    .badge-error { background: #fee2e2; color: #991b1b; }
    .badge-info { background: #dbeafe; color: #1e40af; }

    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #f1f5f9;
    }

    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }

    /* ========== PAGE HEADER ========== */
    .page-header {
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #e2e8f0;
    }

    .page-title {
        font-size: 1.75rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.25rem;
    }

    .page-subtitle {
        font-size: 0.95rem;
        color: #64748b;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# MOCK DATA
# ============================================================================

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

volume_gearing_data = pd.DataFrame(
    {
        "Quarter": ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"],
        "Ratio": [2.12, 2.28, 2.35, 2.45],
        "Volume": [485000, 512000, 548000, 592000],
        "Benchmark": [2.0, 2.1, 2.15, 2.2],
    }
)

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

department_breakdown = pd.DataFrame(
    {
        "Department": ["Engineering", "Sales", "Marketing", "Operations", "Other"],
        "Value": [35, 25, 15, 15, 10],
    }
)

recent_workflows = pd.DataFrame(
    {
        "ID": ["WF-001", "WF-002", "WF-003", "WF-004", "WF-005", "WF-006"],
        "Workflow Name": [
            "Customer Onboarding",
            "Invoice Processing",
            "Lead Qualification",
            "Support Ticket Routing",
            "Employee Onboarding",
            "Report Generation",
        ],
        "Department": [
            "Sales",
            "Finance",
            "Marketing",
            "Operations",
            "HR",
            "Engineering",
        ],
        "Status": [
            "Completed",
            "Completed",
            "Pending",
            "Completed",
            "Failed",
            "Completed",
        ],
        "Duration": ["2h 15m", "45m", "1h 30m", "15m", "3h 45m", "30m"],
    }
)

executive_summaries = [
    {
        "title": "Operational Excellence",
        "content": "Workflow completion rates increased by 12.5% this quarter, driven by automation in Engineering and Operations departments.",
        "metric": "+12.5%",
        "label": "Workflow Growth",
        "icon": "📈",
    },
    {
        "title": "Financial Performance",
        "content": "Volume gearing ratio at 2.45 exceeds industry benchmark of 2.2, indicating optimal resource utilization.",
        "metric": "2.45",
        "label": "Gearing Ratio",
        "icon": "💰",
    },
    {
        "title": "Workforce Productivity",
        "content": "Overall productivity at 87.3% with Engineering leading at 92.5%. Focus areas: HR and Marketing departments.",
        "metric": "87.3%",
        "label": "Avg Productivity",
        "icon": "👥",
    },
    {
        "title": "Technology Adoption",
        "content": "Core technology adoption strong at 90%+. AI adoption at 45% with growth potential through training programs.",
        "metric": "76.8%",
        "label": "Tech Adoption",
        "icon": "💻",
    },
]

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

# ============================================================================
# CHART CONFIGURATION
# ============================================================================

COLORS = {
    "primary": "#3b82f6",
    "success": "#10b981",
    "warning": "#f59e0b",
    "error": "#ef4444",
    "gray": "#64748b",
    "dark": "#1a202c",
}


def get_chart_layout(height=350):
    return {
        "height": height,
        "margin": {"l": 10, "r": 10, "t": 10, "b": 40},
        "plot_bgcolor": "white",
        "paper_bgcolor": "white",
        "font": {"family": "Inter, sans-serif", "size": 11, "color": "#64748b"},
        "hoverlabel": {"bgcolor": "white", "font_size": 12},
        "xaxis": {
            "showgrid": False,
            "showline": True,
            "linecolor": "#e2e8f0",
            "tickfont": {"size": 10},
        },
        "yaxis": {
            "showgrid": True,
            "gridcolor": "#f1f5f9",
            "showline": False,
            "tickfont": {"size": 10},
        },
    }


# ============================================================================
# COMPONENTS
# ============================================================================


def render_kpi_card(label, value, change, trend, format_type="number", icon="📊"):
    if format_type == "percentage":
        display_value = f"{value}%"
    elif format_type == "ratio":
        display_value = f"{value:.2f}"
    elif format_type == "currency":
        display_value = f"${value:,.0f}"
    else:
        display_value = f"{value:,}"

    trend_class = "positive" if trend == "up" else "negative"
    trend_icon = "↗" if trend == "up" else "↘"
    icon_class = "success" if trend == "up" else "warning"

    st.markdown(
        f"""
    <div class="kpi-card">
        <div class="kpi-header">
            <div>
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{display_value}</div>
                <div class="kpi-change {trend_class}">
                    {trend_icon} {abs(change)}%
                </div>
            </div>
            <div class="kpi-icon {icon_class}">{icon}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chart_header(title, subtitle=""):
    st.markdown(
        f"""
    <div class="chart-header">
        <div class="chart-title">{title}</div>
        {f'<div class="chart-subtitle">{subtitle}</div>' if subtitle else ""}
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_summary_card(data):
    st.markdown(
        f"""
    <div class="summary-card">
        <div class="summary-icon">{data["icon"]}</div>
        <div class="summary-title">{data["title"]}</div>
        <div class="summary-content">{data["content"]}</div>
        <div style="margin-top: 1rem;">
            <div class="summary-metric">{data["metric"]}</div>
            <div class="summary-label">{data["label"]}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============================================================================
# CHARTS
# ============================================================================


def create_bar_chart(data):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            name="Completed",
            x=data["Month"],
            y=data["Completed"],
            marker_color=COLORS["success"],
        )
    )
    fig.add_trace(
        go.Bar(
            name="Pending",
            x=data["Month"],
            y=data["Pending"],
            marker_color=COLORS["warning"],
        )
    )
    fig.add_trace(
        go.Bar(
            name="Failed",
            x=data["Month"],
            y=data["Failed"],
            marker_color=COLORS["error"],
        )
    )
    fig.update_layout(
        **get_chart_layout(),
        barmode="stack",
        showlegend=True,
        legend=dict(orientation="h", y=-0.2),
    )
    return fig


def create_donut_chart(data):
    colors = [
        COLORS["primary"],
        COLORS["success"],
        COLORS["warning"],
        "#8b5cf6",
        "#ec4899",
    ]
    fig = go.Figure(
        data=[
            go.Pie(
                labels=data["Department"],
                values=data["Value"],
                hole=0.6,
                marker=dict(colors=colors),
                textinfo="label+percent",
                textfont=dict(size=11),
            )
        ]
    )
    fig.update_layout(**get_chart_layout(300), showlegend=False)
    return fig


def create_line_chart(data, x, y, color):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data[x],
            y=data[y],
            mode="lines+markers",
            line=dict(color=color, width=2),
            marker=dict(size=6, color=color),
            fill="tozeroy",
            fillcolor=f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1)",
        )
    )
    fig.update_layout(**get_chart_layout(), showlegend=False)
    return fig


def create_area_chart(data):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Ratio"],
            mode="lines+markers",
            name="Actual",
            line=dict(color=COLORS["primary"], width=2),
            fill="tozeroy",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Benchmark"],
            mode="lines",
            name="Benchmark",
            line=dict(color=COLORS["gray"], width=2, dash="dash"),
        )
    )
    fig.update_layout(
        **get_chart_layout(), showlegend=True, legend=dict(orientation="h", y=-0.2)
    )
    return fig


def create_horizontal_bar(data):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            y=data["Department"],
            x=data["Score"],
            orientation="h",
            marker_color=COLORS["primary"],
            text=data["Score"].apply(lambda x: f"{x}%"),
            textposition="outside",
        )
    )
    fig.update_layout(**get_chart_layout(), showlegend=False)
    return fig


def create_performance_chart(data):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=data["Month"],
            y=data["Revenue"],
            name="Revenue",
            marker_color=COLORS["primary"],
        ),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Profit"],
            name="Profit",
            mode="lines+markers",
            line=dict(color=COLORS["success"], width=2),
        ),
        secondary_y=True,
    )
    fig.update_layout(
        **get_chart_layout(), showlegend=True, legend=dict(orientation="h", y=-0.2)
    )
    return fig


def create_tech_chart(data):
    colors = [
        COLORS["success"]
        if x >= 80
        else COLORS["warning"]
        if x >= 60
        else COLORS["error"]
        for x in data["Adoption"]
    ]
    fig = go.Figure(
        data=[
            go.Bar(
                x=data["Tool"],
                y=data["Adoption"],
                marker_color=colors,
                text=data["Adoption"].apply(lambda x: f"{x}%"),
                textposition="outside",
            )
        ]
    )
    fig.add_hline(
        y=80,
        line_dash="dash",
        line_color=COLORS["success"],
        line_width=1,
        annotation_text="High (80%)",
    )
    fig.add_hline(
        y=60,
        line_dash="dash",
        line_color=COLORS["warning"],
        line_width=1,
        annotation_text="Medium (60%)",
    )
    fig.update_layout(**get_chart_layout(350), showlegend=False)
    return fig


# ============================================================================
# SESSION STATE
# ============================================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown(
        """
    <div style="text-align: center; padding: 2rem 0; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 1.5rem;">
        <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📊</div>
        <div style="font-size: 1.25rem; font-weight: 700; color: white; margin-bottom: 0.25rem;">BizView</div>
        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.6);">Executive Dashboard</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    pages = [
        ("Dashboard", "🏠"),
        ("Workflow Analytics", "📊"),
        ("Financial Metrics", "💰"),
        ("Productivity", "👥"),
        ("Tech Adoption", "💻"),
        ("Executive Summary", "📋"),
        ("Reports & Export", "📥"),
    ]

    for page_name, icon in pages:
        button_type = (
            "primary" if st.session_state.current_page == page_name else "secondary"
        )
        if st.button(f"{icon}  {page_name}", key=f"nav_{page_name}", type=button_type):
            st.session_state.current_page = page_name
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(
        f"""
    <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 8px; margin-top: 1rem;">
        <div style="font-size: 0.7rem; color: rgba(255,255,255,0.5); text-transform: uppercase; margin-bottom: 0.5rem;">Last Updated</div>
        <div style="font-size: 0.85rem; color: white; font-weight: 600;">{datetime.now().strftime("%b %d, %Y")}</div>
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.7); margin-top: 0.25rem;">{datetime.now().strftime("%I:%M %p")}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ============================================================================
# PAGES
# ============================================================================

if st.session_state.current_page == "Dashboard":
    st.markdown(
        '<div class="page-header"><div class="page-title">Dashboard</div><div class="page-subtitle">Overview of all key metrics and performance indicators</div></div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            kpi_data["workflow_count"]["label"],
            kpi_data["workflow_count"]["value"],
            kpi_data["workflow_count"]["change"],
            kpi_data["workflow_count"]["trend"],
            "number",
            kpi_data["workflow_count"]["icon"],
        )
    with col2:
        render_kpi_card(
            kpi_data["volume_gearing_ratio"]["label"],
            kpi_data["volume_gearing_ratio"]["value"],
            kpi_data["volume_gearing_ratio"]["change"],
            kpi_data["volume_gearing_ratio"]["trend"],
            "ratio",
            kpi_data["volume_gearing_ratio"]["icon"],
        )
    with col3:
        render_kpi_card(
            kpi_data["productivity"]["label"],
            kpi_data["productivity"]["value"],
            kpi_data["productivity"]["change"],
            kpi_data["productivity"]["trend"],
            "percentage",
            kpi_data["productivity"]["icon"],
        )
    with col4:
        render_kpi_card(
            kpi_data["tech_adoption"]["label"],
            kpi_data["tech_adoption"]["value"],
            kpi_data["tech_adoption"]["change"],
            kpi_data["tech_adoption"]["trend"],
            "percentage",
            kpi_data["tech_adoption"]["icon"],
        )

    st.markdown('<div class="spacing-md"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Workflow Trends", "Monthly completion rates")
        st.plotly_chart(
            create_bar_chart(workflow_trend_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Department Split", "Workflow distribution")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Financial Performance", "Revenue & profit")
        st.plotly_chart(
            create_performance_chart(monthly_performance),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Gearing Ratio", "Quarterly vs benchmark")
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<h3 style="margin: 2rem 0 1rem 0;">Executive Insights</h3>',
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        render_summary_card(executive_summaries[0])
        st.markdown('<div class="spacing-sm"></div>', unsafe_allow_html=True)
        render_summary_card(executive_summaries[2])
    with col2:
        render_summary_card(executive_summaries[1])
        st.markdown('<div class="spacing-sm"></div>', unsafe_allow_html=True)
        render_summary_card(executive_summaries[3])

    st.markdown(
        '<h3 style="margin: 2rem 0 1rem 0;">Recent Workflows</h3>',
        unsafe_allow_html=True,
    )
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=280
    )

elif st.session_state.current_page == "Workflow Analytics":
    st.markdown(
        '<div class="page-header"><div class="page-title">Workflow Analytics</div><div class="page-subtitle">Detailed workflow performance analysis</div></div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Workflows", 1247, 12.5, "up", "number", "📊")
    with col2:
        render_kpi_card("Completed", 1098, 15.2, "up", "number", "✅")
    with col3:
        render_kpi_card("Pending", 89, -8.3, "down", "number", "⏳")
    with col4:
        render_kpi_card("Failed", 60, -12.1, "down", "number", "❌")

    st.markdown('<div class="spacing-md"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Monthly Distribution", "Status breakdown")
        st.plotly_chart(
            create_bar_chart(workflow_trend_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Completion Trend", "Success rate")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data, "Month", "Completed", COLORS["success"]
            ),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("Workflow Execution Log", "Recent activity")
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=300
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Financial Metrics":
    st.markdown(
        '<div class="page-header"><div class="page-title">Financial Metrics</div><div class="page-subtitle">Financial performance and gearing analysis</div></div>',
        unsafe_allow_html=True,
    )

    total_revenue = monthly_performance["Revenue"].sum()
    total_profit = monthly_performance["Profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Gearing Ratio", 2.45, 8.3, "up", "ratio", "📈")
    with col2:
        render_kpi_card("Total Revenue", total_revenue, 18.5, "up", "currency", "💰")
    with col3:
        render_kpi_card("Total Profit", total_profit, 24.2, "up", "currency", "💵")
    with col4:
        render_kpi_card(
            "Profit Margin", round(profit_margin, 1), 5.8, "up", "percentage", "📊"
        )

    st.markdown('<div class="spacing-md"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Gearing Analysis", "Quarterly vs benchmark")
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Revenue Distribution", "By department")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("Performance Overview", "Monthly trends")
    st.plotly_chart(
        create_performance_chart(monthly_performance),
        use_container_width=True,
        config={"displayModeBar": False},
    )
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Productivity":
    st.markdown(
        '<div class="page-header"><div class="page-title">Productivity Metrics</div><div class="page-subtitle">Department performance tracking</div></div>',
        unsafe_allow_html=True,
    )

    avg_score = productivity_data["Score"].mean()
    on_target = (productivity_data["Score"] >= productivity_data["Target"]).sum()
    total_employees = productivity_data["Employees"].sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Avg Score", round(avg_score, 1), 5.2, "up", "percentage", "📈")
    with col2:
        render_kpi_card("On Target", on_target, 16.7, "up", "number", "🎯")
    with col3:
        render_kpi_card("Total Employees", total_employees, 8.4, "up", "number", "👥")
    with col4:
        render_kpi_card("Top Score", 92.5, 3.1, "up", "percentage", "🏆")

    st.markdown('<div class="spacing-md"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Department Scores", "Performance comparison")
        st.plotly_chart(
            create_horizontal_bar(productivity_data),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("Trend Analysis", "Monthly output")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data, "Month", "Completed", COLORS["primary"]
            ),
            use_container_width=True,
            config={"displayModeBar": False},
        )
        st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f'<div class="insight-card"><div class="insight-label">Top Performer</div><div class="insight-value" style="color: {COLORS["success"]};">Engineering</div><div class="insight-desc">92.5% score</div></div>',
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f'<div class="insight-card"><div class="insight-label">Achievement Rate</div><div class="insight-value" style="color: {COLORS["primary"]};">{int((on_target / len(productivity_data)) * 100)}%</div><div class="insight-desc">{on_target} of {len(productivity_data)} departments</div></div>',
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f'<div class="insight-card"><div class="insight-label">Workforce</div><div class="insight-value" style="color: {COLORS["dark"]};">{total_employees}</div><div class="insight-desc">Total employees</div></div>',
            unsafe_allow_html=True,
        )

elif st.session_state.current_page == "Tech Adoption":
    st.markdown(
        '<div class="page-header"><div class="page-title">Technology Adoption</div><div class="page-subtitle">Technology stack utilization metrics</div></div>',
        unsafe_allow_html=True,
    )

    avg_adoption = tech_adoption_data["Adoption"].mean()
    high = (tech_adoption_data["Adoption"] >= 80).sum()
    low = (tech_adoption_data["Adoption"] < 60).sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Adoption", round(avg_adoption, 1), -2.1, "down", "percentage", "💻"
        )
    with col2:
        render_kpi_card("High Adoption", high, 12.5, "up", "number", "✅")
    with col3:
        render_kpi_card("Low Adoption", low, -25.0, "down", "number", "⚠️")
    with col4:
        render_kpi_card("Emerging Tech", 1, 100, "up", "number", "🚀")

    st.markdown('<div class="spacing-md"></div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("Adoption by Tool", "Performance thresholds")
    st.plotly_chart(
        create_tech_chart(tech_adoption_data),
        use_container_width=True,
        config={"displayModeBar": False},
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("Technology Stack", "Complete inventory")
    styled_data = tech_adoption_data.copy()
    styled_data["Status"] = styled_data["Adoption"].apply(
        lambda x: "🟢 High" if x >= 80 else "🟡 Medium" if x >= 60 else "🔴 Low"
    )
    st.dataframe(styled_data, use_container_width=True, hide_index=True, height=350)
    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.current_page == "Executive Summary":
    st.markdown(
        '<div class="page-header"><div class="page-title">Executive Summary</div><div class="page-subtitle">Strategic insights and recommendations</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: white; border-radius: 12px; padding: 2rem; margin-bottom: 1.5rem;">
        <div style="font-size: 0.75rem; color: #fbbf24; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.5rem;">📅 {datetime.now().strftime("%B %d, %Y")}</div>
        <div style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.75rem;">Monthly Executive Report</div>
        <div style="color: rgba(255,255,255,0.8); line-height: 1.6;">Comprehensive overview of organizational performance, key achievements, and strategic recommendations.</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    stats = [
        ("📊", f"{kpi_data['workflow_count']['value']:,}", "Workflows"),
        ("📈", str(kpi_data["volume_gearing_ratio"]["value"]), "Gearing"),
        ("👥", f"{kpi_data['productivity']['value']}%", "Productivity"),
        ("💻", f"{kpi_data['tech_adoption']['value']}%", "Tech Adoption"),
    ]
    for col, (icon, value, label) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f'<div class="insight-card" style="text-align: center;"><div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div><div class="insight-value">{value}</div><div class="insight-label" style="text-align: center;">{label}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown(
        '<h3 style="margin: 2rem 0 1rem 0;">Key Insights</h3>', unsafe_allow_html=True
    )
    for i in range(0, 4, 2):
        col1, col2 = st.columns(2)
        with col1:
            render_summary_card(executive_summaries[i])
        with col2:
            render_summary_card(executive_summaries[i + 1])
        st.markdown('<div class="spacing-sm"></div>', unsafe_allow_html=True)

elif st.session_state.current_page == "Reports & Export":
    st.markdown(
        '<div class="page-header"><div class="page-title">Reports & Export</div><div class="page-subtitle">Download comprehensive reports and data</div></div>',
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <div style="width: 50px; height: 50px; background: linear-gradient(135deg, {COLORS["dark"]}, {COLORS["primary"]}); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem;">📄</span>
            </div>
            <h4 style="margin-bottom: 0.5rem;">HTML Report</h4>
            <p style="font-size: 0.875rem; color: #64748b; margin-bottom: 1rem;">Complete dashboard report with all metrics and charts</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        html_report = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>BizView Report - {datetime.now().strftime("%Y%m%d")}</title>
            <style>
                body {{ font-family: Inter, sans-serif; padding: 2rem; max-width: 1200px; margin: 0 auto; }}
                h1 {{ color: #1a202c; }}
                .kpi {{ display: inline-block; background: #f8fafc; padding: 1rem; margin: 0.5rem; border-radius: 8px; }}
                .value {{ font-size: 2rem; font-weight: 700; color: #1a202c; }}
            </style>
        </head>
        <body>
            <h1>📊 BizView Executive Report</h1>
            <p>Generated: {datetime.now().strftime("%B %d, %Y")}</p>
            <div>
                <div class="kpi"><div class="value">1,247</div><div>Total Workflows</div></div>
                <div class="kpi"><div class="value">2.45</div><div>Gearing Ratio</div></div>
                <div class="kpi"><div class="value">87.3%</div><div>Productivity</div></div>
                <div class="kpi"><div class="value">76.8%</div><div>Tech Adoption</div></div>
            </div>
        </body>
        </html>
        """
        st.download_button(
            "📥 Download HTML",
            data=html_report,
            file_name=f"BizView_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <div style="width: 50px; height: 50px; background: linear-gradient(135deg, {COLORS["success"]}, {COLORS["primary"]}); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem;">📊</span>
            </div>
            <h4 style="margin-bottom: 0.5rem;">Excel Export</h4>
            <p style="font-size: 0.875rem; color: #64748b; margin-bottom: 1rem;">Multi-sheet workbook with all data tables</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            workflow_trend_data.to_excel(writer, sheet_name="Workflows", index=False)
            productivity_data.to_excel(writer, sheet_name="Productivity", index=False)
            tech_adoption_data.to_excel(writer, sheet_name="Tech", index=False)

        st.download_button(
            "📥 Download Excel",
            data=buffer.getvalue(),
            file_name=f"BizView_Data_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card">
            <div style="width: 50px; height: 50px; background: linear-gradient(135deg, {COLORS["warning"]}, {COLORS["error"]}); border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem;">📋</span>
            </div>
            <h4 style="margin-bottom: 0.5rem;">CSV Export</h4>
            <p style="font-size: 0.875rem; color: #64748b; margin-bottom: 1rem;">Raw data files for external tools</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.download_button(
            "📥 Download CSV",
            data=productivity_data.to_csv(index=False),
            file_name=f"BizView_Data_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True,
        )

# Footer
st.markdown('<div class="spacing-lg"></div>', unsafe_allow_html=True)
st.markdown(
    f"""
<div style="text-align: center; padding: 1.5rem; background: #f8fafc; border-radius: 8px; border: 1px solid #e2e8f0;">
    <p style="color: #64748b; font-size: 0.875rem; margin: 0;"><strong>BizView Executive Dashboard</strong> • Professional Edition • {datetime.now().strftime("%Y")}</p>
</div>
""",
    unsafe_allow_html=True,
)
