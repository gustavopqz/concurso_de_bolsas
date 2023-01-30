import streamlit as st
import pandas as pd

st.title('Concurso de bolsas 2023.1')

df = pd.read_csv('resultado.csv',delimiter= ';')

inputNome = st.text_input('Digite o nome do candidato:').replace(' ','').lower()

nomes = df['Nome candidato']
def info(conteudo):
    for elem in conteudo:
        return elem

infoCandidato = {}

def getInfo(*args):
    tuple = args
    candidatoSelecionado = ''.join(tuple)
    candidato = df.loc[df['Nome candidato'] == candidatoSelecionado]


    idAvaliacao = info(candidato['ID avaliação'])
    avaliacao = info(candidato['Avaliação'])
    finalizacao = info(candidato['Finalização'])
    codCandidato = info(candidato['Cód. cand.'])
    nomeCandidato = info(candidato['Nome candidato'])
    curso = info(candidato['Inscrição curso'])
    dataEnvio = info(candidato['Enviada'])
    situacao = info(candidato['Situação'])
    nota = info(candidato['Nota'])
    notaMinima = info(candidato['Nota Mínima'])
    avaliador = info(candidato['Avaliador'])
    dataCorrecao = info(candidato['Data correção'])
 
    infoCandidato = {
        'Nome do candidato': [nomeCandidato],
        'Código do candidato': [codCandidato],
        'ID Avaliação': [idAvaliacao],
        'Avaliação': [avaliacao],
        'Curso': [curso],
        'Nota': [nota],
        'Nota mínima': [notaMinima],
        'Data de envio': [dataEnvio],
        'Data de correção': [dataCorrecao],
        'Avaliador': [avaliador],
        'Situação': [situacao],
        'Finalização': [finalizacao]
    }
    st.title(nomeCandidato)
    st.table(pd.DataFrame.from_dict(infoCandidato, orient='index'))

for nome in nomes:
    separado = nome.lower().split(' ')
    if nome.replace(' ','').lower() == inputNome:
        st.button(nome, on_click=getInfo, args=nome)
    elif separado[0] == inputNome or separado[1] == inputNome:
        st.button(nome, on_click=getInfo, args=nome)
    elif separado[0] + separado[1] == inputNome:
        st.button(nome, on_click=getInfo, args=nome)
    