import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained XGBoost model
with open('xgb.pkl', 'rb') as file:
    xgb_model = pickle.load(file)

# User inputs
st.title('Rain Prediction App')

# Asking for user inputs for each feature
Location = st.selectbox('Location', ['Sydney', 'Melbourne', 'Brisbane', 'Perth'])
MinTemp = st.slider('Min Temperature (°C)', 5.0, 25.0, 15.0)
MaxTemp = st.slider('Max Temperature (°C)', 20.0, 40.0, 30.0)
Rainfall = st.slider('Rainfall (mm)', 0.0, 50.0, 10.0)
Evaporation = st.slider('Evaporation (mm)', 0.0, 15.0, 5.0)
Sunshine = st.slider('Sunshine (hours)', 0.0, 12.0, 6.0)
WindGustDir = st.selectbox('Wind Gust Direction', ['N', 'S', 'E', 'W'])
WindGustSpeed = st.slider('Wind Gust Speed (km/h)', 20.0, 90.0, 50.0)
WindDir9am = st.selectbox('Wind Direction at 9 AM', ['N', 'S', 'E', 'W'])
WindDir3pm = st.selectbox('Wind Direction at 3 PM', ['N', 'S', 'E', 'W'])
WindSpeed9am = st.slider('Wind Speed at 9 AM (km/h)', 0.0, 40.0, 10.0)
WindSpeed3pm = st.slider('Wind Speed at 3 PM (km/h)', 0.0, 40.0, 15.0)
Humidity9am = st.slider('Humidity at 9 AM (%)', 20.0, 100.0, 60.0)
Humidity3pm = st.slider('Humidity at 3 PM (%)', 20.0, 100.0, 50.0)
Pressure9am = st.slider('Pressure at 9 AM (hPa)', 990.0, 1030.0, 1010.0)
Pressure3pm = st.slider('Pressure at 3 PM (hPa)', 990.0, 1030.0, 1010.0)
Temp9am = st.slider('Temperature at 9 AM (°C)', 10.0, 30.0, 20.0)
Temp3pm = st.slider('Temperature at 3 PM (°C)', 20.0, 35.0, 25.0)
Cloud9am = st.slider('Cloud Cover at 9 AM (oktas)', 0, 8, 4)
Cloud3pm = st.slider('Cloud Cover at 3 PM (oktas)', 0, 8, 4)
RainToday = st.selectbox('Rain Today?', ['No', 'Yes'])
Date_month = st.slider('Month', 1, 12, 6)
Date_day = st.slider('Day', 1, 31, 15)

# Convert RainToday to 0/1
RainToday = 1 if RainToday == 'Yes' else 0

# Create a DataFrame using the input values
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
    'RainToday': [RainToday],
    'Date_month': [Date_month],
    'Date_day': [Date_day]
})

# Encode categorical variables using LabelEncoder
label_encoders = {}
categorical_columns = ['Location', 'WindGustDir', 'WindDir9am', 'WindDir3pm']

for col in categorical_columns:
    label_encoders[col] = LabelEncoder()
    input_data[col] = label_encoders[col].fit_transform(input_data[col])

# Predict using the XGBoost model
if st.button('Predict'):
    prediction = xgb_model.predict(input_data)
    result = "Yes" if prediction[0] == 1 else "No"
    st.write(f"Prediction (Rain Tomorrow): {result}")
