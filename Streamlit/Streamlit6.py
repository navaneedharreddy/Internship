import streamlit as st

st.title("First 10 Natural Numbers")

if st.button("Display Numbers"):
    for i in range(1, 11):
        st.write(i)