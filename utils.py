import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """Load air quality data from GitHub repository"""
    try:
        # Use raw.githubusercontent.com for direct CSV access
        url = 'https://raw.githubusercontent.com/cntrvsy/colab/main/processed_data.csv'
        df = pd.read_csv(url)

        # Convert Date column to datetime if it exists
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        return df

    except Exception as e:
        st.error(f"Error loading data: {e}")
        st.info("Make sure processed_data.csv exists in your GitHub repository and is publicly accessible.")
        # Return empty DataFrame to prevent crashes
        return pd.DataFrame()
