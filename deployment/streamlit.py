import streamlit as st

st.title("Simple Streamlit app")

user_input=st.text_input("Enter your text:")

if st.button("Show Text"):
    st.write(f"you entered:{user_input}")