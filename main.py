from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model/congestion_predictor.pkl")

class TrafficInput(BaseModel):
    hour: int
    day: str
    location: str
    weather: str
    road_condition: str
    vehicle_type: str
    accident: int
    special_event: int

@app.post("/predict")
def predict_congestion(data: TrafficInput):
    input_df = pd.DataFrame([data.dict()])
    pred = model.predict(input_df)[0]
    return {"congested": bool(pred)}
