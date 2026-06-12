import streamlit as st

st.title("Multiplication Table")

n = st.number_input("Enter a Number", step=1)

if st.button("Generate Table"):
    for i in range(1, 11):
        st.write(f"{int(n)} x {i} = {int(n) * i}")