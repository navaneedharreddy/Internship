import streamlit as st
import pandas as pd

st.title("Read CSV File and Display First 10 Records")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("First 10 Records")
    st.dataframe(data.head(10))