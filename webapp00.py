# myFirstStreamlitApp.py
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import base64

rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTe21GxyDLN7cDFuV5O_fkqoeMV8TZ5g3SMBSajcgnbzWhm6FfUBqGlurFSrYn_kzTIufwRlVyxH5-e/pub?gid=1623706195&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD))
dfD.columns = ['DataHora', 'opiniao', 'resumo', 'idade']
st.DataFrame(dfD)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Prof. Massaki Igarashi - 02/10/23")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Teste de Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Bem vindos!")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.info("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

st.warning("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")
