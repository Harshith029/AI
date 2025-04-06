import joblib
import pandas as pd

# Load pre-trained model
model = joblib.load('models/traffic_predictor_hyderabad.pkl')

def predict_path(start, destination, vehicle):
    # Feature encoding (example, replace with actual encoding logic)
    features = pd.DataFrame([[start, destination, vehicle]], columns=['start', 'destination', 'vehicle'])
    
    predicted_path = model.predict(features)
    return predicted_path.tolist()
