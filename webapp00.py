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
Cidade = "Campinas"
LINK = "https://api.openweathermap.org/data/3.0/onecall?q={Cidade}&appid={API_KEY}"
# import required modules
# Enter your API key here
api_key = "a30bd09c7884982c30901f15edb9a21e"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = st.text_input("Digite a cidade para consulta do clima : ")
st.write('A Cidade escolhida foi ', city_name)
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object 
# convert json format data into
# python format data
x = response.json()
 


# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Prof. Massaki Igarashi - 09/11/23")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Teste de Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Bem vindos!")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.info("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.warning("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
