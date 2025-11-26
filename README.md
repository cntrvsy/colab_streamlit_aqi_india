# CMP7005 - Programming for Data Analysis
## How to Run
Inside github, open the st20343345_CMP7005_PRAC1.ipynb file and click open colab. all the files related to this project are connected here.

## Assessment Summary: 
Air pollution comprises of various chemicals and particles present in the atmosphere, posing significant hazards to both public health and the environment (Lim et al., 2020). Prolonged exposure to air pollution elevates the likelihood of experiencing a stroke, cardiovascular disease, lung carcinoma, and a multitude of other chronic pulmonary conditions (Brauer et al., 2021; Li et al., 2019). Consequently, it is of paramount importance and necessity to mitigate air pollution through the forecasting of air quality. India was ranked among the top five most polluted countries globally in 2024, with an average PM2.5 average AQI level in many cities frequently exceed 400, indicating hazardous conditions for ₅ concentration of 50.6 µg/m³, which is ten times higher than the World Health Organization’s 
recommended limit of 5 µg/m³ (as reported by Haobijam,2025). During peak pollution seasons, particularly in winter, average AQI levels in many cities frequently exceed 400, indicating hazardous conditions to public health. Given the seriousness of this challenge, it is critical to build data-driven systems capable of monitoring and forecasting air pollution. In this assignment, the context of air quality provides a real-world dataset; however, the primary aim is to assess your ability to design and implement software solutions in Python. You will be expected to write modular, reusable, and well-documented code to ingest and process datasets, perform exploratory analysis, construct predictive models, and deliver an interactive platform for data exploration and forecasting. The assessment also evaluates your ability to apply version control and collaboration tools to manage your programming project effectively. 

## Dataset Information: 
The dataset for this assignment contains daily records of air quality data collected across various Indian cities between 2015 and 2020. It includes measurements of particulate matter, gaseous pollutants, and air quality indices. 

**Key Columns:** 
- City, Date 
- Pollutants: PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3 
- Volatile Organic Compounds (VOCs): Benzene, Toluene, Xylene 
- Air Quality Index (AQI) and AQI_Bucket

## Requirements
the following must be present in your choosen environment for the IPYNB file to work.
```
!pip install "vegafusion[embed]>=1.5.0"
!pip install "vl-convert-python>=1.6.0"
!pip install streamlit

import pandas as pd
import numpy as np
import altair as alt
alt.renderers.enable('default')
alt.data_transformers.enable('vegafusion')
```

