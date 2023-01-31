import streamlit as st
import pandas as pd
import random

st.title('Concurso de bolsas 2023.1')

df = pd.read_excel('CDB UNIFAN 2023.1.xlsx')

inputNome = st.text_input('Digite o nome do candidato:').replace(' ','').lower()

nomes = df['Nome candidato']

infoCandidato = {}

def getInfo(*args):
    tuple = args
    candidatoSelecionado = ''.join(tuple)
    candidato = df.loc[df['Nome candidato'] == candidatoSelecionado]


    nomeCandidato = candidato['Nome candidato']
 
    infoCandidato = {
        'Nome do candidato': [nomeCandidato]
    }
    st.title(nomeCandidato)
    st.table(pd.DataFrame.from_dict(infoCandidato, orient='index'))

for nome in nomes:
    separado = nome.lower().split(' ')
    if nome.replace(' ','').lower() == inputNome:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')
    elif separado[0] == inputNome or separado[1] == inputNome:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')
    elif separado[0] + separado[1] == inputNome:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')
    