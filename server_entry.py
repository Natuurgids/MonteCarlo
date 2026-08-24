from __future__ import annotations
import os
import sys
from pathlib import Path

def resource_path(name: str) -> str:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return str(base / name)

def main():
    os.environ.setdefault("STREAMLIT_BROWSER_GATHER_USAGE_STATS", "false")
    from streamlit.web import bootstrap
    app_path = resource_path("app.py")
    flag_options = {
        "server.address": "0.0.0.0",
        "server.port": 8501,
        "server.headless": True,
        "browser.gatherUsageStats": False,
    }
    bootstrap.run(app_path, False, [], flag_options)

if __name__ == "__main__":
    main()
