import requests
import main_functions

my_keys = main_functions.read_from_file("api_keys.json")
my_nasa_api_key = my_keys["nasa_key"]

url_mars = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={my_nasa_api_key}"
# response_mars = requests.get(url_mars).json()
# main_functions.save_to_file(response_mars,'mars_photos.json')

mars_photos = main_functions.read_from_file('mars_photos.json')

list_of_cameras = []
for i in mars_photos['photos']:
    camera_name = i['camera']['full_name']
    list_of_cameras.append(camera_name)

unique_camera = set(list_of_cameras)
# print(unique_camera)

import streamlit as st

st.title('Test Mars Photos')
st.subheader('Check Photos from Mars')

camera = st.selectbox('Camera', unique_camera)

if camera:
    for i in mars_photos['photos']:
        if i['camera']['full_name'] == camera:
            st.image(i['img_src'],width=360)