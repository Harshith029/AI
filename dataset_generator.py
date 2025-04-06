import pandas as pd
import random

locations = ["Office-Area", "School-Zone", "Residential", "Market", "Highway"]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
weather = ["Clear", "Rainy", "Foggy"]
road_cond = ["Good", "Bad"]
vehicle_type = ["Car", "Bike", "Bus", "Truck"]

data = []

for _ in range(10000):
    row = {
        "hour": random.randint(0, 23),
        "day": random.choice(days),
        "location": random.choice(locations),
        "weather": random.choice(weather),
        "road_condition": random.choice(road_cond),
        "vehicle_type": random.choice(vehicle_type),
        "accident": random.choice([0, 1]),
        "special_event": random.choice([0, 1]),
        "congestion": random.choice([0, 1])  # 1 = congestion, 0 = clear
    }
    data.append(row)

df = pd.DataFrame(data)
df.to_csv("model/synthetic_traffic_data.csv", index=False)
print("Dataset generated ✅")
