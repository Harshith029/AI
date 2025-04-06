# 🍬 Hyderabad AI Traffic Optimization System 🚦

## 🔥 SUGAR Hackathon Theme Integration
Just like **ants** scout and adaptively choose the best and most comfortable paths to reach **sugar**, our users (the ants) are guided to their destination (sugar) in a way that avoids overcrowding a single route. This **nature-inspired strategy** ensures smoother traffic flow, minimal delays, and a better experience overall.

This analogy ties into the **SUGAR hackathon theme** by treating the destination as the sugar and mimicking how nature finds **optimal solutions** to movement and resource collection problems.

---

## 📁 Project Structure Overview
```bash
hyderabad-ai-traffic/
├── backend/
│   ├── app.js                 # Express.js backend server
│   ├── routes/
│   │   └── trafficRoutes.js   # Routing logic & APIs
│   └── controllers/
│       └── routeController.js # Path calculation & AI integration
├── frontend/
│   ├── public/                # Static UI or future React client
│   └── index.js               # CLI / web interface for user input
├── ai_model/
│   ├── main.py                # LSTM-based traffic prediction model
│   ├── preprocess.py          # Cleans and encodes traffic data
│   ├── cluster_users.py       # Clusters users to spread load
│   └── model_weights/         # Trained weights for demo purposes
├── emergency/
│   └── green_corridor.py      # Emergency route prioritization logic
├── map_renderer/
│   └── mapplot.py             # Visualization or ASCII mapping
├── data/
│   ├── roads.json             # Simulated road network structure
│   ├── synthetic_traffic.csv  # Artificial congestion data
│   └── events_calendar.csv    # Public event data (festivals, etc.)
├── auth/
│   └── user_auth.py           # Simple authentication (demo-level)
├── utils/
│   └── helpers.py             # Distance calculations and utilities
├── package.json               # Node.js dependencies
├── requirements.txt           # Python dependencies
└── README.md                  # You are here!
```

---

## 🧠 AI Model Overview
### Model: **LSTM Neural Network**
- Predicts upcoming congestion using temporal patterns
- Inputs: time, area, weather/event proximity, road width, vehicle type, peak windows
- Shape: `(24, 15)` input sequences

### Clustering with `cluster_users()`
- Users are clustered based on **origin, sugar, and travel time**
- Reduces conflict between groups on common paths
- Ensures distributed flow with **multi-path redirection**
- Foundation for avoiding early-stage congestion proactively

---

## 👣 Example User Flow
1. **Input via UI / CLI**
   ```bash
   Enter Start Location: HITEC City
   Enter Sugar: LB Nagar
   Vehicle Type: car
   ```

2. **Backend Process**
   - Fetch congestion history, events, time-based traffic maps
   - Cluster users into route buckets
   - Use AI to predict optimal flow and assign path

3. **AI Output (3 Route Options)**
   - Route 1 (fastest but nearing congestion)
   - Route 2 (slightly longer but stable flow)
   - Route 3 (safest path with least footfall)

4. **Final Display**
   ```
   ▶ Route Assigned: Route 3 (Optimized Group Route)
   ETA: 17 mins | Distance: 8.4 km | Congestion Score: 12%
   ```

---

## 🚨 Emergency Mode Handling
- Ambulance/fire brigade users are auto-flagged
- Routes are assigned dynamically with emergency clearance
- `green_corridor.py` handles:
  - Path prioritization
  - Traffic light override (mock)
  - Real-time updates (future API integration)

```python
if vehicle_type == 'ambulance':
    activate_green_corridor(start, destination)
```

---

## 🚏 Output Sample - Hyderabad Use Case
```
Start: Kukatpally
Destination: Mehdipatnam

🚗 Route 1:
▶ Kukatpally → Erragadda → Mehdipatnam (12.1 km | 28 mins)
Congestion: 37%

🚗 Route 2:
▶ Kukatpally → Ring Road → Langar Houz (13.2 km | 25 mins)
Congestion: 24%

🚗 Route 3:
▶ Kukatpally → Yousufguda → Masab Tank (11.8 km | 22 mins)
Congestion: 18%
```

### 📊 Number of Routes Generated
- Default: **3 routes per user**
- Future: Adaptive route count based on cluster density and prediction confidence

---

## 🚧 Current Limitations
- ❌ Real-time updates not yet active
- ❌ Model trained on **synthetic traffic data**, not real city feed
- ❌ APIs not integrated with GHMC / Google / HERE Maps
- ❌ Frontend not fully linked to backend-AI pipeline

⚠️ **Currently, traffic division is auto-handled by AI models** — not manual — but they're demo-level and untrained on real Hyderabad behavior.

---

## 🌍 Expansion & Future Development
- 🛰️ Add real-time APIs (Govt + crowd-sourced)
- 🔄 Real-time retraining of LSTM model
- 🗺️ Heatmap generation for visual analytics
- 📈 Predictive rerouting & auto-cluster rebalance
- 🇮🇳 Expand model coverage from Hyderabad to PAN-India
- 🤖 Train on **live public datasets**, GPS data & mobile streams
- 🧠 Improve AI explainability, reroute confidence metrics
- 🔧 Improve backend-AI-frontend communication and workflows

---

## 📚 Resources Used (Trusted Sources)
- [TensorFlow LSTM](https://www.tensorflow.org/guide/keras/rnn)
- [OpenStreetMap - Hyderabad](https://www.openstreetmap.org/#map=12/17.3850/78.4867)
- [Hyderabad Live Events Calendar](https://www.hyderabadtourism.in/events-in-hyderabad.php)
- [FHWA Traffic Theory](https://ops.fhwa.dot.gov/trafficanalysistools/tft/index.htm)

---

## 🧪 Getting Started (Local Demo)
```bash
# Step 1: Install all dependencies
npm install                      # Node backend
pip install -r requirements.txt # Python AI stack

# Step 2: Launch Servers
node backend/app.js
python ai_model/main.py
node frontend/index.js
```

---

> 🚧 **Note**: This project is an early-stage **prototype** designed for demonstration purposes only. While all individual modules (prediction model, clustering, emergency rerouting, etc.) are functional, they remain siloed. Full integration and production-level deployment require:
> - Large-scale real-world datasets (Hyderabad origin → PAN India)
> - Continuous training pipelines with active data streams
> - Live map APIs and frontend-AI sync workflows
> - User-friendly dashboards, reliability checks, and more testing

---

🎯 **SUGAR Project Philosophy**
> Just like ants locate and follow efficient paths to sugar while dynamically avoiding congestion, this system intelligently leads users to their destinations using adaptive routing and crowd-aware traffic planning. Nature inspires technology to solve complex flow problems — from traffic to data to logistics.

🚦 "**Ants to Sugar, People to Places. Smarter, Smoother, Together.**" 🍬

# Team Name: GPTwizards

# LICENSE

MIT License

Copyright (c) 2025 AITOS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
