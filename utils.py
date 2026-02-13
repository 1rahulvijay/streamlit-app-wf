import streamlit as st
import base64


def local_css(file_name):
    """Loads a local CSS file and injects it into the Streamlit app."""
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def format_number(num):
    """Formats large numbers for display (e.g., 1,200)."""
    if num > 1000000:
        if not num % 1000000:
            return f"{num // 1000000}M"
        return f"{round(num / 1000000, 1)}M"
    return f"{num:,}"


def create_card(title, value, delta, delta_color="inverse"):
    """
    Generates HTML for a custom metric card.

    Args:
        title (str): The metric label.
        value (str/int): The main value to display.
        delta (str/float): The periodic change.
        delta_color (str): 'normal' (green up, red down) or 'inverse' (red up, green down).
                       Default 'inverse' because shorter workflow time is better?
                       Actually depends on metric. Let's make it configurable.
    """

    # Determine color class based on delta
    # Assuming delta is numerical.
    # If delta is a string with %, we parse it? No, let's assume raw delta passed in.

    is_positive = delta >= 0
    delta_str = f"{abs(delta):.1f}"

    if delta_color == "normal":
        color_class = "delta-pos" if is_positive else "delta-neg"
        arrow = "↑" if is_positive else "↓"
    elif delta_color == "inverse":
        color_class = "delta-neg" if is_positive else "delta-pos"
        arrow = "↑" if is_positive else "↓"
    else:  # off
        color_class = ""
        arrow = ""

    html = f"""
    <div class="metric-card">
        <div class="metric-label">{title}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-delta {color_class}">
            {arrow} {delta_str}% vs last month
        </div>
    </div>
    """
    return html
