import streamlit as st
import pandas as pd
import numpy as np

st.title("SurveyMaster")

survey_name = st.text_input("Name your survey:")
question_types = ["Text", "Multiple Choice", "Rating"]
questions = []

if st.button("Add Question"):
    questions.append(st.text_input(f"Question {len(questions) + 1}:"))

for question in questions:
    st.text(question)
    print(question)

st.header("Distribution Settings")
email_list = st.text_area("Enter emails (separated by commas):")

st.header("Collect Responses")
responses = pd.DataFrame({
    "Q1": np.random.choice(["Yes", "No"], 10),
    "Q2": np.random.randint(1, 6, 10)
})
st.write(responses)

st.header("Results Analysis")
st.bar_chart(responses["Q2"])