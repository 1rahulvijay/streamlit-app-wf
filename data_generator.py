import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_historical_data(months=12):
    """Generates monthly historical data for the executive dashboard."""
    dates = [datetime.today() - timedelta(days=30 * i) for i in range(months)][::-1]
    dates = [d.strftime("%b %Y") for d in dates]

    data = {
        "Month": dates,
        "Workflow Count": np.random.randint(150, 500, size=months),
        "Volume Gearing Ratio": np.random.uniform(1.2, 5.0, size=months).round(2),
        "Productivity Score": np.random.uniform(75, 98, size=months).round(1),
        "Tech Adoption Rate": np.linspace(40, 85, num=months)
        + np.random.normal(0, 2, size=months),
    }

    # Add some seasonality/trend
    for i in range(months):
        data["Workflow Count"][i] += i * 10  # Upward trend
        data["Tech Adoption Rate"][i] = min(100, max(0, data["Tech Adoption Rate"][i]))

    return pd.DataFrame(data)


def generate_department_data():
    """Generates snapshot data breakdown by department."""
    departments = ["Finance", "HR", "Operations", "Sales", "IT"]

    data = []
    for dept in departments:
        data.append(
            {
                "Department": dept,
                "Active Workflows": np.random.randint(20, 100),
                "Avg Completion Time (Days)": round(np.random.uniform(2, 10), 1),
                "Automation Level (%)": np.random.randint(30, 90),
                "Staffing Efficiency": round(np.random.uniform(0.7, 1.2), 2),
            }
        )

    return pd.DataFrame(data)


def get_kpi_metrics():
    """Returns top-level KPIs for the cards."""
    # Simulating "current" vs "previous" for deltas
    current_workflow = np.random.randint(450, 500)
    prev_workflow = np.random.randint(400, 480)

    current_gearing = np.random.uniform(4.0, 5.0)
    prev_gearing = np.random.uniform(3.5, 4.5)

    current_prod = np.random.uniform(88, 95)
    prev_prod = np.random.uniform(85, 92)

    current_tech = np.random.uniform(80, 88)
    prev_tech = np.random.uniform(75, 82)

    return {
        "Workflow Count": (
            current_workflow,
            ((current_workflow - prev_workflow) / prev_workflow) * 100,
        ),
        "Volume Gearing Ratio": (
            round(current_gearing, 2),
            ((current_gearing - prev_gearing) / prev_gearing) * 100,
        ),
        "Productivity Score": (
            round(current_prod, 1),
            current_prod - prev_prod,
        ),  # Absolute delta for percentage
        "Tech Adoption Rate": (
            round(current_tech, 1),
            current_tech - prev_tech,
        ),  # Absolute delta
    }
