# live_predictor.py

import joblib
import sys

# ✅ Updated path to your model
model_path = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\solar_model.pkl"

# Load model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print("🚫 ERROR: Trained model not found at given path.")
    print(f"🔍 Checked path: {model_path}")
    sys.exit()

# Welcome Banner
print("="*50)
print("🔆  SOLAR SENSE - Real-Time Solar Irradiance Predictor")
print("📊  Powered by AI | Built in Python")
print("="*50)

# Get user inputs
try:
    month = int(input("📅 Enter month number (1-12): "))
    temperature = float(input("🌡️  Temperature (°C): "))
    humidity = float(input("💧 Humidity (%): "))
    cloud = float(input("☁️  Cloud Cover (%): "))
except ValueError:
    print("⚠️  Please enter numeric values only.")
    sys.exit()

# Validate input
if not (1 <= month <= 12):
    print("🚫 Month must be between 1 and 12.")
    sys.exit()

if not (0 <= humidity <= 100 and 0 <= cloud <= 100):
    print("⚠️  Humidity and Cloud values must be between 0% and 100%.")
    sys.exit()

# Predict
input_data = [[month, temperature, humidity, cloud]]
predicted_irradiance = model.predict(input_data)[0]

# Display result
print("\n🧠 Analyzing weather conditions...")
print("🔍 AI Model in action...")

print(f"\n☀️  Estimated Solar Irradiance: {predicted_irradiance:.2f} W/m²")
if predicted_irradiance > 250:
    print("✅ Great day for solar generation! Panels will perform well.")
elif 150 < predicted_irradiance <= 250:
    print("⚠️ Moderate solar output. Weather might be cloudy.")
else:
    print("🚨 Low solar output expected. Heavy clouds or high humidity likely.")

print("\n✅ Prediction Complete. Stay solar-smart! ⚡")
print("="*50)
