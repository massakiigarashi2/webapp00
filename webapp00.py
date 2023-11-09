# myFirstStreamlitApp.py
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import base64
import requests, json

API_KEY = "a30bd09c7884982c30901f15edb9a21e"
LINK = "https://api.openweathermap.org/data/3.0/onecall?q={Cidade}&appid={API_KEY}"
# import required modules
# Enter your API key here
api_key = "a30bd09c7884982c30901f15edb9a21e"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = st.text_input("Digite a cidade para consulta do clima : ")
st.write('A Cidade escolhida foi ', city_name)

 
# json method of response object 
# convert json format data into
# python format data
#x = response.json()

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Prof. Massaki Igarashi - 09/11/23")
