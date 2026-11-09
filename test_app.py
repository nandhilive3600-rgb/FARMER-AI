import asyncio
import sys
import os

# Set UTF-8 encoding for Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

import httpx
from starlette.testclient import TestClient
from app.main import app

def main():
    print("🌾 Testing FarmBot AI backend endpoints...")
    client = TestClient(app)

    # 1. Health endpoint
    r = client.get("/health")
    assert r.status_code == 200, f"Health check failed: {r.status_code}"
    print("✅ /health OK:", r.json())

    # 2. Districts endpoint
    r = client.get("/api/weather/districts")
    assert r.status_code == 200, f"Districts failed: {r.status_code}"
    districts = r.json().get("districts", [])
    print(f"✅ /api/weather/districts OK: loaded {len(districts)} agricultural districts.")

    # 3. Live Weather Forecast endpoint (Open-Meteo)
    print("🌦️ Testing live Open-Meteo forecast API call...")
    r = client.get("/api/weather/forecast?lat=10.7867&lon=76.6548&crop=Paddy&lang=en")
    assert r.status_code == 200, f"Weather forecast failed: {r.status_code}"
    w_data = r.json()
    cur = w_data["current"]
    print(f"✅ /api/weather/forecast OK: Temp={cur['temperature']}°C, Condition={cur['condition_en']}, Humidity={cur['humidity']}%, Wind={cur['wind_speed']} km/h")
    print(f"   Daily cards: {len(w_data['daily'])}, Alerts: {len(w_data['alerts'])}")

    # 4. Profit & Loss Calculator endpoint
    pl_payload = {
        "crop_name": "Paddy",
        "land_area": 1.5,
        "expected_yield": 30.0,
        "selling_price_per_quintal": 2820.0,
        "seed_cost": 3000.0,
        "fertilizer_cost": 6000.0,
        "pesticide_cost": 2000.0,
        "labor_cost": 15000.0,
        "machinery_cost": 7000.0
    }
    r = client.post("/api/calculators/profit-loss", json=pl_payload)
    assert r.status_code == 200
    pl_res = r.json()
    print(f"✅ /api/calculators/profit-loss OK: Revenue=₹{pl_res['gross_revenue']}, Cost=₹{pl_res['total_cost']}, Net Profit=₹{pl_res['net_profit']}")

    # 5. Fertilizer NPK Bags Calculator
    fert_payload = {"crop_id": "paddy", "land_area_acres": 2.0}
    r = client.post("/api/calculators/fertilizer-quantity", json=fert_payload)
    assert r.status_code == 200
    fert_res = r.json()["fertilizers_needed"]
    print(f"✅ /api/calculators/fertilizer-quantity OK: Urea={fert_res['urea_bags_50kg']} bags, DAP={fert_res['dap_bags_50kg']} bags, MOP={fert_res['mop_bags_50kg']} bags")

    # 6. Land Area Converter
    r = client.post("/api/calculators/land-convert", json={"value": 50, "from_unit": "cents"})
    assert r.status_code == 200
    land_res = r.json()["converted"]
    print(f"✅ /api/calculators/land-convert OK: 50 cents = {land_res['acres']} acres = {land_res['sq_ft']} sq ft")

    # 7. Market Prices
    r = client.get("/api/market/prices")
    assert r.status_code == 200
    print(f"✅ /api/market/prices OK: loaded {len(r.json()['commodities'])} commodity mandi rates.")

    # 8. AI Chat Assistant
    r = client.post("/api/assistant/chat", json={"message": "What is the fertilizer schedule for paddy?", "language": "en"})
    assert r.status_code == 200
    print(f"✅ /api/assistant/chat OK: reply: {r.json()['reply'][:75]}...")

    # 9. Malayalam AI Chat Assistant
    r = client.post("/api/assistant/chat", json={"message": "നെല്ലിലെ കീടബാധ എങ്ങനെ തടയാം?", "language": "ml"})
    assert r.status_code == 200
    print(f"✅ /api/assistant/chat (Malayalam) OK: reply: {r.json()['reply'][:75]}...")

    # 10. Static index.html check
    r = client.get("/")
    assert r.status_code == 200
    assert "FarmBot AI" in r.text
    print("✅ Static index.html served successfully at root (/)!")

    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! FarmBot AI is fully operational.")

if __name__ == "__main__":
    main()
