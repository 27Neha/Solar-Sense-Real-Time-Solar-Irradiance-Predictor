import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import joblib

# Load dataset
data_path = r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\Dataset\solar_irradiance_india.csv"
df = pd.read_csv(data_path)

# Clean column names
df.columns = df.columns.str.strip()
df['States'] = df['States'].str.strip().str.lower()

# Month mapping
month_map = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

# Reshape data
monthly_cols = list(month_map.keys())
df_melted = df.melt(id_vars=['States', 'Latitude', 'Longitude'],
                    value_vars=monthly_cols,
                    var_name='Month', value_name='Solar_Irradiance')
df_melted.dropna(subset=['Solar_Irradiance'], inplace=True)
df_melted['Month_Num'] = df_melted['Month'].map(month_map)

# ✅ Simulate diverse weather data
np.random.seed(42)
df_melted['temperature'] = np.random.uniform(15, 45, len(df_melted))
df_melted['humidity'] = np.random.uniform(10, 95, len(df_melted))
df_melted['cloud'] = np.random.uniform(0, 100, len(df_melted))

# ⚠️ REMOVE this line if present:
# df_melted['Solar_Irradiance'] = np.clip(df_melted['Solar_Irradiance'], 100, 900)

# Features & target
X = df_melted[['Month_Num', 'temperature', 'humidity', 'cloud']]
y = df_melted['Solar_Irradiance']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Compare models
models = {
    "Random Forest": RandomForestRegressor(n_estimators=150, random_state=42),
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42)
}

best_model = None
best_score = -np.inf

print("\n🔍 Model Comparison (R² Scores):")
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = r2_score(y_test, preds)
    print(f"{name}: {score:.3f}")
    if score > best_score:
        best_score = score
        best_model = model
        best_model_name = name

# Save
joblib.dump(best_model, r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\solar_model.pkl")
joblib.dump(scaler, r"C:\Users\nehaa\OneDrive\Desktop\solar-sense-project\solar_model.py\scaler.pkl")

print(f"\n✅ Best Model: {best_model_name} (R²: {best_score:.3f})")
print("💾 Model and scaler saved successfully.")
