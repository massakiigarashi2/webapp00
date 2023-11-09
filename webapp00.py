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
city_name = "Campinas"
city_name = st.text_input('Digite a cidade para consulta do clima : ', 'Campinas')
if st.button('Exibir Previsão'):
  st.write('A Cidade escolhida foi ', city_name)
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
   
  # get method of requests module
  # return response object
  response = requests.get(complete_url)
   
  # json method of response object 
  # convert json format data into
  # python format data
  x = response.json()
  
  if x["cod"] != "404":
   
      # store the value of "main"
      # key in variable y
      y = x["main"]
   
      # store the value corresponding
      # to the "temp" key of y
      current_temperature = y["temp"]
   
      # store the value corresponding
      # to the "pressure" key of y
      current_pressure = y["pressure"]
   
      # store the value corresponding
      # to the "humidity" key of y
      current_humidity = y["humidity"]
   
      # store the value of "weather"
      # key in variable z
      z = x["weather"]
   
      # store the value corresponding 
      # to the "description" key at 
      # the 0th index of z
      weather_description = z[0]["description"]
   
      # print following values
      st.write(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
            "\n humidity (in percentage) = " +
                      str(current_humidity) +
            "\n description = " +
                      str(weather_description))
   
  else:
      st.write(" City Not Found ")
 
 
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Clima Rafa - A Previsão do tempo em 09/11/23")
