import streamlit as st
import pandas as pd
import random

st.title('Concurso de bolsas 2023.1')

df = pd.read_excel('CDB UNIFAN 2023.1.xlsx')

inputNome = st.text_input('Digite o nome do candidato:', placeholder='1° nome || 1° e 2° nome || Nome completo || CPF').replace(' ','').lower()

nomes = df['Nome candidato']
cpfs = df['CPF']

def info(conteudo):
    for elem in conteudo:
        return elem

infoCandidato = {}

def getInfo(*args):
    tuple = args
    candidatoSelecionado = ''.join(tuple)
    candidato = df.loc[df['Nome candidato'] == candidatoSelecionado]


    nomeCandidato = info(candidato['Nome candidato'])
    cpf = str(info(candidato['CPF'])).replace('.','')
    if len(cpf) > 11:
        st.write(cpf)
        cpf = cpf.rstrip(cpf[-1])
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    curso = info(candidato['CURSO'])
    modalidade = info(candidato['MODALIDADE'])
    nota = info(candidato['Soma de Nota'])
    colocacao = info(candidato['COLOCAÇÃO'])
    status = info(candidato['STATUS'])
    bolsa = info(candidato['% BOLSA'])
    if bolsa < 1:
        bolsa = str(bolsa)[2:] + '0%'
 
    infoCandidato = {
        'Nome do candidato': [nomeCandidato],
        'CPF': [cpf],
        'CURSO': [curso],
        'MODALIDADE': [modalidade],
        'NOTA': [nota],
        'COLOCACAO': [colocacao],
        'STATUS': [status],
        'BOLSA': [bolsa]
    }
    st.title(nomeCandidato)
    st.subheader(f'CPF: {cpf}')
    if status == 'APROVADA':
        st.success(f'Aprovado em {curso} - {modalidade} com {bolsa}!')
    else:
        st.error('Reprovado!')
    dfFromDict = pd.DataFrame.from_dict(infoCandidato, orient='index')
    st.table(dfFromDict)

for nome in nomes:
    separado = nome.lower().split(' ')
    if nome.replace(' ','').lower() == inputNome:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')
    elif separado[0] == inputNome or separado[1] == inputNome:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')
    elif separado[0] + separado[1] == inputNome:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')

for cpf in cpfs:
    stringCPF = str(cpf)
    novoCPF = stringCPF.replace('.','')
    if len(novoCPF) < 11:
        novoCPF += '0'
    elif len(novoCPF) > 11:
        novoCPF = novoCPF.rstrip(novoCPF[-1])
    if len(novoCPF) == 9:
        novoCPF += '00'
    elif len(novoCPF) == 10:
        novoCPF += '0'
    
    novoInput = inputNome.replace('.','').replace('-','')
    nome = df.loc[df['CPF'] == cpf]
    nome = info(nome["Nome candidato"])

    if novoCPF == novoInput:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')