import math
import os
from importlib.resources import files

from jinja2 import Environment, FileSystemLoader

from vizblend.figure_defaults import figure_defaults


def _get_figure_title(fig):
    """Extract title from a Plotly figure layout."""
    title = getattr(fig.layout, "title", None)
    if title is None:
        return ""
    if isinstance(title, dict):
        return title.get("text", "") or ""
    if hasattr(title, "text"):
        return getattr(title, "text", "") or ""
    return str(title)


class CreateDashboard:
    """Build a paginated dashboard (grid + expand) from Plotly figures."""

    CHARTS_PER_PAGE = 6  # max 2 rows x 3 columns

    def __init__(self, dashboard_title: str, logo_path: str = None):
        self.dashboard_title = dashboard_title
        self.logo_path = logo_path
        self.figures = []

    def add_figure(self, fig_or_func, options: dict):
        if callable(fig_or_func):
            fig = fig_or_func(options)
        else:
            fig = fig_or_func

        @figure_defaults()
        def figure_defaults_wrapper(fig, options):
            return fig

        styled_figure = figure_defaults_wrapper(fig, options)
        self.figures.append(styled_figure)

    def blend_graphs_to_html(self):
        if not self.figures:
            raise ValueError("Add at least one figure with add_figure() before calling blend_graphs_to_html().")

        # Build chart data: HTML snippet + title per figure
        chart_items = []
        for fig in self.figures:
            # Ensure chart has a height if not set (match card height)
            if not hasattr(fig.layout, 'height') or fig.layout.height is None:
                fig.update_layout(height=380)
            
            div = fig.to_html(
                full_html=False,
                include_plotlyjs=False,
                config={"displayModeBar": False},
            )
            title = _get_figure_title(fig)
            chart_items.append({"html": div, "title": title or "Chart"})

        # Paginate: 6 charts per page
        total_charts = len(chart_items)
        total_pages = math.ceil(total_charts / self.CHARTS_PER_PAGE)
        pages = []
        for p in range(total_pages):
            start = p * self.CHARTS_PER_PAGE
            end = min(start + self.CHARTS_PER_PAGE, total_charts)
            pages.append(chart_items[start:end])

        templates_dir = files("vizblend").joinpath("templates")
        env = Environment(loader=FileSystemLoader(templates_dir))
        template = env.get_template("dashboard_template.html")

        html_content = template.render(
            pages=pages,
            total_pages=total_pages,
            dashboard_name=self.dashboard_title,
            logo_path=self.logo_path,
        )

        output_dir = "./"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        safe_name = "".join(c if c.isalnum() or c in " -_" else "_" for c in self.dashboard_title)
        output_file = os.path.join(output_dir, f"{safe_name.strip() or 'dashboard'}.html")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_file
