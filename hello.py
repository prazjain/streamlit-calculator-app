import streamlit as st

st.write("Hello World from Streamlit")
x = st.text_input("What is your name?")
st.write("Hello " + x)
if (st.button("Click me")):
    st.write("Yes button click works")
