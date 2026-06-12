import streamlit as st

st.title("Positive, Negative or Zero Checker")

num = st.number_input("Enter a Number")

if st.button("Check"):
    if num > 0:
        st.success("Positive Number")
    elif num < 0:
        st.error("Negative Number")
    else:
        st.info("Zero")