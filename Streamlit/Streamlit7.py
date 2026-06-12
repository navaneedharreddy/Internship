import streamlit as st

st.title("First N Natural Numbers")

n = st.number_input("Enter a Number", min_value=1, step=1)

if st.button("Display"):
    i = 1

    while i <= n:
        st.write(i)
        i += 1