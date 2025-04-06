import joblib

# Load the model
model = joblib.load("model/congestion_predictor.pkl")

# Example input
test_input = {
    "hour": 18,
    "vehicle_type_car": 1,
    "vehicle_type_bike": 0,
    "vehicle_type_truck": 0,
    "vehicle_type_ambulance": 0,
    "weather_clear": 1,
    "weather_rainy": 0,
    "road_condition_good": 0,
    "road_condition_bad": 1,
    "accident_on_route": 1,
    "event_nearby": 1
}

# Ensure order of features
ordered_features = [
    "hour",
    "accident_on_route",
    "event_nearby",
    "vehicle_type_ambulance",
    "vehicle_type_bike",
    "vehicle_type_car",
    "vehicle_type_truck",
    "weather_clear",
    "weather_rainy",
    "road_condition_bad",
    "road_condition_good"
]

# Reorder input
features = [test_input.get(f, 0) for f in ordered_features]

# Predict
prediction = model.predict([features])[0]
print(f"Predicted congestion score: {prediction:.2f}")
