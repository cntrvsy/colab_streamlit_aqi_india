import streamlit as st
import pandas as pd
import joblib
import os

# Define the directory where model artifacts are saved
MODEL_DIR = 'streamlit_artifacts'

# Load the trained model and encoder (using Streamlit's cache for efficiency)
@st.cache_resource
def load_model_artifacts():
    model_path = os.path.join(MODEL_DIR, 'random_forest_model.pkl')
    encoder_path = os.path.join(MODEL_DIR, 'one_hot_encoder.pkl')
    features_path = os.path.join(MODEL_DIR, 'model_features.pkl')
    
    model = joblib.load(model_path)
    encoder = joblib.load(encoder_path)
    model_features = joblib.load(features_path)
    return model, encoder, model_features

st.title("Modelling and Prediction")

# Load model and encoder
model_extended, encoder, model_features = load_model_artifacts()

st.subheader("Model Evaluation")
st.markdown("Here's a summary of the extended model's performance:")
st.table(pd.DataFrame({
    "Metric": ["Mean Absolute Error (MAE)", "Mean Squared Error (MSE)", "Root Mean Squared Error (RMSE)", "R-squared (R2)"],
    "Value": [f"{19.91:.2f}", f"{1767.63:.2f}", f"{42.04:.2f}", f"{0.89:.2f}"] # Using previously computed values
}))
st.info("The model with extended features (including Month and City) shows a slight improvement in performance compared to the pollutants-only model, explaining 89% of the variance in AQI.")

st.subheader("Predict AQI for Custom Inputs")
st.markdown("Adjust the pollutant levels, month, and city below to get an estimated AQI.")

# Get unique cities from the encoder (assuming the encoder was fitted on the full dataset)
all_cities = sorted(encoder.categories_[0].tolist())

# Input widgets for prediction
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**Pollutant Levels (μg/m³ unless specified)**")
    pm2_5 = st.slider('PM2.5', 0.0, 500.0, 55.0, 0.1)
    pm10 = st.slider('PM10', 0.0, 1000.0, 100.0, 0.1)
    no = st.slider('NO', 0.0, 400.0, 15.0, 0.1)
    no2 = st.slider('NO2', 0.0, 400.0, 30.0, 0.1)
    nox = st.slider('NOx', 0.0, 500.0, 40.0, 0.1)
with col2:
    st.write("") # Spacer
    nh3 = st.slider('NH3', 0.0, 400.0, 20.0, 0.1)
    co = st.slider('CO (mg/m³)', 0.0, 200.0, 1.5, 0.1)
    so2 = st.slider('SO2', 0.0, 200.0, 10.0, 0.1)
    o3 = st.slider('O3', 0.0, 300.0, 35.0, 0.1)
    benzene = st.slider('Benzene', 0.0, 500.0, 2.0, 0.1)
    toluene = st.slider('Toluene', 0.0, 500.0, 5.0, 0.1)
with col3:
    st.write("") # Spacer
    xylene = st.slider('Xylene', 0.0, 200.0, 1.0, 0.1)
    
    st.write("**Temporal & Location**")
    month = st.selectbox('Month', range(1, 13), index=0) # Jan = 1, Dec = 12
    city = st.selectbox('City', all_cities, index=all_cities.index('Ahmedabad') if 'Ahmedabad' in all_cities else 0)

if st.button('Predict AQI'):
    # Create a DataFrame for the new data point, ensuring all columns match model_features
    new_data_point = pd.DataFrame(0.0, index=[0], columns=model_features)

    # Populate pollutant values
    new_data_point['PM2_5'] = pm2_5
    new_data_point['PM10'] = pm10
    new_data_point['NO'] = no
    new_data_point['NO2'] = no2
    new_data_point['NOx'] = nox
    new_data_point['NH3'] = nh3
    new_data_point['CO'] = co
    new_data_point['SO2'] = so2
    new_data_point['O3'] = o3
    new_data_point['Benzene'] = benzene
    new_data_point['Toluene'] = toluene
    new_data_point['Xylene'] = xylene
    
    # Populate month
    new_data_point['Month'] = month

    # Populate one-hot encoded city
    city_col_name = f'City_{city}'
    if city_col_name in new_data_point.columns:
        new_data_point[city_col_name] = 1.0
    else:
        st.error(f"Selected city '{city}' was not found in the model's training data features. Please select another city.")
    
    # Make prediction
    try:
        predicted_aqi = model_extended.predict(new_data_point)[0]
        st.success(f"Predicted AQI for the given conditions: **{predicted_aqi:.2f}**")
        
        # Convert AQI to bucket for better interpretation
        def aqi_to_bucket(aqi_val):
            if aqi_val <= 50: return "Good"
            elif aqi_val <= 100: return "Satisfactory"
            elif aqi_val <= 200: return "Moderate"
            elif aqi_val <= 300: return "Poor"
            elif aqi_val <= 400: return "Very Poor"
            else: return "Severe"
        
        aqi_category = aqi_to_bucket(predicted_aqi)
        st.info(f"This corresponds to an AQI category of: **{aqi_category}**")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
