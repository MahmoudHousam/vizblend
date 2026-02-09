import warnings
from importlib import metadata as _version

try:
    version = _version("vizblend")
except Exception:
    version = "unknown" 

if version < "2.0.0":
    warnings.warn(
        f"🚨 VizBlend version {version} is deprecated! Please upgrade to version 2.0.0\n"
        "👉 Run pip install vizblend --upgrade vizblend",
        DeprecationWarning,
        stacklevel=2,
    )
