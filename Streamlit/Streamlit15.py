import streamlit as st

st.title("Student Grade Calculator")

name = st.text_input("Enter Student Name")

maths = st.number_input("Enter Maths Marks", min_value=0, max_value=100, step=1)
physics = st.number_input("Enter Physics Marks", min_value=0, max_value=100, step=1)
chemistry = st.number_input("Enter Chemistry Marks", min_value=0, max_value=100, step=1)

if st.button("Calculate Grade"):
    total = maths + physics + chemistry

    if total >= 270:
        grade = "A"
    elif total >= 240:
        grade = "B"
    elif total >= 180:
        grade = "C"
    else:
        grade = "D"

    st.write("Name:", name)
    st.write("Total Marks:", int(total))
    st.success(f"Grade: {grade}")