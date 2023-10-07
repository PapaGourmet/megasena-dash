import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from myutil import categorizar

df = st.session_state["data"]

print(df.info())

st.subheader('Totais de ganhadores por categoria')


df_disorder = pd.DataFrame(df.groupby(['desordem']).size().reset_index(
    name='concursos'))

df_disorder = df_disorder.sort_values(by='desordem', ascending=True)
concourses = df_disorder['concursos'].to_list()

df_winner = df.groupby(['categoria', 'desordem'])['Ganhadores'].sum(
).reset_index()
df_winner = df_winner.rename(columns={'Ganhadores': 'total'})
wins = df_winner['total'].to_list()
index = df_winner['desordem'].to_list()

df_winner = df_winner.sort_values(by='desordem', ascending=True)

data = {}
data['index'] = index
data['vencedores'] = wins
data['concursos'] = concourses
df_data = pd.DataFrame(data)
df_data = df_data.sort_values(by='index', ascending=True)
print(df_data.info())

st.bar_chart(
    df_data, x="index", y=["vencedores", "concursos"],
    color=["#4169E1", "#FFD700"]
)

explode = [0, 0, 0, 0, 1, 2, 3, 4]

labels = index
sizes = concourses

fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
ax.axis('equal')  # Mantém o gráfico de pizza circular
st.pyplot(fig)
