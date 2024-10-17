import streamlit as st
import pandas as pd
import random
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained XGBoost model
with open('xgb.pkl', 'rb') as file:
    xgb_model = pickle.load(file)

# Create a button to generate random input data
if st.button("Generate Random Input"):
    # Assign random values for each feature (within reasonable ranges)
    MinTemp = random.uniform(5.0, 25.0)
    MaxTemp = random.uniform(20.0, 40.0)
    Rainfall = random.uniform(0.0, 50.0)
    Evaporation = random.uniform(0.0, 15.0)
    Sunshine = random.uniform(0.0, 12.0)
    WindGustSpeed = random.uniform(20.0, 90.0)
    WindSpeed9am = random.uniform(0.0, 40.0)
    WindSpeed3pm = random.uniform(0.0, 40.0)
    Humidity9am = random.uniform(20.0, 100.0)
    Humidity3pm = random.uniform(20.0, 100.0)
    Pressure9am = random.uniform(990.0, 1030.0)
    Pressure3pm = random.uniform(990.0, 1030.0)
    Temp9am = random.uniform(10.0, 30.0)
    Temp3pm = random.uniform(20.0, 35.0)
    Location = random.choice(['Sydney', 'Melbourne', 'Brisbane', 'Perth'])
    WindGustDir = random.choice(['N', 'S', 'E', 'W'])
    WindDir9am = random.choice(['N', 'S', 'E', 'W'])
    WindDir3pm = random.choice(['N', 'S', 'E', 'W'])
    Cloud9am = random.randint(0, 8)
    Cloud3pm = random.randint(0, 8)
    Date_month = random.randint(1, 12)
    Date_day = random.randint(1, 31)
    RainToday = random.randint(0, 1)

    # Create a DataFrame using the random values
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

    # Ensure the input data matches the model's expected feature order
    feature_order = [
        'Location', 'MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
        'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm',
        'Temp9am', 'Temp3pm', 'Date_month', 'Date_day', 'RainToday'
    ]
    input_data = input_data[feature_order]

    # Use the model to make predictions
    predictions = xgb_model.predict(input_data)

    # Output the prediction result
    prediction_text = "Yes" if predictions[0] == 1 else "No"
    st.write(f"Prediction (Rain Tomorrow): {prediction_text}")

