import streamlit as st

st.title("Arithmetic Operations")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

if st.button("Calculate"):
    st.write("Addition =", num1 + num2)
    st.write("Subtraction =", num1 - num2)
    st.write("Multiplication =", num1 * num2)

    if num2 != 0:
        st.write("Division =", num1 / num2)
    else:
        st.error("Division by zero is not allowed")