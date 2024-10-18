import streamlit as st
import pickle
import pandas as pd

# Load the trained XGBoost model from the pickle file
with open("xgb.pkl", "rb") as f:
    model = pickle.load(f)

# Function to encode and preprocess the input data
def preprocess_input(data):
    # Convert categorical variables to numeric codes
    data["RainToday"] = data["RainToday"].map({"Yes": 1, "No": 0})
    
    data["Location"] = pd.Categorical(data["Location"]).codes
    data["WindGustDir"] = pd.Categorical(data["WindGustDir"]).codes
    data["WindDir9am"] = pd.Categorical(data["WindDir9am"]).codes
    data["WindDir3pm"] = pd.Categorical(data["WindDir3pm"]).codes

    # Drop the Date column (if not required by the model)
    data = data.drop("Date", axis=1)

    return data

# Streamlit app interface
st.title("Rainfall Prediction App 🌧️")
st.write("Provide the required input data to predict if it will rain tomorrow.")

# Input fields for the user to enter data
Date = st.text_input("Date (YYYY-MM-DD)")
Location = st.text_input("Location")
MinTemp = st.number_input("Min Temperature", step=0.1)
MaxTemp = st.number_input("Max Temperature", step=0.1)
Rainfall = st.number_input("Rainfall (mm)", step=0.1)
Evaporation = st.number_input("Evaporation (mm)", step=0.1)
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

# Prepare the input data as a DataFrame
data = pd.DataFrame([[
    Date, Location, MinTemp, MaxTemp, Rainfall, Evaporation, Sunshine, 
    WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm, WindSpeed9am, 
    WindSpeed3pm, Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, 
    Cloud9am, Cloud3pm, Temp9am, Temp3pm, RainToday
]], columns=[
    "Date", "Location", "MinTemp", "MaxTemp", "Rainfall", "Evaporation", 
    "Sunshine", "WindGustDir", "WindGustSpeed", "WindDir9am", "WindDir3pm", 
    "WindSpeed9am", "WindSpeed3pm", "Humidity9am", "Humidity3pm", 
    "Pressure9am", "Pressure3pm", "Cloud9am", "Cloud3pm", "Temp9am", 
    "Temp3pm", "RainToday"
])

# Preprocess the input data
data = preprocess_input(data)

# Make predictions when the "Predict" button is clicked
if st.button("Predict"):
    prediction = model.predict(data)[0]
    result = "Yes" if prediction == 1 else "No"
    st.subheader(f"Prediction: Will it rain tomorrow? {result}")
