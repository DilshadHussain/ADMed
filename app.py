# youtube link: https://www.youtube.com/watch?v=HvMxZnrigKY

#packages required
"""
Streamlit
Pandas
numpy
matplotlib
statsmodels
pandas_datareader
datetime
yfinance
sklearn
pyportfolioopt
"""

import pandas as pd
import numpy as np
import streamlit as st
# import matplotlib.pyplot as plt
from datetime import date
import datetime as dt
# import plotly.express as px
# import plotly.graph_objects as go

# read data
@st.cache_data
def load_data():
    df = pd.read_excel("Service Wise Collection Report.xlsx")
    # df = df.iloc[2:]
    return df

df = load_data()


#import sidebar
st.sidebar.header("Please filter here")
clientname =st.sidebar.multiselect(
    "Select the Client:",
    options=df['ClientName'].unique(),
    default=df['ClientName'].unique()
)

# st.dataframe(df)

# doctor sidebar
doctor = st.sidebar.multiselect(
    "Select the Doctor",
    options= df['DoctorName'].unique()
)

percentage = st.sidebar.select_slider(
    "Select percentage",
    options=[
        10,
        20,
        30,
        40,
        50,
        60,
        70,
        80,
        90
    ]
)


####main_page
df_select = df.query(
    "ClientName == @clientname & DoctorName ==@doctor"
)

#no data
if df.empty:
    st.warning("No data found")
    st.stop() #halt streamlit run

#title
st.title(":test_tube: Adarsh Medanta")
st.markdown('##')

#Calculate KPI's
# For whole data
total_pat  = int(len(pd.unique(df['BillNo'])))
# using NetAmt
total_rev_netamt = int(df['NetAmt'].sum())
avg_rev_per_bill_netamt = int(df['NetAmt'].mean())
med_rev_per_bill_netamt = int(df['NetAmt'].median())
# using MRP
total_rev_mrp = int(df['MRP'].sum())
avg_rev_per_bill_mrp = int(df['MRP'].mean())
med_rev_per_bill_mrp = int(df['MRP'].median())

st.write(f"Total subjects:  {total_pat}")
st.write(f"Total Revenue using NetAmt:  {total_rev_netamt}")
st.write(f"Average Revenue per subject using NetAmt:  {avg_rev_per_bill_netamt}")
st.write(f"Median Revenue per subject using NetAmt:  {med_rev_per_bill_netamt}")
st.write(f"Total Revenue using MRP:  {total_rev_mrp}")
st.write(f"Average Revenue per subject using MRP:  {avg_rev_per_bill_mrp}")
st.write(f"Median Revenue per subject using MRP:  {med_rev_per_bill_mrp}")

st.divider()

# For selected doctor
# Handle NaN values by filling with a default value (e.g., 0) 
df_select['NetAmt'] = df_select['NetAmt'].fillna(0)
df_select['MRP'] = df_select['MRP'].fillna(0)

average_price_NetAmt = float(df_select['NetAmt'].mean())
total_price_netamt = float(df_select['NetAmt'].sum())
average_price_MRP = float(df_select['MRP'].mean())
total_price_mrp = int(df_select['MRP'].sum())
total_sample = df_select.shape[0]
total_pat_doc = len(pd.unique(df_select['BillNo']))

NetAmt_percentage = (total_price_netamt*percentage)/100
MRP_percentage = (total_price_mrp*percentage)/100
Total_percentage = NetAmt_percentage+MRP_percentage

st.write("Details of the doctor selected are diplayed below")

total_pat_doc_col, total_netamt_col, netamt_per_col, total_mrp_col, mrp_per_col = st.columns(5)


with total_pat_doc_col:
    st.subheader('Total number of Patients from doctor selected')
    st.subheader(f"{total_pat_doc:,}")

with netamt_per_col:
    st.subheader('NetAmt percentage')
    st.subheader(NetAmt_percentage)

with mrp_per_col:
    st.subheader('MRP percentage')
    st.subheader(MRP_percentage)

with total_netamt_col:
    st.subheader('Total NetAmt')
    st.subheader(total_price_netamt)

with total_mrp_col:
    st.subheader('Total MRP')
    st.subheader(total_price_mrp)


st.divider()


# netamt_per_col, mrt_per,_col, total_per_col

# st.dataframe(df_select)
