# ===========================
# Full AI Traffic Prediction with .pkl Support
# Includes data generation, model training, saving/loading model
# ===========================

import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

# ===========================
# STEP 1: Generate Sample Traffic Data (simulate real-world features)
# ===========================
def generate_sample_traffic_data(n=1000):
    np.random.seed(42)
    data = {
        'hour_of_day': np.random.randint(0, 24, n),
        'day_of_week': np.random.randint(0, 7, n),
        'vehicle_count': np.random.randint(50, 200, n),
        'weather_condition': np.random.randint(0, 4, n),  # 0: Clear, 1: Rainy, etc.
        'accident': np.random.randint(0, 2, n),
        'school_zone': np.random.randint(0, 2, n),
        'office_zone': np.random.randint(0, 2, n),
        'congestion_level': np.random.randint(10, 100, n)  # Simulated label
    }
    return pd.DataFrame(data)

# ===========================
# STEP 2: Train Model & Evaluate
# ===========================
def train_model(df):
    X = df.drop('congestion_level', axis=1)
    y = df['congestion_level']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Model trained successfully ✅")
    print(f"RMSE on test data: {rmse:.2f}")
    return model

# ===========================
# STEP 3: Save Model to .pkl File
# ===========================
def save_model(model, path='traffic_model.pkl'):
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {path} 🧠")

# ===========================
# STEP 4: Load Model from .pkl File
# ===========================
def load_model(path='traffic_model.pkl'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}")
    with open(path, 'rb') as f:
        model = pickle.load(f)
    print(f"Model loaded from {path} 📦")
    return model

# ===========================
# STEP 5: Predict Congestion Level for New Data
# ===========================
def predict_congestion(model, input_data):
    prediction = model.predict(input_data)
    return prediction

# ===========================
# MAIN PIPELINE
# ===========================
if __name__ == "__main__":
    print("\n🚦 Starting Traffic Congestion Prediction Pipeline 🚦\n")

    # Step 1: Generate and visualize data
    df = generate_sample_traffic_data(1000)
    print("Sample data preview:")
    print(df.head())

    # Step 2: Train model
    model = train_model(df)

    # Step 3: Save model
    save_model(model)

    # Step 4: Load model again
    loaded_model = load_model()

    # Step 5: Predict with new input
    new_input = pd.DataFrame({
        'hour_of_day': [8],       # 8 AM
        'day_of_week': [1],       # Monday
        'vehicle_count': [160],
        'weather_condition': [1], # Rainy
        'accident': [1],
        'school_zone': [1],
        'office_zone': [1]
    })

    prediction = predict_congestion(loaded_model, new_input)
    print(f"\n🚗 Predicted Congestion Level: {prediction[0]:.2f} 🚗")

    print("\n✅ End of pipeline ✅")
