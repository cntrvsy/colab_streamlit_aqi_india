import streamlit as st
import plotly.express as px
from src.utils import load_data

st.title("Exploratory Data Analysis")

df = load_data()

tab1, tab2 = st.tabs(["AQI Trends", "Correlations"])

with tab1:
    fig = px.line(
        df,
        x="Date",
        y="AQI",
        color="City",
        title="AQI Trends Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Correlation Matrix")
    st.dataframe(df.corr(numeric_only=True))

st.subheader("Inference")
st.info(
    "Clear temporal and city-specific AQI patterns are observed, "
    "suggesting strong environmental and seasonal influences."
)
