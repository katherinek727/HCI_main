import streamlit as st
import requests

st.title("Currency monitoring")
st.header("Find the latest ctypto price updates")

crypto = st.selectbox("Choose a cryptocurrency", options=[
    '',
    'Bitcoin',
    'Ethereum',
    'Litecoin'
])

if crypto == 'Bitcoin':
    response = request('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USB')