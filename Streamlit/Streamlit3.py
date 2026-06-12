import streamlit as st

st.title("Compare Two Numbers")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

if st.button("Compare"):
    if num1 > num2:
        st.success("First Number is Greater")
    elif num2 > num1:
        st.success("Second Number is Greater")
    else:
        st.info("Both Numbers are Equal")