import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

st.set_page_config(
     page_title="PECVD k value property predictions",
     page_icon="house",
     layout="wide",
     menu_items={
         'Get Help': 'mailto:dht003@ucsd.edu',
         'Report a bug': 'mailto:dht003@ucsd.edu',
         'About': "# Made for NETS Python workshop day 4."
     }
 )

start_time = time.time()

row1, row2 = st.columns((1, 3))
with row1:
    st.title(":house: PECVD k value property predictions")
with row2:
    with st.expander("ℹ️ - About this app", expanded=True):
        st.write(
            """     
            -   The **PECVD k value property predictions** app is an interface built in Streamlit to predict the k value of deposited thin-film precursors under any provided PECVD process conditions.
            """
            )
    
def load_model(url):
    return pickle.load(open(url,'rb'))

linear_model = load_model('Predicting_k_value_model.pkl')

st.write("Input the following process conditions to make predictions:")


co1, co2, co3, co4, co5, co6 = st.columns([1,1,1,1,1,1])
with co1:
    input_var1 = st.number_input(
        "Power (W)",
        value = 300.,
        format = '%.1f',
    )
with co2:
    input_var2 = st.number_input(
        "TFR (mg/min)",
        value = 950.,
        format = '%.1f',
    )
with co3:
    input_var3 = st.number_input(
        "O2-Lo (mg/min)",
        value = 50.,
        format = '%.1f',
    )
with co4:
    input_var4 = st.number_input(
        "Temperature (C)",
        value = 200.,
        format = '%.1f',
    )
with co5:
    input_var5 = st.number_input(
        "Pressure (torr)",
        value = 7.5,
        format = '%.1f',
    )
with co6:
    input_var6 = st.number_input(
        "He (sccm)",
        value = 300.,
        format = '%.1f',
    )
        
input_process_condition = pd.DataFrame([input_var1, input_var2, input_var3, input_var4, input_var5, input_var6])

input_process_condition = input_process_condition.T

st.write("Predict k value = ")
st.write(str(linear_model.predict(input_process_condition)[0]))


