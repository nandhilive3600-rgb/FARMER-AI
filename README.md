# 🌱 FarmBot AI – All-in-One AI Farming Assistant
> **Your Smart Farming Companion • One platform. Complete farming assistance.**

FarmBot AI (also branded as **SHAZINFARMER AI**) is a complete, farmer-friendly, bilingual digital agriculture assistant. Built with **Python FastAPI** and a modern responsive web frontend, it delivers real-time weather analytics, automated farming alerts, agricultural math utilities, government schemes, Mandi market trends, and an interactive voice & chat assistant in both **English and Malayalam (മലയാളം)**.

---

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.10+
- Web browser (Chrome, Edge, Safari, or Firefox)

### 2. Installation
Open your terminal in `d:\SHAZINFARMER AI` and install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Start the Application
Run the launcher script:
```bash
python run.py
```
Or start with uvicorn directly:
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Access the App
- **Web App**: Open [http://localhost:8000](http://localhost:8000) on your desktop or mobile browser.
- **Interactive API Documentation (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Mobile Access**: Connect your phone to the same Wi-Fi and open `http://<your-computer-ip>:8000`.

---

## 🌾 Features & Integrated Modules

### 1. 🌦️ Weather Information Center (Priority Module)
- **Live 7-Day Forecast**: Direct Open-Meteo API integration providing temperatures, rain probability %, precipitation sum in mm, wind speeds, and WMO condition codes.
- **Location & Geolocation**: Preset agricultural districts (Palakkad, Wayanad, Idukki, Thrissur, Alappuzha, Kottayam, Kozhikode, etc.) plus one-click **GPS Location** detection.
- **Automated Agricultural Alerts**:
  - *Strong Wind Alert*: Warns against foliar spraying to prevent drift and advises propping banana crops.
  - *Heavy Rain Advisory*: Warns against chemical fertilizer loss and waterlogging.
  - *High Heat Alert*: Advises early morning irrigation and mulching.
  - *High Humidity Alert*: Flags fungal blight and downey mildew risk.
- **Crop-Specific Weather Advice**: Tailored recommendations for Paddy, Banana, Coconut, Pepper, and Vegetables.
- **24-Hour Trend Chart**: Interactive temperature and precipitation probability curve.

### 2. 🤖 AI Chat & Voice Assistant
- Conversational agronomist answering agronomy, pest control, and fertilizer questions.
- **Web Speech API Integration**:
  - 🎙️ Microphone voice input (Speech-to-Text) in English (`en-IN`) and Malayalam (`ml-IN`).
  - 🔊 Audio speech output (Text-to-Speech) for hands-free listening in the field.
- Quick question chips for one-tap answers.

### 3. 🧮 Agricultural Utilities & Calculators (5 Tools)
1. **Profit & Loss Calculator**: Area, expected yield, market rate, and itemized input costs $\rightarrow$ Net profit, margin %, and ROI.
2. **Seed Rate Calculator**: Seed quantity and spacing recommendations for Paddy, Maize, Banana, Tomato, Chilli, Okra, Ginger, and Groundnut.
3. **Fertilizer Quantity (NPK to 50kg Bags)**: Translates N-P-K nutrient targets into exact 50kg bags of Urea, DAP, and MOP plus Farmyard Manure (FYM), with a 3-stage application schedule.
4. **Land Area Converter**: Instant conversions between Cents, Acres, Hectares, Ares, Guntha, and Square Feet.
5. **Agricultural Unit Converter**: Instant conversion between Quintals, Metric Tonnes, Kilograms, and Pounds.

### 4. 📈 Market Values & Mandi Center
- Daily modal prices, min/max ranges, and 7-day price trends for key agricultural commodities:
  - Natural Rubber (RSS-4), Paddy (Jyothi/Uma), Black Pepper Garbled, Small Cardamom (8mm), Coconut De-husked, Banana (Nendran), Arecanut, and Green Ginger.
  - Nearby Mandis directory with distances, opening days, and contact numbers.
  - Links to official government trade portals (e-NAM and Agmarknet).

### 5. 🌿 Smart Fertilizers Management
- Guidance for Urea, DAP, Potash (MOP), and Neem Cake.
- Traditional bio-fertilizer and compost preparation recipes:
  - *Jeevamrutha* (Liquid Bio-fertilizer)
  - *Panchagavya* (Growth Booster)
  - *Vermicompost* (Earthworm composting)

### 6. 🚜 Agricultural Tools & Equipment
- Equipment directory: Power Tillers, Multi-purpose Brush Cutters, Drone Sprayers, 16L Battery Sprayers, and Mini Tractors.
- Custom Hiring Centers (CHC) hourly and daily rental rates.
- Sub-Mission on Agricultural Mechanization (SMAM) government subsidy guide.

### 7. 🏛️ Government Schemes & Subsidies
- Comprehensive profiles for:
  - **PM-KISAN** (₹6,000 annual direct income support)
  - **PMFBY** (Pradhan Mantri Fasal Bima Yojana - Crop insurance)
  - **Subhiksha Keralam** (Fallow land cultivation subsidy)
  - **PM-KUSUM** (Up to 60% subsidy for solar water pumps)
  - **KCC** (Kisan Credit Card 4% interest loans)
  - **SMAM** (Machinery purchase subsidies)
- Detailed eligibility, required documents, and one-click buttons to official application portals.

### 8. 🌾 Crops, Soil Health & Pest Diagnosis
- **Soil pH Health & Liming Calculator**: Enter soil pH to calculate exact Agricultural Lime or Gypsum dosages per acre.
- **Pest & Disease Diagnosis**: Visual symptoms, organic biocontrol remedies, and chemical treatment guidelines for:
  - Rice Blast (*Pyricularia oryzae*)
  - Banana Sigatoka Leaf Spot
  - Tomato/Chilli Leaf Curl Virus (Whitefly vector)
  - Coconut Rhinoceros Beetle (*Oryctes rhinoceros*)

---

## 🌐 Multilingual Architecture
- Instant language toggle between **English** and **Malayalam (മലയാളം)**.
- All metrics, navigation labels, alerts, fertilizer recipes, government scheme profiles, and market updates switch seamlessly without reloading the page.

---

## 🧪 Testing the Application
Run the automated test suite anytime to verify backend services and external APIs:
```bash
python test_app.py
```

