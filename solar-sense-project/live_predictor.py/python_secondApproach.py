# live_predictor.py

import joblib
import sys

# Month-wise simulated weather profiles (avg India trends)
seasonal_weather = {
    1:  {"temp": 23, "humidity": 60, "cloud": 40},
    2:  {"temp": 26, "humidity": 55, "cloud": 35},
    3:  {"temp": 30, "humidity": 50, "cloud": 30},
    4:  {"temp": 34, "humidity": 40, "cloud": 25},
    5:  {"temp": 37, "humidity": 35, "cloud": 20},  # Peak Summer
    6:  {"temp": 33, "humidity": 65, "cloud": 70},  # Monsoon onset
    7:  {"temp": 30, "humidity": 75, "cloud": 80},  # Monsoon
    8:  {"temp": 29, "humidity": 70, "cloud": 75},
    9:  {"temp": 31, "humidity": 60, "cloud": 60},
    10: {"temp": 28, "humidity": 50, "cloud": 45},
    11: {"temp": 26, "humidity": 50, "cloud": 35},
    12: {"temp": 24, "humidity": 55, "cloud": 40}
}

# Labels for month and season
month_labels = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]

seasonal_tips = {
    "Summer": "☀️ Excellent season for solar generation. Maximize usage!",
    "Winter": "⚠️ Fair performance. Cold but clear skies help.",
    "Monsoon": "🌧️ Low output expected due to clouds and high humidity.",
    "Transition": "🔄 Variable output. Good for hybrid systems."
}

# Load model
model_path = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\solar_model.pkl"
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print("🚫 Model not found. Check path:", model_path)
    sys.exit()

# Ask month only
print("="*55)
print("🔆  SOLAR SENSE – Seasonal Solar Energy Forecaster")
print("📊  Real-time Insight Based on Monthly Weather Trends")
print("="*55)

try:
    month = int(input("📅 Enter month number (1–12): "))
    if month < 1 or month > 12:
        raise ValueError
except ValueError:
    print("❌ Please enter a valid month (1–12)")
    sys.exit()

# Simulated weather for that month
weather = seasonal_weather[month]
features = [[month, weather["temp"], weather["humidity"], weather["cloud"]]]
prediction = model.predict(features)[0]

# Interpret season
if month in [3, 4, 5]:
    season = "Summer"
elif month in [6, 7, 8]:
    season = "Monsoon"
elif month in [1, 2, 11, 12]:
    season = "Winter"
else:
    season = "Transition"

# Output
print(f"\n📅 Month: {month_labels[month - 1]}")
print(f"🌡️  Simulated Temp: {weather['temp']}°C")
print(f"💧 Humidity: {weather['humidity']}%")
print(f"☁️ Cloud Cover: {weather['cloud']}%")
print(f"\n☀️ Predicted Irradiance: **{prediction:.2f} W/m²**")
print(f"\n🔍 {seasonal_tips[season]}")
print("="*55)
2