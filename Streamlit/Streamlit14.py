import streamlit as st

st.title("Sum of List Elements")

numbers = [10, 20, 30, 40, 50]

if st.button("Calculate Sum"):
    total = 0

    for num in numbers:
        total += num

    st.write("List:", numbers)
    st.success(f"Sum = {total}")