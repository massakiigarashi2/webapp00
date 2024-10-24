# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("MEU 1º WEB APP STREAMLIT")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Meu prof. Massaki é D+ e muito convencido!")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

col2, col3 = st.columns(2)

with col2:
    st.header("NALA")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("CORUJA")
    st.image("https://static.streamlit.io/examples/owl.jpg")
