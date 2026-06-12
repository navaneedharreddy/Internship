import streamlit as st

st.title("Prime Number Checker")

n = st.number_input("Enter a Number", min_value=0, step=1)

if st.button("Check Prime"):
    n = int(n)

    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                st.error("Not a Prime Number")
                break
        else:
            st.success("Prime Number")
    else:
        st.error("Not a Prime Number")