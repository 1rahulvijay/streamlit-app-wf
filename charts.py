import plotly.graph_objects as go
import plotly.express as px

# Theme Colors
COLOR_NAVY = "#0A192F"
COLOR_LIGHT_NAVY = "#172A45"
COLOR_BLUE = "#64FFDA"  # Teal/Mint accent
COLOR_GREY = "#8892b0"
COLOR_WHITE = "#FFFFFF"
COLOR_GRID = "#E5E7EB"


def apply_theme(fig):
    """Applies the custom Dashboard theme to a Plotly figure."""
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter, sans-serif", "color": COLOR_NAVY},
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(
            showgrid=False, linecolor=COLOR_GRID, tickfont=dict(color=COLOR_GREY)
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLOR_GRID,
            gridwidth=0.5,
            tickfont=dict(color=COLOR_GREY),
        ),
        title_font=dict(size=18, color=COLOR_NAVY, family="Inter, sans-serif"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def plot_trend(df, x_col, y_col, title):
    """Creates a sleek line chart."""
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df[x_col],
            y=df[y_col],
            mode="lines+markers",
            line=dict(color=COLOR_NAVY, width=3, shape="spline"),
            marker=dict(size=6, color=COLOR_BLUE, line=dict(width=2, color=COLOR_NAVY)),
            name=y_col,
            fill="tozeroy",
            fillcolor="rgba(10, 25, 47, 0.05)",  # Very faint navy fill
        )
    )

    fig.update_layout(title=title)
    return apply_theme(fig)


def plot_bar_comparison(df, x_col, y_cols, title):
    """Creates a grouped bar chart."""
    fig = go.Figure()

    colors = [COLOR_NAVY, "#2E5C8A", "#5C8BB8", "#8ABBE6"]  # Shades of navy/blue

    for i, col in enumerate(y_cols):
        fig.add_trace(
            go.Bar(
                x=df[x_col],
                y=df[col],
                name=col,
                marker_color=colors[i % len(colors)],
                text=df[col],
                textposition="auto",
            )
        )

    fig.update_layout(title=title, barmode="group")
    return apply_theme(fig)


def plot_donut(labels, values, title):
    """Creates a donut chart."""
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.6,
                marker=dict(colors=[COLOR_NAVY, COLOR_BLUE, "#CCD6F6", "#8892b0"]),
                textinfo="percent+label",
                hoverinfo="label+percent+value",
            )
        ]
    )

    fig.update_layout(title=title)
    return apply_theme(fig)


def plot_area_stack(df, x_col, y_cols, title):
    """Creates a stacked area chart."""
    fig = go.Figure()

    colors = [COLOR_NAVY, "#1D3557", "#457B9D", "#A8DADC"]

    for i, col in enumerate(y_cols):
        fig.add_trace(
            go.Scatter(
                x=df[x_col],
                y=df[col],
                mode="lines",
                line=dict(width=0),
                stackgroup="one",
                name=col,
                fillcolor=colors[i % len(colors)],
            )
        )

    fig.update_layout(title=title)
    return apply_theme(fig)
