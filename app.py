from datetime import datetime
import streamlit as st

st.title('My First Data Driven WebApp')
st.header("User Info")
st.subheader("Registration")

first_name = st.text_input("Enter first name")
last_name = st.text_input("Enter last name")
year_of_birth = st.number_input("Enter your year of birth")
start_FIU_year = st.number_input("Enter the year you started FIU")

current_year = datetime.now().year
age = current_year - year_of_birth
years_at_FIU = current_year - start_FIU_year

if first_name and last_name and year_of_birth and start_FIU_year:
    st.success(f"Hi {first_name}, you are {age} years old, and you have been at FIU for {years_at_FIU} year.")
    st.warning("You are missing one field")
    st.error("Year of birth must be a number")
    st.info("This is a user registration form")