import streamlit as st
import pandas as pd

df = pd.read_csv('Resultado 2023.1.csv',delimiter= ';')

inputNome = st.text_input('Digite o nome do candidato:').replace(' ','').lower()

nomes = df['Nome candidato']

for nome in nomes:
    separado = nome.lower().split(' ')
    if nome.replace(' ','').lower() == inputNome:
        st.markdown(nome)
        st.markdown(df.loc[df['Nome candidato'] == nome.replace(' ','').lower()])
    elif separado[0] == inputNome or separado[1] == inputNome:
        st.markdown(nome)
    elif separado[0] + separado[1] == inputNome:
        st.markdown(nome)