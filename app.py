import streamlit as st
import pandas as pd
import joblib

# Load the trained XGBoost model
model = joblib.load("xgb.pkl")

# Title of the app
st.title("Rainfall Prediction App")

# Create input fields for user to enter feature values
MinTemp = st.number_input("Min Temperature (°C)", min_value=-10.0, max_value=50.0, value=12.5)
MaxTemp = st.number_input("Max Temperature (°C)", min_value=-10.0, max_value=50.0, value=24.3)
Rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=1.2)
Evaporation = st.number_input("Evaporation (mm)", min_value=0.0, max_value=50.0, value=4.3)
Sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=15.0, value=8.0)
WindGustSpeed = st.number_input("Wind Gust Speed (km/h)", min_value=0, max_value=200, value=35)
WindSpeed9am = st.number_input("Wind Speed at 9 AM (km/h)", min_value=0, max_value=200, value=15)
WindSpeed3pm = st.number_input("Wind Speed at 3 PM (km/h)", min_value=0, max_value=200, value=25)
Humidity9am = st.number_input("Humidity at 9 AM (%)", min_value=0, max_value=100, value=80)
Humidity3pm = st.number_input("Humidity at 3 PM (%)", min_value=0, max_value=100, value=50)
Pressure9am = st.number_input("Pressure at 9 AM (hPa)", min_value=900.0, max_value=1100.0, value=1015.6)
Pressure3pm = st.number_input("Pressure at 3 PM (hPa)", min_value=900.0, max_value=1100.0, value=1012.3)
Temp9am = st.number_input("Temperature at 9 AM (°C)", min_value=-10.0, max_value=50.0, value=16.5)
Temp3pm = st.number_input("Temperature at 3 PM (°C)", min_value=-10.0, max_value=50.0, value=22.0)

# Prepare input data as a DataFrame
input_data = pd.DataFrame({
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
    'Temp3pm': [Temp3pm]
})

# Predict button
if st.button("Predict Rainfall"):
    # Make prediction using the loaded model
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("It will rain tomorrow!")
    else:
        st.info("No rain expected tomorrow.")
