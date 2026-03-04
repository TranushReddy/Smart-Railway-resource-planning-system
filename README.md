# 🚆 Smart Railway Resource Planning System

## Overview

This project is a data‑driven application designed to help railway planners optimize resource allocation using historical and operational data.

The system analyzes passenger demand patterns and provides recommendations to improve railway planning efficiency. It helps reduce overcrowding, improve passenger experience, and maximize resource utilization during peak travel periods.

## Key Features

### 1. Passenger Demand Visualization

- Visualize passenger demand across routes
- Identify peak travel hours
- Analyze passenger distribution across platforms

### 2. Demand Prediction

- Predict passenger demand using a Machine Learning model
- Identify high-demand travel windows
- Forecast potential overcrowding scenarios

### 3. Resource Allocation Recommendations

- Recommend additional coaches when demand is high
- Identify routes that may require extra trains
- Detect possible platform congestion

### 4. Interactive Dashboard

- Built using Streamlit
- Real-time visualization and predictions
- Easy-to-use interface for planners

## Technology Stack

| Component            | Technology         |
| -------------------- | ------------------ |
| Programming Language | Python             |
| Data Analysis        | Pandas, NumPy      |
| Machine Learning     | Scikit-learn       |
| Visualization        | Plotly, Matplotlib |
| Dashboard            | Streamlit          |
| Model Saving         | Joblib             |
| Version Control      | Git & GitHub       |

## Project Structure

```
smart-railway-planner
│
├── railway_dataset.csv
│
|── railway_ml_pipeline.ipynb
│
│─ railway_demand_model.pkl
│
├── app
|   |----- app.py
├── requirements.txt
├── README.md
```

## Dataset

Synthetic railway operational dataset containing:

- Train ID
- Route (Source–Destination)
- Date
- Departure Time
- Passenger Count
- Number of Coaches
- Seat Capacity
- Platform Number
- Delay Records
- Holiday/Weekend Indicator
- Demand Level

## Installation

Clone the repository

git clone https://github.com/TranushReddy/Smart-Railway-resource-planning-system.git

Navigate to the folder

cd smart-railway-resource-planner

Install dependencies

pip install -r requirements.txt

## Running the Application

Run the Streamlit dashboard

streamlit run app.py

Open in browser:

http://localhost:8501

## Machine Learning Workflow

1. Import libraries
2. Load dataset
3. Data preprocessing
4. Exploratory data analysis (EDA)
5. Feature engineering
6. Train-test split
7. Model training (Random Forest)
8. Prediction
9. Model evaluation
10. Model saving

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Future Improvements

- Add real railway datasets
- Implement time-series forecasting
- Integrate real-time passenger booking data
- Advanced platform scheduling optimization

## Author

Smart Railway Resource Planning Hackathon Project
