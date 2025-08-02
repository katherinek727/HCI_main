import streamlit as st
from datetime import datetime, timedelta

st.title("QuickAppointment")

services = st.selectbox("Select the service you want to book:",
                          ["Dental Checkup", "Eye Examination", "General Consultation"])

appointment_date = st.date_input("Enter Date:")
appointment_time = st.time_input("Enter time:")

terms = st.checkbox("I agree to the terms and conditions.", value=False)

if st.button("Book Appointment"):
    # Violation: Assumes correct format without validation or user feedback
    try:
        # datetime.strptime(appointment_date)
        st.success("Your appointment has been booked.")
    except ValueError:
        st.error("Please enter the date and time in the correct format.")