import streamlit as st
from multiapp import MultiApp

import data_overview
import exploratory_analysis
import modelling_prediction
import conclusions

st.set_page_config(
    page_title="Air Quality Dashboard",
    layout="wide"
)

app = MultiApp()

app.add_app("📊 Data Overview", data_overview.app)
app.add_app("📈 Exploratory Data Analysis", exploratory_analysis.app)
app.add_app("🤖 Modelling & Prediction", modelling_prediction.app)
app.add_app("🧠 Conclusions", conclusions.app)

app.run()
