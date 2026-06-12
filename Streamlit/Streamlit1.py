import streamlit as st

st.title("Even or Odd Checker")

num = st.number_input("Enter an Integer", step=1)

if st.button("Check"):
    if num % 2 == 0:
        st.success(f"{int(num)} is an Even Number")
    else:
        st.success(f"{int(num)} is an Odd Number")
        