import streamlit as st
import pandas as pd

df = pd.read_csv('resultado.csv',delimiter= ';')

inputNome = st.text_input('Digite o nome do candidato:').replace(' ','').lower()

nomes = df['Nome candidato']

for nome in nomes:
    separado = nome.lower().split(' ')
    if nome.replace(' ','').lower() == inputNome:
        def getName():
            candidato = df.loc[df['Nome candidato'] == nome]
            idAvaliacao = candidato['ID avaliação']
            avaliacao = candidato['Avaliação']
            finalizacao = candidato['Finalização']
            codCandidato = candidato['Cód. cand.']
            nomeCadidato = candidato['Nome candidato']
            curso = candidato['Inscrição curso']
            dataEnvio = candidato['Enviada']
            situacao = candidato['Situação']
            nota = candidato['Nota']
            notaMinima = candidato['Nota Mínima']
            avaliador = candidato['Avaliador']
            dataCorrecao = candidato['Data correção']
            for column in candidato:
                st.markdown(f'{candidato[column]} ')

        st.button(nome, on_click=getName)
        
    elif separado[0] == inputNome or separado[1] == inputNome:
        st.button(nome)
    elif separado[0] + separado[1] == inputNome:
        st.button(nome)

# maria = df.loc[df['Nome candidato'] == 'Maria Eloiza Oliveira Ferreira ']
# idAvaliacao = maria['ID avaliação']
# avaliacao = maria['Avaliação']
# finalizacao = maria['Finalização']
# codCandidato = maria['Cód. cand.']
# nomeCadidato = maria['Nome candidato']
# curso = maria['Inscrição curso']
# dataEnvio = maria['Enviada']
# situacao = maria['Situação']
# nota = maria['Nota']
# notaMinima = maria['Nota Mínima']
# avaliador = maria['Avaliador']
# dataCorrecao = maria['Data correção']

# for column in df:
#     print(df[column][0])

# def getName():
#     nomeCadidato = df.loc[df['Nome candidato']]

# if inputNome:
#     candidato = df.loc[df['Nome candidato'] == inputNome]
#     st.button(inputNome, on_click=getName)

#     for column in candidato:
#         st.markdown(f'{candidato[column].name} - {candidato[column][0]}')




