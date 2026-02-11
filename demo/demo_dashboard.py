"""Demo: build a dashboard (grid + pagination + expand) from Plotly figures."""

import plotly.graph_objects as go
from vizblend import CreateDashboard

bar_options = {"title": "Bar Graph"}
bar_fig = go.Figure(go.Bar(x=["A", "B", "C"], y=[3, 1, 2], text=[3, 1, 2]))

scatter_options = {"title": "Scatter Graph"}
scatter_fig = go.Figure(
    go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16], mode="lines+markers")
)

pie_options = {"title": "Pie Graph"}
pie_fig = go.Figure(
    go.Pie(labels=["Apples", "Bananas", "Cherries"], values=[30, 20, 50])
)

box_options = {"title": "Box Graph"}
box_fig = go.Figure(go.Box(y=[10, 15, 20, 25, 30, 35, 40], boxpoints="all", jitter=0.3))

if __name__ == "__main__":
    dashboard = CreateDashboard(
        dashboard_title="Example Dashboard",
        logo_path="Logo_TV_2015.svg.png",
    )
    dashboard.add_figure(bar_fig, bar_options)
    dashboard.add_figure(scatter_fig, scatter_options)
    dashboard.add_figure(pie_fig, pie_options)
    dashboard.add_figure(box_fig, box_options)
    # Add 5 more so we get 2 pages (6 + 3)
    for i in range(5):
        opts = {"title": f"Extra Chart {i + 1}"}
        f = go.Figure(go.Bar(x=["X", "Y"], y=[10 + i, 20 - i]))
        dashboard.add_figure(f, opts)

    out = dashboard.blend_graphs_to_html()
    print(f"Dashboard saved to {out}")
