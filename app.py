import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained XGBoost model
model = joblib.load("xgb.pkl")

# Define encoders for categorical columns
location_encoder = LabelEncoder()
wind_gust_dir_encoder = LabelEncoder()
wind_dir_9am_encoder = LabelEncoder()
wind_dir_3pm_encoder = LabelEncoder()

# Pre-fit encoders with expected values (use values from the original dataset)
location_encoder.classes_ = ['Location1', 'Location2', 'Location3']  # Replace with actual locations
wind_gust_dir_encoder.classes_ = ['N', 'S', 'E', 'W']  # Add valid wind directions
wind_dir_9am_encoder.classes_ = ['N', 'S', 'E', 'W']
wind_dir_3pm_encoder.classes_ = ['N', 'S', 'E', 'W']

# Title of the app
st.title("Rainfall Prediction App")

# Create input fields for the features
Location = st.selectbox("Location", location_encoder.classes_)
Date_day = st.number_input("Day of the Month", min_value=1, max_value=31, value=1)
Date_month = st.number_input("Month", min_value=1, max_value=12, value=1)
RainToday = st.selectbox("Rain Today", ["Yes", "No"])
WindGustDir = st.selectbox("Wind Gust Direction", wind_gust_dir_encoder.classes_)
WindDir9am = st.selectbox("Wind Direction at 9 AM", wind_dir_9am_encoder.classes_)
WindDir3pm = st.selectbox("Wind Direction at 3 PM", wind_dir_3pm_encoder.classes_)

MinTemp = st.number_input("Min Temperature (°C)", value=12.5)
MaxTemp = st.number_input("Max Temperature (°C)", value=24.3)
Rainfall = st.number_input("Rainfall (mm)", value=1.2)
Evaporation = st.number_input("Evaporation (mm)", value=4.3)
Sunshine = st.number_input("Sunshine (hours)", value=8.0)
WindGustSpeed = st.number_input("Wind Gust Speed (km/h)", value=35)
WindSpeed9am = st.number_input("Wind Speed at 9 AM (km/h)", value=15)
WindSpeed3pm = st.number_input("Wind Speed at 3 PM (km/h)", value=25)
Humidity9am = st.number_input("Humidity at 9 AM (%)", value=80)
Humidity3pm = st.number_input("Humidity at 3 PM (%)", value=50)
Pressure9am = st.number_input("Pressure at 9 AM (hPa)", value=1015.6)
Pressure3pm = st.number_input("Pressure at 3 PM (hPa)", value=1012.3)
Temp9am = st.number_input("Temperature at 9 AM (°C)", value=16.5)
Temp3pm = st.number_input("Temperature at 3 PM (°C)", value=22.0)
Cloud9am = st.number_input("Cloud Cover at 9 AM", value=4)
Cloud3pm = st.number_input("Cloud Cover at 3 PM", value=3)

# Convert categorical inputs to numerical values using the encoders
input_data = pd.DataFrame({
    'Location': [location_encoder.transform([Location])[0]],
    'Date_day': [Date_day],
    'Date_month': [Date_month],
    'RainToday': [1 if RainToday == "Yes" else 0],
    'WindGustDir': [wind_gust_dir_encoder.transform([WindGustDir])[0]],
    'WindDir9am': [wind_dir_9am_encoder.transform([WindDir9am])[0]],
    'WindDir3pm': [wind_dir_3pm_encoder.transform([WindDir3pm])[0]],
    'MinTemp': [MinTemp],
    'MaxTemp': [MaxTemp],
    'Rainfall': [Rainfall],
    'Evaporation': [Evaporation],
    'Sunshine': [Sunshine],
    'WindGustSpeed': [WindGustSpeed],
    'WindSpeed9am': [WindSpeed9am],
    'WindSpeed3pm': [WindSpeed3pm],
    'Humidity9am': [Humidity9am],
    'Humidity3pm': [Humidity3pm],
    'Pressure9am': [Pressure9am],
    'Pressure3pm': [Pressure3pm],
    'Temp9am': [Temp9am],
    'Temp3pm': [Temp3pm],
    'Cloud9am': [Cloud9am],
    'Cloud3pm': [Cloud3pm]
})

# Predict button
if st.button("Predict Rainfall"):
    # Make prediction using the model
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("It will rain tomorrow!")
    else:
        st.info("No rain expected tomorrow.")
