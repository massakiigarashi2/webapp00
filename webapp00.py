# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQtWlwpc4_SPunNRbY9MWEsLemJ4-kr7JK1OE8avUWMU7BULFMQNt6-bFkIsJ-_7nOvH3sFOSyOFkeb/pub?gid=1851101266&single=true&output=csv"
db = Ler_GooglePlanilha(url, coluna_indice = None)
db.columns = ['DataHora', 'Idade', 'Jundiaiense', 'Qualidade', 'Sonho']
Escrever(db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("MEU 1º WEB APP STREAMLIT")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Hejheheheh! Prof. Massaki")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

values = st.slider("Select a range of values", 0.0, 100.0, (5.0, 15.0))
st.write("Values:", values)
