import streamlit as st

st.set_page_config(
    page_title="Air Quality Dashboard - India",
    page_icon="🇮🇳",
    layout="wide"
)

st.title("🇮🇳 Air Quality Analysis & Prediction - India")

st.markdown("""
Welcome to the Air Quality Dashboard! Use the sidebar on the left to navigate through different sections of the analysis.

### Dashboard Sections:
1. **📊 Data Overview**: High-level summary of the dataset.
2. **📈 Exploratory Data Analysis**: Visual insights into AQI trends and correlations.
3. **🤖 Modelling & Prediction**: Predict AQI based on custom pollutant levels.
4. **💡 Conclusions**: Summary of findings and recommendations.

---

### About the Project
This application analyzes air quality data from various Indian cities to understand pollution patterns and build a predictive model for Air Quality Index (AQI).
""")

st.info("👈 Select a page from the sidebar to get started!")
