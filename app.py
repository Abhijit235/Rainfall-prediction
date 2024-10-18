import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("xgb.pkl", "rb") as f:
    model = pickle.load(f)

# Function to make predictions
def predict_rainfall(data):
    prediction = model.predict(data)[0]
    return "Yes" if prediction == 1 else "No"

# Streamlit app interface
st.title("Rainfall Prediction App 🌧️")
st.write("Provide the required input data to predict if it will rain tomorrow.")

# Collect inputs
Date = st.text_input("Date (YYYY-MM-DD)")
Location = st.text_input("Location")
MinTemp = st.number_input("Min Temperature", step=0.1)
MaxTemp = st.number_input("Max Temperature", step=0.1)
Rainfall = st.number_input("Rainfall (mm)", step=0.1)
Evaporation = st.number_input("Evaporation", step=0.1)
Sunshine = st.number_input("Sunshine (hours)", step=0.1)
WindGustDir = st.text_input("Wind Gust Direction")
WindGustSpeed = st.number_input("Wind Gust Speed (km/h)", step=0.1)
WindDir9am = st.text_input("Wind Direction at 9 AM")
WindDir3pm = st.text_input("Wind Direction at 3 PM")
WindSpeed9am = st.number_input("Wind Speed at 9 AM (km/h)", step=0.1)
WindSpeed3pm = st.number_input("Wind Speed at 3 PM (km/h)", step=0.1)
Humidity9am = st.number_input("Humidity at 9 AM (%)", step=0.1)
Humidity3pm = st.number_input("Humidity at 3 PM (%)", step=0.1)
Pressure9am = st.number_input("Pressure at 9 AM (hPa)", step=0.1)
Pressure3pm = st.number_input("Pressure at 3 PM (hPa)", step=0.1)
Cloud9am = st.number_input("Cloud cover at 9 AM (oktas)", step=0.1)
Cloud3pm = st.number_input("Cloud cover at 3 PM (oktas)", step=0.1)
Temp9am = st.number_input("Temperature at 9 AM (°C)", step=0.1)
Temp3pm = st.number_input("Temperature at 3 PM (°C)", step=0.1)
RainToday = st.selectbox("Did it rain today?", ["Yes", "No"])

# Prepare input data
data = pd.DataFrame([[
    Date, Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, 
    WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, 
    WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, 
    Cloud9am, Cloud3pm, Temp9am, Temp3pm, 1 if RainToday == "Yes" else 0
]], columns=[
    "Date", "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation", 
    "Sunshine", "WindGustDir", "WindGustSpeed", "WindDir9am", "WindDir3pm", 
    "WindSpeed9am", "WindSpeed3pm", "Humidity9am", "Humidity3pm", 
    "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am", 
    "Temp3pm", "RainToday"
])

# Button to trigger prediction
if st.button("Predict"):
    result = predict_rainfall(data)
    st.subheader(f"Prediction: Will it rain tomorrow? {result}")

