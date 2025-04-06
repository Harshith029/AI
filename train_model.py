import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Create synthetic traffic dataset
def generate_data(samples=2000):
    data = []
    for _ in range(samples):
        hour = np.random.randint(0, 24)
        vehicle_type = np.random.choice(["car", "bike", "truck", "ambulance"])
        weather = np.random.choice(["clear", "rainy"])
        accident_on_route = np.random.choice([0, 1])
        road_condition = np.random.choice(["good", "bad"])
        event_nearby = np.random.choice([0, 1])

        # Simulate congestion score based on time/conditions
        base_score = (
            0.9 if 7 <= hour <= 9 or 17 <= hour <= 19 else 0.3  # peak hours
        ) + 0.2 * (vehicle_type in ["truck", "ambulance"]) \
          + 0.3 * (weather == "rainy") \
          + 0.4 * accident_on_route \
          + 0.2 * (road_condition == "bad") \
          + 0.3 * event_nearby

        congestion_score = min(base_score + np.random.normal(0, 0.1), 1.0)

        data.append([hour, vehicle_type, weather, accident_on_route, road_condition, event_nearby, congestion_score])

    columns = ["hour", "vehicle_type", "weather", "accident_on_route", "road_condition", "event_nearby", "congestion_score"]
    return pd.DataFrame(data, columns=columns)

df = generate_data()

# One-hot encode + preprocess
df = pd.get_dummies(df, columns=["vehicle_type", "weather", "road_condition"])

X = df.drop("congestion_score", axis=1)
y = df["congestion_score"]

# Train pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, "model/congestion_predictor.pkl")

print("✅ Model trained and saved to model/congestion_predictor.pkl")
