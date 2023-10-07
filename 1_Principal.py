import pandas as pd
import streamlit as st

from myutil import categorizar, getExplanatoryText

st.title('Demostração de Vulnerabilidades')
st.write(getExplanatoryText())

df = pd.read_csv(
    'https://gist.githubusercontent.com/PapaGourmet/311644f05cd5c7ef75e63b395ea01128/raw/c6ffc7446db845a972ea3639b254fec3dd1e8a96/mega.csv')
# df.set_index('Data', inplace=True)
df['Data'] = pd.to_datetime(df['Data'])
df['mesrel'] = df['Data'].dt.month
df['mes'] = df['mesrel'].apply(lambda x: pd.Timestamp(
    month=x, day=1, year=2023).strftime('%B'))
df = df.drop(['id'], axis=1)

df = df.sort_values(by='Concurso', ascending=True)

print(df['Data'])

# Exibir o DataFrame ordenado

df['categoria'] = df['desordem'].apply(categorizar)

if "data" not in st.session_state:
    st.session_state["data"] = df
