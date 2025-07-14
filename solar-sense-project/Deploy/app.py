import streamlit as st
import joblib
import requests
import numpy as np

# ---------------- CONFIG ----------------
API_KEY = "0a62fc0525c61a0e99364d8e3ac9655b"  # Your OpenWeatherMap API Key
MODEL_PATH = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\solar_model.pkl"
SCALER_PATH = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\scaler.pkl"

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Solar Sense", layout="centered")
st.title("🔆 Solar Sense – Real-Time AI Solar Energy Predictor")
st.markdown("🌐 **Powered by OpenWeatherMap + Machine Learning**")
st.markdown("---")

# ---------------- USER INPUT ----------------
city = st.text_input("🏙️ Enter your city", placeholder="e.g. Pune")
month = st.selectbox("📅 Select month", list(range(1, 13)))

if st.button("🔍 Predict"):
    try:
        # ---------------- FETCH WEATHER ----------------
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        weather_data = response.json()

        if response.status_code != 200:
            raise Exception(weather_data.get("message", "API error"))

        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']

        # Simulate random cloud cover for presentation purposes (until real values vary)
        import random
        cloud = random.randint(0, 80)  # simulate 0–80% cloud cover

        # ---------------- LOAD MODEL ----------------
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

        features = np.array([[month, temp, humidity, cloud]])
        features_scaled = scaler.transform(features)
        predicted_irradiance = model.predict(features_scaled)[0]
        predicted_irradiance = round(predicted_irradiance, 2)

        # ---------------- DISPLAY ----------------
        st.markdown("## 🔍 Real-Time Weather Data")
        st.write(f"📍 **Location:** {city.title()}")
        st.write(f"🌡️ **Temperature:** {temp} °C")
        st.write(f"💧 **Humidity:** {humidity} %")
        st.write(f"☁️ **Cloud Cover:** {cloud} %")

        st.markdown("## 📊 AI-Based Prediction")
        st.write(f"☀️ **Solar Irradiance:** {predicted_irradiance} W/m²")

        # Assume 0.027 kWh per 100W irradiance (hypothetical)
        estimated_energy = round((predicted_irradiance / 1000) * 0.27, 4)
        st.write(f"🔋 **Estimated Solar Energy Generation:** {estimated_energy} kWh/day")

        st.markdown("## 💡 Insights")
        if predicted_irradiance < 250:
            st.warning("🚨 Low output. Weather conditions not favorable for solar generation.")
        elif predicted_irradiance < 500:
            st.info("☁️ Moderate output. Partially favorable conditions.")
        else:
            st.success("✅ Good solar conditions! Efficient generation expected.")

    except Exception as e:
        st.error(f"🚫 Could not fetch weather data.\n\nReason: {e}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🔁 **Made with ❤️ by Neha Mahajan** | Stay energy smart! ⚡")
