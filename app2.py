import streamlit as st

st.title('Party RSVP')
st.subheader('Come celebrate my birthday party!')

st.sidebar.title('Contact')
st.sidebar.subheader('Any questions about the party?')
contact_method = st.sidebar.selectbox('How do you want to be contacted?',
                                      options=[
                                          '',
                                          'Phone',
                                          'Email',
                                          'Text'
                                      ])
if contact_method:
    contactInfo = st.sidebar.text_input(f'Enter your {contact_method}.')

with st.form('RSVP'):
    name = st.text_input('Enter your name')
    age = st.number_input('Enter your age')
    email = st.text_input('Enter your email address')
    major = st.selectbox('What is your major', options=[
        '','CS','Data Science','IT','Cys','Iot'
    ])
    level = st.radio('Select your degree level', options=[
        'Bachelor', 'Master', 'PhD', 'Other'
    ])
    subscribe =  st.checkbox('Would you like to be notified about future events?')
    submit = st.form_submit_button('Submit')