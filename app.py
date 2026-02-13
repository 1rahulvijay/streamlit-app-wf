import streamlit as st

import data_generator as dg
import charts as ch
import utils
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# Configuration & Setup
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Executive Dashboard", layout="wide", initial_sidebar_state="expanded"
)

utils.local_css("assets/style.css")

# -----------------------------------------------------------------------------
# State Management (Imitating "Hooks")
# -----------------------------------------------------------------------------
if "data_history" not in st.session_state:
    st.session_state["data_history"] = dg.generate_historical_data()
    st.session_state["data_snapshot"] = dg.generate_department_data()

df_hist = st.session_state["data_history"]
df_dept = st.session_state["data_snapshot"]
kpis = dg.get_kpi_metrics()

# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("📊 Executive Suite")

    page = st.radio(
        "Navigate",
        [
            "Executive Summary",
            "Workflow Analytics",
            "Productivity Deep Dive",
            "Tech Adoption",
        ],
    )

    st.markdown("---")
    st.subheader("Filters")
    selected_dept = st.multiselect(
        "Department",
        df_dept["Department"].unique(),
        default=df_dept["Department"].unique(),
    )

    st.markdown("---")
    if st.button("🖨️ Print / Save PDF"):
        # Inject JS to trigger print dialog
        components.html("<script>window.print()</script>", height=0, width=0)

    st.markdown("---")
    st.caption("v1.0.2 | Corporate Data Office")

# Filter Logic (Simulated)
# In a real app, this would filter the dataframe.
# Here we just show the selection for context.
if len(selected_dept) < len(df_dept["Department"].unique()):
    st.toast(f"Filtering for: {', '.join(selected_dept)}")
    # Simple filter simulation
    df_dept_filtered = df_dept[df_dept["Department"].isin(selected_dept)]
else:
    df_dept_filtered = df_dept

# -----------------------------------------------------------------------------
# Pages
# -----------------------------------------------------------------------------


def show_executive_summary():
    st.markdown("## Executive Summary")
    st.markdown("High-level overview of corporate performance metrics.")

    # KPI Row
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            utils.create_card(
                "Workflow Count",
                utils.format_number(kpis["Workflow Count"][0]),
                kpis["Workflow Count"][1],
            ),
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            utils.create_card(
                "Vol. Gearing Ratio",
                kpis["Volume Gearing Ratio"][0],
                kpis["Volume Gearing Ratio"][1],
            ),
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            utils.create_card(
                "Productivity Score",
                f"{kpis['Productivity Score'][0]}%",
                kpis["Productivity Score"][1],
            ),
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            utils.create_card(
                "Tech Adoption",
                f"{kpis['Tech Adoption Rate'][0]}%",
                kpis["Tech Adoption Rate"][1],
            ),
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Main Charts Row 1
    c1, c2 = st.columns([2, 1])
    with c1:
        st.plotly_chart(
            ch.plot_trend(df_hist, "Month", "Workflow Count", "Monthly Workflow Trend"),
            use_container_width=True,
        )
    with c2:
        st.plotly_chart(
            ch.plot_donut(
                df_dept_filtered["Department"],
                df_dept_filtered["Active Workflows"],
                "Workflows by Dept",
            ),
            use_container_width=True,
        )

    # Main Charts Row 2
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(
            ch.plot_bar_comparison(
                df_dept_filtered,
                "Department",
                ["Staffing Efficiency"],
                "Staffing Efficiency by Dept",
            ),
            use_container_width=True,
        )
    with c2:
        st.plotly_chart(
            ch.plot_trend(
                df_hist, "Month", "Volume Gearing Ratio", "Volume Gearing Ratio Trend"
            ),
            use_container_width=True,
        )


def show_workflow_analytics():
    st.markdown("## Workflow Analytics")

    c1, c2 = st.columns([3, 1])
    with c1:
        st.plotly_chart(
            ch.plot_trend(
                df_hist, "Month", "Workflow Count", "Total Workflows Over Time"
            ),
            use_container_width=True,
        )

    st.markdown("### Departmental Breakdown")
    st.dataframe(df_dept_filtered, use_container_width=True)


def show_productivity():
    st.markdown("## Productivity Deep Dive")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(
            ch.plot_trend(
                df_hist, "Month", "Productivity Score", "Productivity Score Trend"
            ),
            use_container_width=True,
        )
    with c2:
        st.plotly_chart(
            ch.plot_bar_comparison(
                df_dept_filtered,
                "Department",
                ["Avg Completion Time (Days)"],
                "Completion Time (Lower is Better)",
            ),
            use_container_width=True,
        )


def show_tech_adoption():
    st.markdown("## Tech Adoption & Automation")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(
            ch.plot_trend(
                df_hist, "Month", "Tech Adoption Rate", "Tech Adoption Trend"
            ),
            use_container_width=True,
        )
    with c2:
        st.plotly_chart(
            ch.plot_bar_comparison(
                df_dept_filtered,
                "Department",
                ["Automation Level (%)"],
                "Automation Level by Dept",
            ),
            use_container_width=True,
        )


# -----------------------------------------------------------------------------
# Routing
# -----------------------------------------------------------------------------

if page == "Executive Summary":
    show_executive_summary()
elif page == "Workflow Analytics":
    show_workflow_analytics()
elif page == "Productivity Deep Dive":
    show_productivity()
elif page == "Tech Adoption":
    show_tech_adoption()
