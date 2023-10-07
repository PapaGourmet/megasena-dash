import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from myutil import categorizar

months = [
    "jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out",
    "nov", "dez"
]

df = st.session_state["data"]
st.subheader('Totais de concursos por categoria e desordem ')

df_disorder = pd.DataFrame(df.groupby(
    ['desordem', 'categoria'])['desordem'].count())
df_disorder = pd.DataFrame(df_disorder.rename(
    columns={'desordem': 'concursos'}))
st.write(df_disorder)

df_disorder = pd.DataFrame(df.groupby(['desordem']).size().reset_index(
    name='concursos'))

st.bar_chart(
    df_disorder, x="desordem", y=["concursos"],
    color=["#4169E1"]
)

itens = pd.DataFrame(df.groupby(
    ['mesrel', 'categoria', 'mes']).size().reset_index(name='concursos'))
itens = itens.set_index('mesrel')

strong = itens['categoria'] == 'forte'
strong = list(itens[strong]['concursos'])
intermediate = itens['categoria'] == 'intermediário'
intermediate = list(itens[intermediate]['concursos'])
weak = itens['categoria'] == 'fraco'
weak = list(itens[weak]['concursos'])
dict_category = {}
dict_category['forte'] = strong
dict_category['intermediário'] = intermediate
dict_category['fraco'] = weak
dict_category['meses'] = months
df_category = pd.DataFrame(dict_category)
st.write(itens)

st.bar_chart(
    df_category, x="meses", y=["forte", "intermediário", "fraco"],
    color=["#4169E1", "#FFD700", "#FF6347"]
)
