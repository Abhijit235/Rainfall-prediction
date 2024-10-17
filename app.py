import streamlit as st
import pandas as pd
import xgboost as xgb
import joblib

# Load the trained model
xgb_model = joblib.load('xgb.pkl')  # Adjust the path if necessary

# Function to convert categorical variables
def preprocess_input(data):
    # Convert categorical variables to numerical values
    location_mapping = {'Melbourne': 0, 'Sydney': 1, 'Brisbane': 2}  # Add more locations if needed
    data['Location'] = data['Location'].map(location_mapping)
    
    wind_gust_dir_mapping = {'N': 0, 'S': 1, 'E': 2, 'W': 3, 'NE': 4, 'NW': 5, 'SE': 6, 'SW': 7}  # Adjust as needed
    data['WindGustDir'] = data['WindGustDir'].map(wind_gust_dir_mapping)
    data['WindDir9am'] = data['WindDir9am'].map(wind_gust_dir_mapping)
    data['WindDir3pm'] = data['WindDir3pm'].map(wind_gust_dir_mapping)

    return data

# Create input fields
st.title("Rain Prediction App")

MinTemp = st.number_input("Min Temperature (°C)", value=10.0)
MaxTemp = st.number_input("Max Temperature (°C)", value=25.0)
Rainfall = st.number_input("Rainfall (mm)", value=5.0)
Evaporation = st.number_input("Evaporation (mm)", value=2.5)
Sunshine = st.number_input("Sunshine (hours)", value=7.0)
WindGustSpeed = st.number_input("Wind Gust Speed (km/h)", value=20.0)
WindSpeed9am = st.number_input("Wind Speed at 9am (km/h)", value=15.0)
WindSpeed3pm = st.number_input("Wind Speed at 3pm (km/h)", value=10.0)
Humidity9am = st.number_input("Humidity at 9am (%)", value=80.0)
Humidity3pm = st.number_input("Humidity at 3pm (%)", value=50.0)
Pressure9am = st.number_input("Pressure at 9am (hPa)", value=1010.0)
Pressure3pm = st.number_input("Pressure at 3pm (hPa)", value=1008.0)
Temp9am = st.number_input("Temperature at 9am (°C)", value=12.0)
Temp3pm = st.number_input("Temperature at 3pm (°C)", value=22.0)
Location = st.selectbox("Location", ['Melbourne', 'Sydney', 'Brisbane'])  # Add more options as necessary
WindGustDir = st.selectbox("Wind Gust Direction", ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW'])  # Adjust as necessary
WindDir9am = st.selectbox("Wind Direction at 9am", ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW'])  # Adjust as necessary
WindDir3pm = st.selectbox("Wind Direction at 3pm", ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW'])  # Adjust as necessary
Cloud9am = st.number_input("Cloud at 9am (octas)", value=3)
Cloud3pm = st.number_input("Cloud at 3pm (octas)", value=1)
Date_month = st.number_input("Date Month", value=10)  # Example for October
Date_day = st.number_input("Date Day", value=17)  # Example for 17th
RainToday = st.number_input("Rain Today (0 for No, 1 for Yes)", value=0)  # Adjust as necessary

# Prepare the input data as a DataFrame in the correct order
input_data = pd.DataFrame({
    'Location': [Location],
    'MinTemp': [MinTemp],
    'MaxTemp': [MaxTemp],
    'Rainfall': [Rainfall],
    'Evaporation': [Evaporation],
    'Sunshine': [Sunshine],
    'WindGustDir': [WindGustDir],
    'WindGustSpeed': [WindGustSpeed],
    'WindDir9am': [WindDir9am],
    'WindDir3pm': [WindDir3pm],
    'WindSpeed9am': [WindSpeed9am],
    'WindSpeed3pm': [WindSpeed3pm],
    'Humidity9am': [Humidity9am],
    'Humidity3pm': [Humidity3pm],
    'Pressure9am': [Pressure9am],
    'Pressure3pm': [Pressure3pm],
    'Cloud9am': [Cloud9am],
    'Cloud3pm': [Cloud3pm],
    'Temp9am': [Temp9am],
    'Temp3pm': [Temp3pm],
    'Date_month': [Date_month],
    'Date_day': [Date_day],
    'RainToday': [RainToday]
})

# Preprocess the input data
input_data = preprocess_input(input_data)

# Use the model to make predictions
predictions = xgb_model.predict(input_data)

# Output the prediction result
st.write(f"Predicted Rainfall: {predictions[0]}")
