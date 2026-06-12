import streamlit as st

st.title("Factorial Calculator")

n = st.number_input("Enter a Number", min_value=0, step=1)

if st.button("Calculate Factorial"):
    factorial = 1

    for i in range(1, int(n) + 1):
        factorial = factorial * i

    st.success(f"Factorial = {factorial}")