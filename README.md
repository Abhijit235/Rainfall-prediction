# Rainfall-prediction
Rainfall Prediction Using XGBoost 🌧️
Welcome to the Rainfall Prediction App! This project uses machine learning with XGBoost to predict whether it will rain tomorrow, based on historical weather data collected from various Australian locations. The goal of this project is to provide accurate rainfall forecasts using meteorological data.

Explore the live demo of this app deployed using Streamlit through the link below:

🔗 [Live Demo](https://rainfall-prediction-6vjxfrhyyqe4lph8ufvt5m.streamlit.app/)

Project Overview:

Accurate rainfall prediction is crucial for sectors like agriculture, water management, and disaster preparedness. In this project, I developed a predictive model using the XGBoost algorithm trained on weather data from the National Center for Atmospheric Research (NCAR).

The features include key meteorological variables such as temperature, humidity, wind speed, cloud cover, and more, making the prediction both reliable and insightful.

Features of the App
User-Friendly Interface:

Built with Streamlit for a seamless user experience.
Enter weather conditions, and the app instantly predicts if it will rain tomorrow.
XGBoost Model:

Trained with carefully preprocessed weather data.
Provides high accuracy in rainfall prediction.
Responsive Design:

The app works on both desktop and mobile devices.
Technologies Used
Python
XGBoost for machine learning
Streamlit for app deployment
Pandas for data preprocessing
GitHub for version control and project management
How to Run the App Locally
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/rainfall-prediction
cd rainfall-prediction
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
streamlit run app.py
Open the browser at [https://rainfall-prediction-6vjxfrhyyqe4lph8ufvt5m.streamlit.app/] to access the app.

Model Details:

Dataset: The data comes from NCAR's publicly available Australian weather data.
Target Variable: RainTomorrow – A binary classification to determine if it will rain tomorrow (Yes or No).

Key Features:
Temperature: MinTemp, MaxTemp, Temp9am, Temp3pm
Humidity: Humidity9am, Humidity3pm
Wind: WindGustDir, WindGustSpeed, WindDir9am, WindDir3pm
Cloud Cover: Cloud9am, Cloud3pm
Rainfall, Evaporation, and Sunshine hours


Project Structure


rainfall-prediction/
│
├── app.py               # Streamlit app code
├── xgb.pkl              # Trained XGBoost model
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
Live Demo
🚀 Check out the live app here: Rainfall Prediction App(https://rainfall-prediction-6vjxfrhyyqe4lph8ufvt5m.streamlit.app/)

How This Project Helps Me Get Placed 💼
This project demonstrates my ability to work on end-to-end machine learning projects, including:

Data Preprocessing: Handling missing values, encoding categorical data, and feature engineering.
Model Development: Building and tuning predictive models with XGBoost.
Web Deployment: Creating interactive and responsive apps with Streamlit.
Collaboration on GitHub: Managing code and documentation effectively.
I believe this project highlights my technical expertise and problem-solving skills, and I hope it showcases my potential to future employers.

