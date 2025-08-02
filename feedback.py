import streamlit as st
from tornado.options import options

st.title("App Feedback")
age = st.number_input("Enter your age")
q1 = st.text("Do you find this app useful? (Yes/No)")
q1Sel = st.selectbox('Do you find this app useful? (Yes/No)', options = ['Yes','No'])
st.text("Rate the quality of the app")
feedback_quality = st.feedback("stars")

if st.button("Submit"):
    pass

