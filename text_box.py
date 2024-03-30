import streamlit as st

user_input = st.text_input("Enter text")
st.write(f'you entered: {user_input}')
