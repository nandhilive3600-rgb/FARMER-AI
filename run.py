"""
FarmBot AI Application Launcher
Run with: python run.py
"""

import sys
import uvicorn

# Configure UTF-8 for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

if __name__ == "__main__":
    print("Starting FarmBot AI - All-in-One AI Farming Assistant...")
    print("Access the web application at: http://localhost:8000")
    print("API Documentation at: http://localhost:8000/docs")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

