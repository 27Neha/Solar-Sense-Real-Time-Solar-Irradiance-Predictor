# ☀️ Solar Sense – Real-Time Solar Irradiance Predictor

Welcome to **Solar Sense**, an AI-powered tool that predicts **solar irradiance** in real time using **machine learning** and **weather simulation or live data**. Designed with sustainability and clean energy in mind, this project is perfect for energy analysts, solar panel users, researchers, and smart city planners.

---

## 📌 Project Objective

To create a reliable and intelligent system that predicts solar energy potential across **Indian states** using:
- Historical solar irradiance data
- Simulated weather features
- Real-time weather via API

This helps in making **energy-efficient decisions**, **power forecasting**, and **resource planning** for solar energy usage.

---

## 🌟 Key Features

- 🔍 Accurate solar irradiance prediction using **Random Forest Regression**
- 🌤️ Simulated weather inputs (Temperature, Humidity, Wind, Cloud Cover)
- 📡 Real-time weather integration via **OpenWeatherMap API**
- 📈 Scaled predictions using `MinMaxScaler`
- 🎨 Clean and interactive **Streamlit UI**
- ⚡ Customizable and ready for deployment

---

## 🔍 The 3 Approaches We Tried

| Approach | Description | Outcome |
|---------|-------------|---------|
| **1. Static Model** | Trained on raw state-wise solar data | Basic predictions but lacked real-world variability |
| **2. Simulated Weather** | Introduced simulated weather features | Better prediction accuracy, more realistic but initially had overfitting issues |
| **3. Real-Time Weather API** | Integrated OpenWeatherMap API | Most dynamic and accurate; ready for deployment |

---

## 👥 Who Will Benefit From This?

| Stakeholder | Benefits |
|-------------|----------|
| 🏢 **Energy Companies** | Efficient load balancing, energy forecasting |
| 🧪 **Researchers & Students** | Real-world ML application with weather data |
| 🏠 **Solar Panel Users** | Know when solar energy is optimal to use |
| 🏙️ **Smart Cities / Planners** | Sustainable planning with solar potential insight |
| 🌱 **Environment Advocates** | Promotes clean, renewable energy usage |

---

## 🚀 How to Run Locally

1. **Clone the Repo**
   ```bash
   git clone https://github.com/yourusername/solar-sense.git
   cd solar-sense
Install Requirements

bash
Copy
Edit
pip install -r requirements.txt
Run the App

bash
Copy
Edit
streamlit run app.py
(Optional): Add your OpenWeatherMap API key in .env or directly in the code.

## 🌐 Deployment Scope
This project is Streamlit-ready, and you can deploy it on:

🟦 Streamlit Cloud

🐳 Docker

☁️ Heroku / Railway / Render

## Future Scope:

Model retraining with historical + real-time data

Support for more countries

User login and usage dashboard
