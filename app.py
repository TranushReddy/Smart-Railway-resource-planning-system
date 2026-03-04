import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

# Page config
st.set_page_config(page_title="Smart Railway Resource Planner", layout="wide")

st.title("🚆 Smart Railway Resource Planning System")


# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv(
        "railway_dataset.csv"
    )
    return df


df = load_data()

# Sidebar
st.sidebar.header("Filters")

route_filter = st.sidebar.multiselect(
    "Select Route", df["Route"].unique(), default=df["Route"].unique()
)

df = df[df["Route"].isin(route_filter)]

# ---------------------------
# Passenger Demand Visualization
# ---------------------------

st.header("Passenger Demand Analysis")

col1, col2 = st.columns(2)

with col1:
    route_demand = df.groupby("Route")["Passenger_Count"].sum().reset_index()

    fig = px.bar(
        route_demand, x="Route", y="Passenger_Count", title="Passenger Demand by Route"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    time_demand = df.groupby("Departure_Time")["Passenger_Count"].sum().reset_index()

    fig2 = px.line(
        time_demand,
        x="Departure_Time",
        y="Passenger_Count",
        title="Passenger Demand by Time",
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# High Demand Route Detection
# ---------------------------

st.header("High Demand Routes")

high_demand = df[df["Seat_Occupancy_Percent"] > 90]

st.write("Routes experiencing high passenger demand")

st.dataframe(
    high_demand[["Train_Name", "Route", "Passenger_Count", "Seat_Occupancy_Percent"]]
)

# ---------------------------
# Prediction Section
# ---------------------------

st.header("Predict Passenger Demand")

try:
    model = joblib.load(
        "railway_demand_model.pkl"
    )
except:
    model = None

if model is not None:

    col1, col2, col3 = st.columns(3)

    with col1:
        coaches = st.slider("Number of Coaches", 8, 20, 12)

    with col2:
        platform = st.slider("Platform Number", 1, 10, 3)

    with col3:
        weekend = st.selectbox("Weekend", [0, 1])

    holiday = st.selectbox("Holiday", [0, 1])
    month = st.slider("Month", 1, 12, 6)
    hour = st.slider("Departure Hour", 0, 23, 10)

    features = np.array([[coaches, platform, weekend, holiday, month, hour]])

    if st.button("Predict Passenger Count"):

        prediction = model.predict(features)[0]

        st.success(f"Predicted Passenger Count: {int(prediction)}")

        # Resource Recommendation
        capacity = coaches * 72
        occupancy = (prediction / capacity) * 100

        st.subheader("Resource Recommendation")

        if occupancy > 95:
            st.error("⚠️ Overcrowding expected → Add 2 Coaches")
        elif occupancy > 85:
            st.warning("High demand → Add 1 Coach")
        else:
            st.success("Current resources sufficient")

else:
    st.warning("Model file not found. Train the ML model first.")

# ---------------------------
# Platform Usage Analysis
# ---------------------------

st.header("Platform Utilization")

platform_usage = df.groupby("Platform_Number")["Passenger_Count"].sum().reset_index()

fig3 = px.bar(
    platform_usage,
    x="Platform_Number",
    y="Passenger_Count",
    title="Platform Usage by Passenger Volume",
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------
# Dataset Preview
# ---------------------------

st.header("Dataset Preview")

st.dataframe(df.head(20))

