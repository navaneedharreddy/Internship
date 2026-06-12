import streamlit as st

st.title("Sum of Digits")

num = st.number_input("Enter a Number", min_value=0, step=1)

if st.button("Calculate Sum"):
    total = 0
    temp = int(num)

    while temp > 0:
        digit = temp % 10
        total += digit
        temp = temp // 10

    st.success(f"Sum of Digits = {total}")