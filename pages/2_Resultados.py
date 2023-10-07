import streamlit as st
import pandas as pd
from myutil import categorizar

df = st.session_state["data"]
    
st.subheader('Resultados dos jogos')

filtro = st.sidebar.radio(
    "***Categorias***",
    ["todos","forte", "intermediário", "fraco"],
    captions = ["0 a 7","0, 1 e 2", "3 e 4", "5, 6 e 7"])

if filtro != 'todos':
    filtrado = (df['categoria'] == filtro)
    resultado = df[filtrado]
    st.write(resultado)
else:
    st.write(df)