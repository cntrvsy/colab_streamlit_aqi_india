import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    """Load air quality data from local file or GitHub repository"""
    # Try local path first
    local_path = 'data/processed/processed_data.csv'
    try:
        if os.path.exists(local_path):
            df = pd.read_csv(local_path)
            if 'Date' in df.columns:
                df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
            return df
    except Exception as e:
        st.warning(f"Could not load local data: {e}")

    # Fallback to GitHub
    try:
        # Use raw.githubusercontent.com for direct CSV access
        url = 'https://raw.githubusercontent.com/cntrvsy/colab/main/data/processed/processed_data.csv'
        df = pd.read_csv(url)

        # Convert Date column to datetime if it exists
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        return df

    except Exception as e:
        st.error(f"Error loading data from GitHub: {e}")
        st.info("Make sure processed_data.csv exists in your local 'data/processed/' directory or GitHub repository.")
        # Return empty DataFrame to prevent crashes
        return pd.DataFrame()
