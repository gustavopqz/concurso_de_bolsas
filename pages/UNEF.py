# IMPORTAÇÕES
import streamlit as st
import pandas as pd
import random

#LEITURA DO ARQUIVO EXCEL
df = pd.read_excel('exemplo.xlsx')

#TÍTULO DA PÁGINA
st.title('Concurso de bolsas UNEF 2023.1!')

#INPUT NOME/CPF
inputNome = st.text_input('Digite o nome do candidato:', placeholder='1° nome || 1° e 2° nome || Nome completo || CPF').replace(' ','').lower()

# PEGANDO OS NOMES E OS CPFS DOS CANDIDATOS PARA VERIFICAÇÃO POSTERIOR
nomes = df['Nome candidato']
cpfs = df['CPF']

#TRAZ SOMENTE A INFORMAÇÃO DESEJADA
def info(conteudo):
    for elem in conteudo:
        return elem

#CRIAÇAO DO OBJETO QUER SERÁ USADO NA TABELA
infoCandidato = {}

#FUNÇÃO QUE TRAZ AS INFORMALÇÕES DO CANDIDATO PESQUISADO
def getInfo(*args):
    tuple = args
    candidatoSelecionado = ''.join(tuple)
    candidato = df.loc[df['Nome candidato'] == candidatoSelecionado]

    #NOME
    nomeCandidato = info(candidato['Nome candidato'])
    #CPF
    cpf = str(info(candidato['CPF'])).split('.')
    novoCPF = cpf[0]
    if len(novoCPF) > 11:
        novoCPF = novoCPF.rstrip(novoCPF[-1])
    elif len(novoCPF) == 9:
        novoCPF = f'00{novoCPF}'
    elif len(novoCPF) == 10:
        novoCPF = f'0{novoCPF}'
    novoCPF = f'{novoCPF[:3]}.{novoCPF[3:6]}.{novoCPF[6:9]}-{novoCPF[9:]}'
    #CURSO
    curso = info(candidato['CURSO'])
    #MODALIDADE
    modalidade = info(candidato['MODALIDADE'])
    #NOTA
    nota = info(candidato['Soma de Nota'])
    #COLOCAÇÃO
    colocacao = info(candidato['COLOCAÇÃO'])
    if str(colocacao) == 'nan':
        colocacao = 'Sem colocação'
    #STATUS
    status = info(candidato['STATUS'])
    #BOLSA
    bolsa = info(candidato['% BOLSA'])
    if bolsa < 1:
        if bolsa == 0.35:
            bolsa = str(bolsa)[2:] + '%'
        else:
            bolsa = str(bolsa)[2:] + '0%'
    else:
        bolsa = '100%'
    instituicao = info(candidato['IES'])
    
    #DICIONÁRIO COM INFORMAÇÕES COLETADAS
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

    #LOGO DA UNIFAN EM QUE O CANDIDATO FEZ A PROVA
    if instituicao == 'UNIFAN':
        st.image('logo-unifan.png', width=250)
    elif instituicao == 'UNEF':
        st.image('logo-unef.png', width=250)

    #NOME DO CANDIDATO EM DESTAQUE
    st.title(nomeCandidato)
    #CPF DO CANDIDATO COMO SEGUNDO DESTAQUE
    st.subheader(f'CPF: {novoCPF}')
    #VERDE PARA APROVADO E VERMELHO PARA REPROVADO COM INFORMAÇÕES DO CURSO E PORCENTAGEM DA BOLSA
    if status == 'APROVADA':
        st.success(f'Aprovado em {curso} - {modalidade} com {bolsa}!')
    else:
        st.error('Reprovado!')
    
    #TABELA COM TODAS AS INFORMAÇÕES DO CANDIDATO
    dfFromDict = pd.DataFrame.from_dict(infoCandidato, orient='index')
    st.table(dfFromDict)

#BOTÕES COM O NOME DOS CANDIDATOS PESQUISADOS
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
    novoCPF = stringCPF.split('.')[0]
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