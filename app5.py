import streamlit as st
import requests
import main_functions

my_keys = main_functions.read_from_file("api_keys.json")
my_nasa_api_key = my_keys["nasa_key"]

st.title('NASA API')
st.subheader('Pictures from Outer Space')

category = st.selectbox('Chose an API', options=['','APOD','Mars Pictures'])
if category == 'APOD':
    url_apod = f"https://api.nasa.gov/planetary/apod?api_key={my_nasa_api_key}"
    response = requests.get(url_apod).json()
    # st.write(response)
    st.title(response["title"])
    col1,col2 = st.columns(2)
    with col1:
        st.image(response["hdurl"])
    with col2:
        explanation = st.checkbox('Explanation')
        if explanation:
            st.write(response["explanation"])
            st.text("Date: " + response["date"])
if category == 'Mars Pictures':
    pass
    # url_mars = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={my_nasa_api_key}"
    # response_mars = requests.get(url_mars).json()
    # main_functions.save_to_file(response_mars,'mars_photos.json')
    # st.write(response_mars)
