import streamlit as st

st.title("Conclusions")

st.markdown("""
### Summary
- AQI varies strongly across cities and seasons
- Data preprocessing improves model reliability
- Ensemble models provide the best predictive performance

### Future Enhancements
- Incorporate meteorological variables
- Enable real-time AQI prediction
- Deploy dashboard publicly
""")

st.subheader("Recommendations")
st.markdown("""
- Targeted City Interventions: Delhi, Gurugram, Patna, and Lucknow need urgent action—stricter emission controls, awareness drives, and cleaner energy adoption.
- Focus on PM2.5 & CO: These two pollutants most strongly influence AQI; reducing their sources should be the top priority.
- Seasonal Strategies: AQI spikes in winter and spring call for tighter industrial/agricultural controls and timely health advisories.
- Holistic Particulate Control: Since PM2.5 and PM10 are closely linked, solutions must address both together for maximum impact
""")
