"""
BizView Executive Dashboard - ULTRA PREMIUM EDITION
Enterprise-Grade Streamlit Application with:
- Glassmorphism UI & Premium Gradients
- D3-Style Smooth Animations
- 4K/HD Chart Rendering
- React-Like Component Architecture
- Optimized for 16" Displays
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
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
# ============================================================================
# V5 ENTERPRISE SAAS DESIGN SYSTEM - REACT GRID & STRIPE STYLE
# ============================================================================
st.markdown(
    """
<style>
    /* ========== 1. SAAS VARIABLES & THEME TOKENS ========== */
    :root {
        /* Base Colors - Slate (Professional Neutral) */
        --bg-app: #f8fafc;       /* Slate-50 */
        --bg-card: #ffffff;      /* White */
        --bg-sidebar: #0f172a;   /* Slate-900 */
        
        /* Typography Colors */
        --text-primary: #0f172a; /* Slate-900 */
        --text-secondary: #64748b; /* Slate-500 */
        --text-tertiary: #94a3b8; /* Slate-400 */
        
        /* Brand Colors - Indigo/Violet 'Linear' Vibe */
        --brand-primary: #6366f1; /* Indigo-500 */
        --brand-secondary: #8b5cf6; /* Violet-500 */
        --brand-accent: #0ea5e9; /* Sky-500 */
        
        /* Status Colors - Muted & Professional */
        --status-success-bg: #dcfce7; --status-success-text: #166534;
        --status-warning-bg: #fef9c3; --status-warning-text: #854d0e;
        --status-error-bg: #fee2e2;   --status-error-text: #991b1b;
        --status-info-bg: #e0f2fe;    --status-info-text: #075985;

        /* Borders & Shadows */
        --border-subtle: #f1f5f9;
        --border-light: #e2e8f0;
        --border-focus: #cbd5e1;
        --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.06);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.06);
        
        /* Spacing System */
        --space-1: 0.25rem;
        --space-2: 0.5rem;
        --space-3: 0.75rem;
        --space-4: 1rem;
    }

    /* ========== 2. GLOBAL RESET & LAYOUT ========== */
    
    /* Font Import - Inter & Outfit */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
        box-sizing: border-box;
    }
    
    /* App Container Reset */
    .stApp {
        background-color: var(--bg-app) !important;
    }
    
    /* Main Content Area - ZERO PADDING START */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 100% !important;
        margin-top: 0 !important;
    }
    
    /* Hide Streamlit UI Elements */
    #MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
    [data-testid="stToolbar"] { display: none !important; }
    .stApp > header { display: none !important; }
    
    /* Remove vertical gaps between Streamlit elements */
    div[data-testid="stVerticalBlock"] {
        gap: 0.75rem !important;
    }
    
    /* ========== 3. SIDEBAR - COMMAND CENTER ========== */
    [data-testid="stSidebar"] {
        background-color: var(--bg-sidebar) !important;
        border-right: 1px solid #1e293b !important;
        width: 260px !important;
        padding-top: 0 !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding: 0 !important;
    }
    
    /* Sidebar Header Area */
    .sidebar-header {
        padding: 1.5rem 1rem 1rem 1rem;
        border-bottom: 1px solid rgba(255,255,255,0.05);
        margin-bottom: 1rem;
    }
    
    /* Sidebar Nav Buttons */
    [data-testid="stSidebar"] .stButton > button {
        width: 100%;
        background: transparent !important;
        color: #94a3b8 !important; /* Slate-400 */
        border: none !important;
        border-radius: 6px !important;
        padding: 0.5rem 0.75rem !important;
        font-size: 0.875rem !important;
        font-weight: 500 !important;
        display: flex !important;
        justify-content: flex-start !important;
        align-items: center !important;
        transition: all 0.15s ease !important;
        margin: 0.1rem 0 !important;
    }
    
    /* Hover State */
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(255,255,255,0.05) !important;
        color: #f8fafc !important;
    }
    
    /* Active State - 'Linear' Style */
    [data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: rgba(255,255,255,0.1) !important;
        color: #ffffff !important;
        box-shadow: inset 2px 0 0 0 var(--brand-primary) !important;
        border-radius: 4px !important; /* Sharper corners for active */
    }

    /* ========== 4. KPI CARDS - STRIPE STYLE ========== */
    .kpi-card {
        background: var(--bg-card);
        border: 1px solid var(--border-light);
        border-radius: 8px; /* Standard radius */
        padding: 1rem 1.25rem;
        box-shadow: var(--shadow-sm);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.2s ease;
    }
    
    .kpi-card:hover {
        box-shadow: var(--shadow-md);
        border-color: var(--border-focus);
        transform: translateY(-1px);
    }
    
    .kpi-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: var(--text-secondary);
        font-weight: 600;
        margin-bottom: 0.25rem;
    }
    
    .kpi-value-row {
        display: flex;
        align-items: baseline;
        justify-content: space-between;
        margin-top: 0.25rem;
    }
    
    .kpi-value {
        font-family: 'Inter', sans-serif; /* Clean Inter */
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.02em;
        line-height: 1.2;
    }
    
    .kpi-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.125rem 0.5rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        gap: 0.25rem;
    }
    
    .badge-success { background: var(--status-success-bg); color: var(--status-success-text); }
    .badge-warning { background: var(--status-warning-bg); color: var(--status-warning-text); }
    .badge-error { background: var(--status-error-bg); color: var(--status-error-text); }

    /* ========== 5. CHARTS - MODERN MINIMAL ========== */
    .chart-card {
        background: var(--bg-card);
        border: 1px solid var(--border-light);
        border-radius: 8px;
        padding: 0;
        box-shadow: var(--shadow-sm);
        margin-bottom: 1rem;
    }
    
    .chart-header {
        padding: 1rem 1.25rem;
        border-bottom: 1px solid var(--border-subtle);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .chart-title {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-primary);
    }
    
    /* ========== 6. HEADERS & TYPOGRAPHY ========== */
    h1 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.75rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.02em !important;
        margin-bottom: 0.5rem !important;
    }
    
    h2, h3 {
        font-family: 'Inter', sans-serif;
        color: var(--text-primary) !important;
        letter-spacing: -0.01em !important;
    }
    
    /* ========== 7. UTILITY CLASSES ========== */
    .spacer-xs { height: 0.5rem; }
    .spacer-sm { height: 1rem; }
    .spacer-md { height: 2rem; }
    
</style>
    """,
    unsafe_allow_html=True,
)

# ============================================================================
# MOCK DATA - ENTERPRISE DATASET
# ============================================================================

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
        "content": "Workflow completion rates have increased by 12.5% compared to last quarter, driven primarily by process automation initiatives in the Engineering and Operations departments.",
        "metric": "+12.5%",
        "metric_label": "Workflow Efficiency",
        "icon": "📈",
    },
    {
        "title": "Financial Performance",
        "content": "Volume gearing ratio has improved to 2.45, exceeding the industry benchmark of 2.2. This indicates optimal resource utilization and scalable growth patterns.",
        "metric": "2.45",
        "metric_label": "Gearing Ratio",
        "icon": "💰",
    },
    {
        "title": "Workforce Productivity",
        "content": "Overall productivity score stands at 87.3%, with Engineering leading at 92.5%. Cross-departmental collaboration initiatives have contributed to a 5.2% increase.",
        "metric": "87.3%",
        "metric_label": "Avg Productivity",
        "icon": "👥",
    },
    {
        "title": "Technology Transformation",
        "content": "Core technology adoption remains strong at 90%+, while emerging technologies like AI assistants show 45% adoption with significant growth potential.",
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

# ============================================================================
# CHART CONFIGURATION - 4K READY & D3-STYLE
# ============================================================================

# Premium Color Palette
COLORS = {
    "primary": "#3b82f6",
    "secondary": "#8b5cf6",
    "accent": "#06b6d4",
    "success": "#10b981",
    "warning": "#f59e0b",
    "error": "#ef4444",
    "navy": "#0f172a",
    "gray": "#64748b",
}


# Plotly Template for V5 SaaS
def get_chart_config():
    return {
        "displayModeBar": False,
        "responsive": True,
        "displaylogo": False,
    }


def get_chart_layout(title="", height=280):
    """V5 Minimal Chart Layout"""
    return {
        "title": {"text": "", "font": {"size": 1}},
        "height": height,
        "margin": {"l": 10, "r": 10, "t": 10, "b": 30},
        "plot_bgcolor": "rgba(0,0,0,0)",
        "paper_bgcolor": "rgba(0,0,0,0)",
        "font": {"family": "Inter, sans-serif", "size": 11, "color": "#64748b"},
        "hoverlabel": {
            "bgcolor": "white",
            "font_size": 12,
            "font_family": "Inter, sans-serif",
            "bordercolor": "#e2e8f0",
            "namelength": -1,
        },
        "xaxis": {
            "showgrid": False,
            "showline": True,
            "linecolor": "#e2e8f0",
            "linewidth": 1,
            "tickfont": {"size": 10, "color": "#94a3b8"},
            "zeroline": False,
        },
        "yaxis": {
            "showgrid": True,
            "gridcolor": "#f1f5f9",
            "gridwidth": 1,
            "griddash": "dot",
            "showline": False,
            "tickfont": {"size": 10, "color": "#94a3b8"},
            "zeroline": False,
        },
        "legend": {
            "orientation": "h",
            "yanchor": "top",
            "y": -0.15,
            "xanchor": "center",
            "x": 0.5,
            "bgcolor": "rgba(0,0,0,0)",
        },
    }


# ============================================================================
# REACT-LIKE COMPONENTS
# ============================================================================


def render_kpi_card(
    label, value, change, trend, format_type="number", icon="📊", animation_delay=0
):
    """V5 SaaS KPI Card - Stripe Style"""

    # Format value
    if format_type == "percentage":
        display_value = f"{value}%"
    elif format_type == "ratio":
        display_value = f"{value:.2f}"
    elif format_type == "currency":
        display_value = f"${value:,.0f}"
    else:
        display_value = f"{value:,}"

    # Determine badge styling
    if trend == "up":
        trend_icon = "↗"
        badge_class = "badge-success"
        trend_color = "var(--status-success-text)"
    else:
        trend_icon = "↘"
        badge_class = "badge-error"
        trend_color = "var(--status-error-text)"

    # Add 'neutral' logic if change is small? For now keep binary.

    st.markdown(
        f"""
    <div class="kpi-card" style="animation-delay: {animation_delay}s;">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value-row">
            <div class="kpi-value">{display_value}</div>
            <div class="kpi-badge {badge_class}">
                {trend_icon} {abs(change)}%
            </div>
        </div>
        <div style="margin-top: 0.5rem; height: 4px; width: 100%; background: var(--gray-100); border-radius: 2px; overflow: hidden;">
            <div style="height: 100%; width: {min(abs(change) * 5, 100)}%; background: {trend_color}; border-radius: 2px;"></div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_chart_header(title, subtitle=""):
    """V5 Chart Header - Minimalist"""
    st.markdown(
        f"""
    <div class="chart-header">
        <div class="chart-title">{title}</div>
        {f'<div style="font-size: 0.75rem; color: var(--text-tertiary);">{subtitle}</div>' if subtitle else ""}
    </div>
    """,
        unsafe_allow_html=True,
    )


def render_summary_card(summary):
    """V5 Executive Summary Card"""
    st.markdown(
        f"""
    <div class="summary-card">
        <div style="font-size: 1.5rem; margin-bottom: 0.75rem;">{summary["icon"]}</div>
        <div style="font-weight: 600; color: #f8fafc; margin-bottom: 0.5rem;">{summary["title"]}</div>
        <div style="font-size: 0.75rem; color: #cbd5e1; line-height: 1.5; margin-bottom: 1rem;">
            {summary["content"]}
        </div>
        <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 0.75rem;">
            <div style="font-size: 1.25rem; font-weight: 700; color: white;">{summary["metric"]}</div>
            <div style="font-size: 0.7rem; text-transform: uppercase; color: #94a3b8; letter-spacing: 0.05em;">{summary["metric_label"]}</div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


# ============================================================================
# CHART COMPONENTS - D3-STYLE WITH ANIMATIONS
# ============================================================================


def create_workflow_bar_chart(data):
    """Animated Stacked Bar Chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            name="Completed",
            x=data["Month"],
            y=data["Completed"],
            marker=dict(
                color=COLORS["success"],
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
            hovertemplate="<b>%{x}</b><br>Completed: %{y}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Bar(
            name="Pending",
            x=data["Month"],
            y=data["Pending"],
            marker=dict(
                color=COLORS["warning"],
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
            hovertemplate="<b>%{x}</b><br>Pending: %{y}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Bar(
            name="Failed",
            x=data["Month"],
            y=data["Failed"],
            marker=dict(
                color=COLORS["error"], line=dict(color="rgba(255,255,255,0.5)", width=2)
            ),
            hovertemplate="<b>%{x}</b><br>Failed: %{y}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    layout.update(
        {
            "barmode": "stack",
            "bargap": 0.2,
        }
    )
    fig.update_layout(**layout)

    return fig


def create_donut_chart(data):
    """Premium Donut Chart with Gradient Effect"""
    colors = [
        COLORS["primary"],
        COLORS["accent"],
        COLORS["success"],
        COLORS["warning"],
        COLORS["secondary"],
    ]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=data["Department"],
                values=data["Value"],
                hole=0.65,
                marker=dict(colors=colors, line=dict(color="white", width=3)),
                textposition="outside",
                textinfo="label+percent",
                textfont=dict(size=12, family="Inter, sans-serif"),
                hovertemplate="<b>%{label}</b><br>%{value}%<br>%{percent}<extra></extra>",
            )
        ]
    )

    layout = get_chart_layout(height=380)
    layout.update(
        {
            "showlegend": False,
            "annotations": [
                {
                    "text": f"<b>{data['Value'].sum()}%</b><br><span style='font-size:11px; color:#94a3b8;'>Total</span>",
                    "x": 0.5,
                    "y": 0.5,
                    "font": {
                        "size": 24,
                        "family": "Outfit, sans-serif",
                        "color": "#0f172a",
                    },
                    "showarrow": False,
                }
            ],
        }
    )
    fig.update_layout(**layout)

    return fig


def create_line_chart(data, x_col, y_col, name, color):
    """Smooth Line Chart with Area Fill"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y_col],
            mode="lines+markers",
            name=name,
            line=dict(color=color, width=3, shape="spline"),
            marker=dict(size=8, color=color, line=dict(color="white", width=2)),
            fill="tozeroy",
            fillcolor=f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1)",
            hovertemplate="<b>%{x}</b><br>" + name + ": %{y}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)

    return fig


def create_area_chart(data):
    """Multi-Series Area Chart"""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Ratio"],
            mode="lines+markers",
            name="Actual Ratio",
            line=dict(color=COLORS["primary"], width=3),
            marker=dict(size=10, symbol="circle"),
            fill="tozeroy",
            fillcolor="rgba(59, 130, 246, 0.2)",
            hovertemplate="<b>%{x}</b><br>Ratio: %{y:.2f}<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=data["Quarter"],
            y=data["Benchmark"],
            mode="lines",
            name="Benchmark",
            line=dict(color=COLORS["gray"], width=2, dash="dash"),
            hovertemplate="<b>%{x}</b><br>Benchmark: %{y:.2f}<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)

    return fig


def create_horizontal_bar_chart(data):
    """Horizontal Bar Chart with Target Comparison"""
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=data["Department"],
            x=data["Score"],
            name="Score",
            orientation="h",
            marker=dict(
                color=data["Score"],
                colorscale=[
                    [0, COLORS["error"]],
                    [0.5, COLORS["warning"]],
                    [1, COLORS["success"]],
                ],
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
            text=data["Score"].apply(lambda x: f"{x}%"),
            textposition="outside",
            hovertemplate="<b>%{y}</b><br>Score: %{x}%<extra></extra>",
        )
    )

    fig.add_trace(
        go.Scatter(
            y=data["Department"],
            x=data["Target"],
            mode="markers",
            name="Target",
            marker=dict(
                size=12,
                color=COLORS["navy"],
                symbol="diamond",
                line=dict(color="white", width=2),
            ),
            hovertemplate="<b>%{y}</b><br>Target: %{x}%<extra></extra>",
        )
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)

    return fig


def create_tech_adoption_chart(data):
    """Tech Adoption Chart with Threshold Lines"""
    fig = go.Figure()

    colors = [
        COLORS["success"]
        if x >= 80
        else COLORS["warning"]
        if x >= 60
        else COLORS["error"]
        for x in data["Adoption"]
    ]

    fig.add_trace(
        go.Bar(
            x=data["Tool"],
            y=data["Adoption"],
            marker=dict(
                color=colors, line=dict(color="rgba(255,255,255,0.5)", width=2)
            ),
            text=data["Adoption"].apply(lambda x: f"{x}%"),
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Adoption: %{y}%<extra></extra>",
        )
    )

    # Add threshold lines
    fig.add_hline(
        y=80,
        line_dash="dash",
        line_color=COLORS["success"],
        line_width=2,
        annotation_text="High (80%)",
        annotation_position="right",
    )
    fig.add_hline(
        y=60,
        line_dash="dash",
        line_color=COLORS["warning"],
        line_width=2,
        annotation_text="Medium (60%)",
        annotation_position="right",
    )

    layout = get_chart_layout(height=400)
    fig.update_layout(**layout)

    return fig


def create_performance_chart(data):
    """Multi-Axis Performance Chart"""
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Bar(
            x=data["Month"],
            y=data["Revenue"],
            name="Revenue",
            marker=dict(
                color=COLORS["primary"],
                line=dict(color="rgba(255,255,255,0.5)", width=2),
            ),
            hovertemplate="<b>%{x}</b><br>Revenue: $%{y:,.0f}<extra></extra>",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=data["Month"],
            y=data["Profit"],
            name="Profit",
            mode="lines+markers",
            line=dict(color=COLORS["success"], width=3),
            marker=dict(size=8, line=dict(color="white", width=2)),
            hovertemplate="<b>%{x}</b><br>Profit: $%{y:,.0f}<extra></extra>",
        ),
        secondary_y=True,
    )

    layout = get_chart_layout(height=380)
    fig.update_layout(**layout)
    fig.update_yaxes(title_text="Revenue ($)", secondary_y=False)
    fig.update_yaxes(title_text="Profit ($)", secondary_y=True)

    return fig


# ============================================================================
# EXPORT FUNCTIONALITY
# ============================================================================


def generate_html_report():
    """Generate HTML Report for Download"""
    current_date = datetime.now().strftime("%B %d, %Y")

    # Convert dataframe to HTML with styling
    workflows_html = recent_workflows.to_html(
        index=False, border=0, classes="styled-table"
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BizView Executive Report - {current_date}</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{ font-family: 'Inter', sans-serif; color: #0f172a; background: #ffffff; padding: 4rem; max-width: 1200px; margin: 0 auto; }}
            .header {{ border-bottom: 4px solid #0f172a; padding-bottom: 2rem; margin-bottom: 3rem; display: flex; justify-content: space-between; align-items: flex-end; }}
            .header h1 {{ font-family: 'Outfit', sans-serif; font-size: 3rem; font-weight: 800; color: #0f172a; line-height: 1; }}
            .header .subtitle {{ color: #64748b; font-size: 1.25rem; margin-top: 0.5rem; font-weight: 500; }}
            .header .meta {{ text-align: right; }}
            .header .date {{ font-size: 1.25rem; font-weight: 700; color: #0f172a; }}
            
            .kpi-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.5rem; margin-bottom: 4rem; }}
            .kpi-card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 16px; padding: 2rem; text-align: center; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }}
            .kpi-card .value {{ font-family: 'Outfit', sans-serif; font-size: 2.5rem; font-weight: 800; color: #0f172a; margin: 0.5rem 0; letter-spacing: -0.02em; }}
            .kpi-card .label {{ color: #64748b; font-size: 0.875rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }}
            .kpi-card .change {{ display: inline-flex; align-items: center; gap: 0.25rem; margin-top: 1rem; padding: 0.375rem 0.75rem; border-radius: 100px; font-size: 0.875rem; font-weight: 700; }}
            .kpi-card .change.positive {{ background: #dcfce7; color: #166534; }}
            .kpi-card .change.negative {{ background: #fee2e2; color: #991b1b; }}
            
            .section {{ margin-bottom: 4rem; }}
            .section h2 {{ font-family: 'Outfit', sans-serif; font-size: 1.75rem; font-weight: 800; margin-bottom: 1.5rem; color: #0f172a; letter-spacing: -0.02em; border-left: 5px solid #3b82f6; padding-left: 1rem; }}
            
            .styled-table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; border-radius: 12px; overflow: hidden; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1); }}
            .styled-table thead tr {{ background-color: #f1f5f9; color: #475569; text-align: left; font-weight: 600; }}
            .styled-table th, .styled-table td {{ padding: 1rem 1.5rem; border-bottom: 1px solid #e2e8f0; }}
            .styled-table tbody tr:last-of-type border-bottom {{ border-bottom: 2px solid #3b82f6; }}
            .styled-table tbody tr:hover {{ background-color: #f8fafc; }}
            
            .footer {{ margin-top: 5rem; padding-top: 2rem; border-top: 1px solid #e2e8f0; text-align: center; color: #94a3b8; font-size: 0.875rem; }}
        </style>
    </head>
    <body>
        <div class="header">
            <div>
                <h1>BizView Dashboard</h1>
                <div class="subtitle">Executive Performance Report</div>
            </div>
            <div class="meta">
                <div class="date">{current_date}</div>
                <div style="color: #64748b; font-size: 0.875rem; margin-top: 0.25rem;">CONFIDENTIAL</div>
            </div>
        </div>
        
        <div class="section">
            <h2>Key Performance Indicators</h2>
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="label">Total Workflows</div>
                    <div class="value">1,247</div>
                    <div class="change positive">↗ 12.5%</div>
                </div>
                <div class="kpi-card">
                    <div class="label">Gearing Ratio</div>
                    <div class="value">2.45</div>
                    <div class="change positive">↗ 8.3%</div>
                </div>
                <div class="kpi-card">
                    <div class="label">Productivity</div>
                    <div class="value">87.3%</div>
                    <div class="change positive">↗ 5.2%</div>
                </div>
                <div class="kpi-card">
                    <div class="label">Tech Adoption</div>
                    <div class="value">76.8%</div>
                    <div class="change negative">↘ 2.1%</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>Recent Workflows</h2>
            {workflows_html}
        </div>
        
        <div class="section">
            <h2>Executive Summary</h2>
            <div style="background: #f8fafc; padding: 2rem; border-radius: 12px; border: 1px solid #e2e8f0; line-height: 1.8;">
                <p><strong>Operational Excellence:</strong> Workflow completion rates have increased by 12.5% compared to last quarter, driven primarily by process automation initiatives in the Engineering and Operations departments.</p>
                <div style="height: 1rem;"></div>
                <p><strong>Financial Performance:</strong> Volume gearing ratio has improved to 2.45, exceeding the industry benchmark of 2.2. This indicates optimal resource utilization and scalable growth patterns.</p>
            </div>
        </div>
        
        <div class="footer">
            <p>Generated by BizView Analytics Platform • Enterprise Edition</p>
            <p style="margin-top: 0.5rem;">For internal use only. Do not distribute without authorization.</p>
        </div>
    </body>
    </html>
    """
    return html


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

with st.sidebar:
    st.markdown(
        """
    <div class="sidebar-header">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 32px; height: 32px; background: var(--brand-primary); border-radius: 6px; display: flex; align-items: center; justify-content: center;">
                <span style="color: white; font-weight: 800; font-size: 1.1rem;">B</span>
            </div>
            <div>
                <div style="font-family: 'Outfit', sans-serif; font-weight: 700; font-size: 1.1rem; color: #f8fafc; line-height: 1;">BizView</div>
                <div style="font-size: 0.7rem; color: #64748b; font-weight: 500; letter-spacing: 0.05em;">ENTERPRISE</div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div style='font-size: 0.7rem; font-weight: 600; color: rgba(255,255,255,0.4); margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;'>Menu</div>",
        unsafe_allow_html=True,
    )

    pages = [
        ("Dashboard", "🏠"),
        ("Workflow", "📊"),
        ("Financial", "💰"),
        ("Productivity", "👥"),
        ("Tech Stack", "💻"),
        ("Summary", "📋"),
        ("Export", "📥"),
    ]

    for page_name, icon in pages:
        # Match short names to session state full names
        full_name = page_name
        if page_name == "Workflow":
            full_name = "Workflow Analytics"
        if page_name == "Financial":
            full_name = "Financial Metrics"
        if page_name == "Tech Stack":
            full_name = "Tech Adoption"
        if page_name == "Summary":
            full_name = "Executive Summary"
        if page_name == "Export":
            full_name = "Reports & Export"

        button_type = (
            "primary" if st.session_state.current_page == full_name else "secondary"
        )
        if st.button(f"{icon}  {page_name}", key=f"nav_{page_name}", type=button_type):
            st.session_state.current_page = full_name
            st.rerun()

    st.markdown(
        "<div style='flex-grow: 1;'></div>", unsafe_allow_html=True
    )  # Spacer push to bottom
    st.markdown("<hr style='margin: 1rem 0; opacity: 0.1;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.selectbox(
            "Theme", ["Auto", "Dark"], key="theme_select", label_visibility="collapsed"
        )
    with col2:
        st.download_button(
            "📥 Report",
            data=generate_html_report(),
            file_name="report.html",
            use_container_width=True,
        )


# ============================================================================
# MAIN CONTENT AREA
# ============================================================================

# Dashboard Page
if st.session_state.current_page == "Dashboard":
    # Inline Header for extra Compactness
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
            <h1 style="margin: 0; font-size: 1.5rem;">🏠 Executive Dashboard</h1>
            <p style="margin: 0; color: #64748b; font-size: 0.9rem;">Overview of key performance indicators</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # KPI Cards Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            kpi_data["workflow_count"]["label"],
            kpi_data["workflow_count"]["value"],
            kpi_data["workflow_count"]["change"],
            kpi_data["workflow_count"]["trend"],
            "number",
            kpi_data["workflow_count"]["icon"],
            0,
        )
    with col2:
        render_kpi_card(
            kpi_data["volume_gearing_ratio"]["label"],
            kpi_data["volume_gearing_ratio"]["value"],
            kpi_data["volume_gearing_ratio"]["change"],
            kpi_data["volume_gearing_ratio"]["trend"],
            "ratio",
            kpi_data["volume_gearing_ratio"]["icon"],
            0.1,
        )
    with col3:
        render_kpi_card(
            kpi_data["productivity"]["label"],
            kpi_data["productivity"]["value"],
            kpi_data["productivity"]["change"],
            kpi_data["productivity"]["trend"],
            "percentage",
            kpi_data["productivity"]["icon"],
            0.2,
        )
    with col4:
        render_kpi_card(
            kpi_data["tech_adoption"]["label"],
            kpi_data["tech_adoption"]["value"],
            kpi_data["tech_adoption"]["change"],
            kpi_data["tech_adoption"]["trend"],
            "percentage",
            kpi_data["tech_adoption"]["icon"],
            0.3,
        )

    # Charts Row 1
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("WORKFLOW TRENDS", "Monthly completion rates by status")
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT SPLIT", "Workflow distribution")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Charts Row 2
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("FINANCIAL PERFORMANCE", "Revenue & Profit Analysis")
        st.plotly_chart(
            create_performance_chart(monthly_performance),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("GEARING RATIO TREND", "Quarterly progression vs benchmark")
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Executive Summaries
    st.markdown(
        "<h3 style='margin: 2.5rem 0 1.5rem 0;'>📋 Executive Insights</h3>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        render_summary_card(executive_summaries[0])

        render_summary_card(executive_summaries[2])
    with col2:
        render_summary_card(executive_summaries[1])
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
        render_summary_card(executive_summaries[3])

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    # Recent Workflows Table
    st.markdown(
        "<h3 style='margin: 2.5rem 0 1.5rem 0;'>📝 Recent Workflows</h3>",
        unsafe_allow_html=True,
    )
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=400
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Workflow Analytics Page
elif st.session_state.current_page == "Workflow Analytics":
    st.markdown("# 📊 Workflow Analytics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Detailed analysis of workflow performance and efficiency</p>",
        unsafe_allow_html=True,
    )

    # KPI Summary
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Total Workflows", 1247, 12.5, "up", "number", "📊", 0)
    with col2:
        render_kpi_card("Completed", 1098, 15.2, "up", "number", "✅", 0.1)
    with col3:
        render_kpi_card("Pending", 89, -8.3, "down", "number", "⏳", 0.2)
    with col4:
        render_kpi_card("Failed", 60, -12.1, "down", "number", "❌", 0.3)

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "MONTHLY WORKFLOW DISTRIBUTION", "Status breakdown over time"
        )
        st.plotly_chart(
            create_workflow_bar_chart(workflow_trend_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("COMPLETION TREND", "Success rate progression")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data,
                "Month",
                "Completed",
                "Completed",
                COLORS["success"],
            ),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header("WORKFLOW EXECUTION LOG", "Detailed activity history")
    st.dataframe(
        recent_workflows, use_container_width=True, hide_index=True, height=400
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Financial Metrics Page
elif st.session_state.current_page == "Financial Metrics":
    st.markdown("# 💰 Financial Metrics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Financial performance analysis and volume gearing metrics</p>",
        unsafe_allow_html=True,
    )

    total_revenue = monthly_performance["Revenue"].sum()
    total_profit = monthly_performance["Profit"].sum()
    profit_margin = (total_profit / total_revenue) * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card("Gearing Ratio", 2.45, 8.3, "up", "ratio", "📈", 0)
    with col2:
        render_kpi_card(
            "Total Revenue", total_revenue, 18.5, "up", "currency", "💰", 0.1
        )
    with col3:
        render_kpi_card("Total Profit", total_profit, 24.2, "up", "currency", "💵", 0.2)
    with col4:
        render_kpi_card(
            "Profit Margin", round(profit_margin, 1), 5.8, "up", "percentage", "📊", 0.3
        )

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header(
            "VOLUME GEARING ANALYSIS", "Quarterly performance vs benchmark"
        )
        st.plotly_chart(
            create_area_chart(volume_gearing_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("REVENUE DISTRIBUTION", "By department")
        st.plotly_chart(
            create_donut_chart(department_breakdown),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "FINANCIAL PERFORMANCE OVERVIEW", "Monthly revenue and profit trends"
    )
    st.plotly_chart(
        create_performance_chart(monthly_performance),
        use_container_width=True,
        config=get_chart_config(),
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Productivity Page
elif st.session_state.current_page == "Productivity":
    st.markdown("# 👥 Productivity Metrics")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Department-wise productivity analysis and performance tracking</p>",
        unsafe_allow_html=True,
    )

    avg_score = productivity_data["Score"].mean()
    on_target = (productivity_data["Score"] >= productivity_data["Target"]).sum()
    total_employees = productivity_data["Employees"].sum()
    top_dept = productivity_data.loc[productivity_data["Score"].idxmax()]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Productivity", round(avg_score, 1), 5.2, "up", "percentage", "📈", 0
        )
    with col2:
        render_kpi_card("Depts On Target", on_target, 16.7, "up", "number", "🎯", 0.1)
    with col3:
        render_kpi_card(
            "Total Employees", total_employees, 8.4, "up", "number", "👥", 0.2
        )
    with col4:
        render_kpi_card(
            "Top Score", top_dept["Score"], 3.1, "up", "percentage", "🏆", 0.3
        )

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("DEPARTMENT PRODUCTIVITY", "Score vs Target comparison")
        st.plotly_chart(
            create_horizontal_bar_chart(productivity_data),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        render_chart_header("PRODUCTIVITY TREND", "Monthly output progression")
        st.plotly_chart(
            create_line_chart(
                workflow_trend_data, "Month", "Completed", "Output", COLORS["primary"]
            ),
            use_container_width=True,
            config=get_chart_config(),
        )
        st.markdown("</div>", unsafe_allow_html=True)

    # Insight Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>TOP PERFORMER</h4>
            <div class="insight-value" style="color: {COLORS["success"]};">{top_dept["Department"]}</div>
            <div class="insight-label">{top_dept["Score"]}% productivity score</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>ACHIEVEMENT RATE</h4>
            <div class="insight-value" style="color: {COLORS["primary"]};">{int((on_target / len(productivity_data)) * 100)}%</div>
            <div class="insight-label">{on_target} out of {len(productivity_data)} departments</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>TEAM SIZE</h4>
            <div class="insight-value" style="color: {COLORS["accent"]};">{total_employees}</div>
            <div class="insight-label">Across all departments</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Tech Adoption Page
elif st.session_state.current_page == "Tech Adoption":
    st.markdown("# 💻 Technology Adoption")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2rem;'>Technology stack adoption rates and utilization metrics</p>",
        unsafe_allow_html=True,
    )

    avg_adoption = tech_adoption_data["Adoption"].mean()
    high_adoption = (tech_adoption_data["Adoption"] >= 80).sum()
    low_adoption = (tech_adoption_data["Adoption"] < 60).sum()
    emerging = (tech_adoption_data["Category"] == "Emerging").sum()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        render_kpi_card(
            "Avg Adoption", round(avg_adoption, 1), -2.1, "down", "percentage", "💻", 0
        )
    with col2:
        render_kpi_card("High Adoption", high_adoption, 12.5, "up", "number", "✅", 0.1)
    with col3:
        render_kpi_card("Low Adoption", low_adoption, -25.0, "down", "number", "⚠️", 0.2)
    with col4:
        render_kpi_card("Emerging Tech", emerging, 100, "up", "number", "🚀", 0.3)

    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "TECHNOLOGY ADOPTION ANALYSIS", "Adoption rates with performance thresholds"
    )
    st.plotly_chart(
        create_tech_adoption_chart(tech_adoption_data),
        use_container_width=True,
        config=get_chart_config(),
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    render_chart_header(
        "TECHNOLOGY STACK DETAILS", "Complete tool inventory with adoption metrics"
    )

    # Style the dataframe with colored badges
    styled_data = tech_adoption_data.copy()
    styled_data["Status"] = styled_data["Adoption"].apply(
        lambda x: "🟢 High" if x >= 80 else "🟡 Medium" if x >= 60 else "🔴 Low"
    )
    st.dataframe(styled_data, use_container_width=True, hide_index=True, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

    # Action Items
    st.markdown("<div style='height: 0.75rem;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        low_tools = tech_adoption_data[tech_adoption_data["Adoption"] < 60]
        st.markdown(
            f"""
        <div class="summary-card">
            <div class="summary-card-icon">⚠️</div>
            <div class="summary-card-title">Focus Areas</div>
            <div class="summary-card-content">
                {"".join(f'<p style="margin: 8px 0;">• {row["Tool"]} - {row["Adoption"]}% adoption</p>' for _, row in low_tools.iterrows())}
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
            <h4>TOP PERFORMERS</h4>
            <div style="margin-top: 1rem;">
                {"".join(f'<p style="margin: 12px 0; color: {COLORS["success"]}; font-weight: 600;">✅ {row["Tool"]} - {row["Adoption"]}%</p>' for _, row in high_tools.iterrows())}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Executive Summary Page
elif st.session_state.current_page == "Executive Summary":
    current_date = datetime.now().strftime("%A, %B %d, %Y")

    st.markdown(
        f"""
    <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #475569 100%); 
                color: white; 
                border-radius: 28px; 
                padding: 3rem; 
                margin-bottom: 2.5rem; 
                position: relative; 
                overflow: hidden;
                box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);">
        <div style="position: absolute; top: -50%; right: -20%; width: 60%; height: 200%; 
                    background: radial-gradient(circle, rgba(59, 130, 246, 0.2) 0%, transparent 70%);
                    animation: rotateGradient 15s linear infinite;"></div>
        <div style="position: relative; z-index: 1;">
            <p style="color: #fbbf24; font-size: 14px; font-weight: 700; letter-spacing: 0.15em; margin-bottom: 16px; text-transform: uppercase;">
                📅 {current_date}
            </p>
            <h1 style="color: white !important; margin-bottom: 20px; font-size: 2.5rem; font-weight: 900; letter-spacing: -0.04em;">
                Executive Summary Report
            </h1>
            <p style="color: rgba(255,255,255,0.8); max-width: 800px; line-height: 1.8; font-size: 1.125rem;">
                Comprehensive overview of organizational performance metrics, highlighting key achievements,
                strategic insights, and actionable recommendations for continued growth and excellence.
            </p>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    stats = [
        (
            "📊",
            f"{kpi_data['workflow_count']['value']:,}",
            "Total Workflows",
            COLORS["navy"],
        ),
        (
            "📈",
            str(kpi_data["volume_gearing_ratio"]["value"]),
            "Gearing Ratio",
            COLORS["primary"],
        ),
        (
            "👥",
            f"{kpi_data['productivity']['value']}%",
            "Productivity",
            COLORS["success"],
        ),
        (
            "💻",
            f"{kpi_data['tech_adoption']['value']}%",
            "Tech Adoption",
            COLORS["warning"],
        ),
    ]

    for col, (icon, value, label, color) in zip([col1, col2, col3, col4], stats):
        with col:
            st.markdown(
                f"""
            <div class="insight-card" style="text-align: center; padding: 2rem;">
                <span style="font-size: 2.5rem; display: block; margin-bottom: 1rem;">{icon}</span>
                <div class="insight-value" style="color: {color};">{value}</div>
                <div class="insight-label">{label}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        "<h2 style='margin: 3rem 0 2rem 0;'>📋 Strategic Insights & Analysis</h2>",
        unsafe_allow_html=True,
    )

    for i in range(0, 4, 2):
        col1, col2 = st.columns(2)
        with col1:
            render_summary_card(executive_summaries[i])
        with col2:
            if i + 1 < len(executive_summaries):
                render_summary_card(executive_summaries[i + 1])

    # Action Items
    st.markdown(
        "<h2 style='margin: 3rem 0 2rem 0;'>🎯 Strategic Action Items</h2>",
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>🚀 PRIORITIES</h4>
            <div style="margin-top: 1.5rem;">
                <div style="display: flex; gap: 1rem; padding: 1.25rem; background: linear-gradient(135deg, {COLORS["primary"]}15, {COLORS["accent"]}10); border-radius: 12px; margin-bottom: 1rem; border-left: 4px solid {COLORS["primary"]};">
                    <div style="font-size: 1.5rem; font-weight: 900; color: {COLORS["primary"]};">1</div>
                    <div>
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["navy"]};">Accelerate AI Adoption</div>
                        <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Implement training programs to increase AI assistant adoption from 45% to 70%</div>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; padding: 1.25rem; background: linear-gradient(135deg, {COLORS["success"]}15, {COLORS["accent"]}10); border-radius: 12px; margin-bottom: 1rem; border-left: 4px solid {COLORS["success"]};">
                    <div style="font-size: 1.5rem; font-weight: 900; color: {COLORS["success"]};">2</div>
                    <div>
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["navy"]};">Scale Automation</div>
                        <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Expand workflow automation to reduce manual processing by 30%</div>
                    </div>
                </div>
                <div style="display: flex; gap: 1rem; padding: 1.25rem; background: linear-gradient(135deg, {COLORS["warning"]}15, {COLORS["accent"]}10); border-radius: 12px; border-left: 4px solid {COLORS["warning"]};">
                    <div style="font-size: 1.5rem; font-weight: 900; color: {COLORS["warning"]};">3</div>
                    <div>
                        <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["navy"]};">Department Alignment</div>
                        <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Focus on HR and Marketing to bring productivity above target</div>
                    </div>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card">
            <h4>🏆 KEY ACHIEVEMENTS</h4>
            <div style="margin-top: 1.5rem;">
                <div style="padding: 1.25rem; background: linear-gradient(135deg, {COLORS["success"]}15, {COLORS["success"]}05); border-radius: 12px; margin-bottom: 1rem; border: 2px solid {COLORS["success"]}30;">
                    <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["success"]};">✅ 12.5% Workflow Growth</div>
                    <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Exceeded quarterly targets with significant efficiency gains</div>
                </div>
                <div style="padding: 1.25rem; background: linear-gradient(135deg, {COLORS["primary"]}15, {COLORS["primary"]}05); border-radius: 12px; margin-bottom: 1rem; border: 2px solid {COLORS["primary"]}30;">
                    <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["primary"]};">✅ Gearing Ratio Above Benchmark</div>
                    <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Achieved 2.45 vs 2.2 industry standard</div>
                </div>
                <div style="padding: 1.25rem; background: linear-gradient(135deg, {COLORS["accent"]}15, {COLORS["accent"]}05); border-radius: 12px; border: 2px solid {COLORS["accent"]}30;">
                    <div style="font-weight: 700; margin-bottom: 0.5rem; color: {COLORS["accent"]};">✅ Engineering Excellence</div>
                    <div style="font-size: 0.875rem; color: {COLORS["gray"]};">Engineering department achieved 92.5% productivity score</div>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Reports & Export Page
elif st.session_state.current_page == "Reports & Export":
    st.markdown("# 📥 Reports & Export")
    st.markdown(
        "<p style='color: #64748b; font-size: 1.125rem; margin-bottom: 2.5rem;'>Download comprehensive reports and export data in multiple formats</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 2rem;">
            <div style="width: 64px; height: 64px; background: linear-gradient(135deg, {COLORS["navy"]}, {COLORS["primary"]}); 
                        border-radius: 18px; display: flex; align-items: center; justify-content: center; 
                        margin-bottom: 1.5rem; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.25);">
                <span style="font-size: 2rem;">📄</span>
            </div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">Full Report</h3>
            <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 1.5rem;">
                Complete executive dashboard with all KPIs, charts, and insights in HTML format
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.download_button(
            "📥 Download HTML Report",
            data=generate_html_report(),
            file_name=f"BizView_Executive_Report_{datetime.now().strftime('%Y%m%d')}.html",
            mime="text/html",
            use_container_width=True,
        )

    with col2:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 2rem;">
            <div style="width: 64px; height: 64px; background: linear-gradient(135deg, {COLORS["success"]}, {COLORS["accent"]}); 
                        border-radius: 18px; display: flex; align-items: center; justify-content: center; 
                        margin-bottom: 1.5rem; box-shadow: 0 8px 24px rgba(16, 185, 129, 0.25);">
                <span style="font-size: 2rem;">📊</span>
            </div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">Excel Export</h3>
            <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 1.5rem;">
                All data tables in multi-sheet workbook for advanced analysis and custom reporting
            </p>
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
        )

    with col3:
        st.markdown(
            f"""
        <div class="insight-card" style="padding: 2rem;">
            <div style="width: 64px; height: 64px; background: linear-gradient(135deg, {COLORS["warning"]}, {COLORS["error"]}); 
                        border-radius: 18px; display: flex; align-items: center; justify-content: center; 
                        margin-bottom: 1.5rem; box-shadow: 0 8px 24px rgba(245, 158, 11, 0.25);">
                <span style="font-size: 2rem;">📋</span>
            </div>
            <h3 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">CSV Export</h3>
            <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 1.5rem;">
                Raw data files for integration with external tools and systems
            </p>
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
        )

    # Report Preview with st.components.v1.iframe/html
    st.markdown(
        "<hr style='margin: 2rem 0; border: none; height: 1px; background: linear-gradient(90deg, transparent, #e2e8f0, transparent);'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h2 style='margin-bottom: 1rem; font-size: 1.25rem;'>📄 Report Preview</h2>",
        unsafe_allow_html=True,
    )

    # Use Streamlit Components to render the actual HTML in an iframe
    # This ensures styles don't conflict and it looks exactly like the export
    report_html = generate_html_report()
    st.components.v1.html(report_html, height=800, scrolling=True)

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("<div style='height: 3rem;'></div>", unsafe_allow_html=True)
st.markdown(
    f"""
<div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.8); backdrop-filter: blur(10px); border-radius: 20px; border: 1px solid #e2e8f0;">
    <p style="color: {COLORS["gray"]}; font-size: 0.875rem; margin-bottom: 0.5rem;">
        <strong>BizView Executive Dashboard</strong> • Ultra Premium Edition
    </p>
    <p style="color: {COLORS["gray"]}; font-size: 0.75rem;">
        Powered by Streamlit • {datetime.now().strftime("%Y")} • All Rights Reserved
    </p>
</div>
""",
    unsafe_allow_html=True,
)
