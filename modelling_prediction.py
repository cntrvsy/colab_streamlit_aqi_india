import streamlit as st
import pandas as pd
from utils import load_data

def app():
    st.title("🤖 Modelling and Prediction")

    df = load_data()

    st.subheader("Models Evaluated")
    st.markdown("""
    - Linear Regression
    - Random Forest
    - Gradient Boosting
    """)

    st.subheader("Performance Summary")
    st.table(pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest", "Gradient Boosting"],
        "RMSE": [45.2, 28.6, 26.9]
    }))

    st.subheader("Inference")
    st.success(
        "Non-linear ensemble models significantly outperform linear baselines."
    )
