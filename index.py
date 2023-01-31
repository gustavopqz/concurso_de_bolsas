import streamlit as st
import pandas as pd
import random

df = pd.read_excel('CDB AMBOS 2023.1.xlsx')

st.title('Concurso de bolsas GRUPO NOBRE 2023.1!')

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
    novoCPF = cpf.replace('.','')
    if len(novoCPF) > 11:
        novoCPF = novoCPF.rstrip(novoCPF[-1])
    elif len(novoCPF) == 9:
        novoCPF = f'00{novoCPF}'
    elif len(novoCPF) == 10:
        novoCPF = f'0{novoCPF}'
    novoCPF = f'{novoCPF[:3]}.{novoCPF[3:6]}.{novoCPF[6:9]}-{novoCPF[9:]}'
    curso = info(candidato['CURSO'])
    modalidade = info(candidato['MODALIDADE'])
    nota = info(candidato['Soma de Nota'])
    colocacao = info(candidato['COLOCAÇÃO'])
    if str(colocacao) == 'nan':
        colocacao = 'Sem colocação'
    status = info(candidato['STATUS'])
    bolsa = info(candidato['% BOLSA'])
    if bolsa < 1:
        bolsa = str(bolsa)[2:] + '0%'
    else:
        bolsa = '100%'
    instituicao = info(candidato['IES'])
 
    infoCandidato = {
        'Nome do candidato': [nomeCandidato],
        'CPF': [novoCPF],
        'CURSO': [curso],
        'MODALIDADE': [modalidade],
        'NOTA': [nota],
        'COLOCACAO': [colocacao],
        'STATUS': [status],
        'BOLSA': [bolsa],
        'INSTITUIÇÃO': [instituicao]
    }
    if instituicao == 'UNIFAN':
        st.image('logo-unifan.png', width=250)
    elif instituicao == 'UNEF':
        st.image('logo-unef.png', width=250)

    st.write(len(cpf))
    st.title(nomeCandidato)
    st.subheader(f'CPF: {novoCPF}')
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
    if len(novoCPF) > 11:
        novoCPF = novoCPF.rstrip(novoCPF[-1])
    elif len(novoCPF) == 9:
        novoCPF = f'00{novoCPF}'
    elif len(novoCPF) == 10:
        novoCPF = f'0{novoCPF}'
    
    novoInput = inputNome.replace('.','').replace('-','')
    nome = df.loc[df['CPF'] == cpf]
    nome = info(nome["Nome candidato"])

    if novoCPF == novoInput:
        st.button(nome, on_click=getInfo, args=nome, key=f'{random.random()}')