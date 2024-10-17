import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained XGBoost model
with open('xgb.pkl', 'rb') as file:
    xgb_model = pickle.load(file)

# Streamlit app title
st.title("Rain Prediction App")

# Create input fields for each feature
Location = st.selectbox("Location", ['Sydney', 'Melbourne', 'Brisbane', 'Perth'])
MinTemp = st.number_input("Minimum Temperature (°C)", min_value=5.0, max_value=25.0, value=15.0)
MaxTemp = st.number_input("Maximum Temperature (°C)", min_value=20.0, max_value=40.0, value=30.0)
Rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=50.0, value=10.0)
Evaporation = st.number_input("Evaporation (mm)", min_value=0.0, max_value=15.0, value=5.0)
Sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=12.0, value=6.0)
WindGustSpeed = st.number_input("Wind Gust Speed (km/h)", min_value=20.0, max_value=90.0, value=40.0)
WindSpeed9am = st.number_input("Wind Speed at 9 AM (km/h)", min_value=0.0, max_value=40.0, value=10.0)
WindSpeed3pm = st.number_input("Wind Speed at 3 PM (km/h)", min_value=0.0, max_value=40.0, value=10.0)
Humidity9am = st.number_input("Humidity at 9 AM (%)", min_value=20.0, max_value=100.0, value=60.0)
Humidity3pm = st.number_input("Humidity at 3 PM (%)", min_value=20.0, max_value=100.0, value=60.0)
Pressure9am = st.number_input("Pressure at 9 AM (hPa)", min_value=990.0, max_value=1030.0, value=1010.0)
Pressure3pm = st.number_input("Pressure at 3 PM (hPa)", min_value=990.0, max_value=1030.0, value=1010.0)
Temp9am = st.number_input("Temperature at 9 AM (°C)", min_value=10.0, max_value=30.0, value=20.0)
Temp3pm = st.number_input("Temperature at 3 PM (°C)", min_value=20.0, max_value=35.0, value=25.0)
WindGustDir = st.selectbox("Wind Gust Direction", ['N', 'S', 'E', 'W'])
WindDir9am = st.selectbox("Wind Direction at 9 AM", ['N', 'S', 'E', 'W'])
WindDir3pm = st.selectbox("Wind Direction at 3 PM", ['N', 'S', 'E', 'W'])
Cloud9am = st.number_input("Cloud Cover at 9 AM (0-8)", min_value=0, max_value=8, value=4)
Cloud3pm = st.number_input("Cloud Cover at 3 PM (0-8)", min_value=0, max_value=8, value=4)
Date_month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=1)
Date_day = st.number_input("Day (1-31)", min_value=1, max_value=31, value=1)
RainToday = st.selectbox("Rain Today", [0, 1])  # 0 for No, 1 for Yes

# Create a DataFrame using the user inputs
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
    # Assuming the label encoders have been fitted on the training data
    # You may want to fit and save these encoders during the model training
    if col in label_encoders:
        input_data[col] = label_encoders[col].transform(input_data[col])
    else:
        label_encoders[col] = LabelEncoder()
        input_data[col] = label_encoders[col].fit_transform(input_data[col])

# Ensure the input data matches the model's expected feature order
feature_order = [
    'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
    'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
    'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
    'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
    'Temp9am', 'Temp3pm', 'Date_month', 'Date_day', 'RainToday'
]
input_data = input_data[feature_order]

# Button to make the prediction
if st.button("Predict"):
    # Use the model to make predictions
    predictions = xgb_model.predict(input_data)

    # Output the prediction result
    prediction_text = "Yes" if predictions[0] == 1 else "No"
    st.write(f"Prediction (Rain Tomorrow): {prediction_text}")
