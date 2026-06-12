import streamlit as st

st.title("Factors of a Number")

n = st.number_input("Enter a Number", min_value=1, step=1)

if st.button("Find Factors"):
    st.write("Factors are:")

    for i in range(1, int(n) + 1):
        if int(n) % i == 0:
            st.write(i)