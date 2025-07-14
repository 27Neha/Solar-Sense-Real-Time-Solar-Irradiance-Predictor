import requests
import joblib
import sys
import calendar
import pandas as pd

# ✅ OpenWeatherMap API Key
API_KEY = "0a62fc0525c61a0e99364d8e3ac9655b"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ✅ Load trained model and scaler from correct paths
model_path = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\solar_model.pkl"
scaler_path = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\scaler.pkl"

try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
except FileNotFoundError as e:
    print("🚫 ERROR: File not found ->", e)
    sys.exit()

# ✅ App Header
print("=" * 60)
print("🔆  SOLAR SENSE – Real-Time AI Solar Energy Predictor")
print("🌐  Powered by OpenWeatherMap + Machine Learning")
print("=" * 60)

# 🏙️ Get city input
city = input("🏙️  Enter your city : ")

# 📅 Get month input
while True:
    try:
        month = int(input("📅 Enter month number (1-12): "))
        if 1 <= month <= 12:
            break
        else:
            print("⚠️ Please enter a number between 1 and 12.")
    except ValueError:
        print("⚠️ Invalid input. Enter a number (1 for January, etc.)")

# 🌐 Fetch real-time weather data
params = {"q": city, "appid": API_KEY, "units": "metric"}
try:
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("🚫 ERROR: Could not fetch weather data.\nReason:", e)
    sys.exit()

# 🔍 Extract weather data
data = response.json()
temp = data['main']['temp']
humidity = data['main']['humidity']
cloud = data['clouds']['all']

# 🧠 Prepare input for model
features = pd.DataFrame([[month, temp, humidity, cloud]],
                        columns=['Month_Num', 'temperature', 'humidity', 'cloud'])
features_scaled = scaler.transform(features)
predicted_irradiance = model.predict(features_scaled)[0]

# 🔋 Energy Calculation (for 1.5 m² panel, 18% efficiency)
panel_area = 1.5  # in m²
efficiency = 0.18  # 18%
energy_kwh = predicted_irradiance * panel_area * efficiency / 1000  # W to kWh

# 📊 Output Results
print("\n🔍 Real-Time Weather Data:")
print(f"📍 Location: {city.title()}")
print(f"🗓️  Month: {calendar.month_name[month]}")
print(f"🌡️  Temperature: {temp}°C  | 💧 Humidity: {humidity}%  | ☁️ Cloud: {cloud}%")

print("\n📊 AI-Based Prediction:")
print(f"☀️  Solar Irradiance: {predicted_irradiance:.2f} W/m²")
print(f"🔋 Estimated Solar Energy Generation: {energy_kwh:.4f} kWh/day")

# 📢 Insight Based on Irradiance
print("\n📢 Insights:")
if predicted_irradiance > 250:
    print("✅ Excellent solar energy day! Expect high power generation.")
elif 150 < predicted_irradiance <= 250:
    print("⚠️ Fair solar output. Good for moderate energy use.")
else:
    print("🚨 Low output. Weather conditions not favorable for solar generation.")

print("\n🔁 Powered by AI + Real-Time Weather API")
print("✅ Prediction complete. Stay energy smart! ⚡")
print("=" * 60)
