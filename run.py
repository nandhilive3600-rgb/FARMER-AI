"""
FarmBot AI Application Launcher
Run with: python run.py
"""

import os
import sys
import uvicorn

# Configure UTF-8 for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting FarmBot AI - All-in-One AI Farming Assistant on port {port}...")
    print(f"Access the web application at: http://localhost:{port}")
    print(f"API Documentation at: http://localhost:{port}/docs")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)


