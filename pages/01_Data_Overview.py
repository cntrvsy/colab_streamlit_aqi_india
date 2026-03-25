import streamlit as st
from src.utils import load_data

st.title("Data Overview")

df = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", len(df))
col2.metric("Cities", df["City"].nunique())
col3.metric("Features", df.shape[1])

st.subheader("Dataset Preview")
st.dataframe(df.head(), use_container_width=True)

st.subheader("Key Observations")
st.markdown("""
- Dataset spans multiple cities and pollutants
- Contains temporal AQI measurements
- Suitable for trend and predictive analysis
""")
