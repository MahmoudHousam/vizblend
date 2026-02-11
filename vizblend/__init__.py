import warnings
from importlib import metadata as _version

from vizblend.create_dashboard import CreateDashboard
from vizblend.create_report import CreateReport

__all__ = ["CreateReport", "CreateDashboard", "version"]

try:
    version = _version("vizblend")
except Exception:
    version = "unknown"

if version < "3.0.0":
    warnings.warn(
        f"🚨 VizBlend version {version} is deprecated! Please upgrade to version 3.0.0\n"
        "👉 Run pip install vizblend --upgrade vizblend",
        DeprecationWarning,
        stacklevel=2,
    )
