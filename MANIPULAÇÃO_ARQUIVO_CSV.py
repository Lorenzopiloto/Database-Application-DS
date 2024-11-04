#Um arquivo csv é aquele cujos itens sao separados por virgula, ponto e virgula

# print('Revisao a jato de txt')
# arqAlunos = open('alunos_idade.csv', mode = 'r', encoding='UTF-8')
# textoCompleto = arqAlunos.read()
# print(textoCompleto)
# arqAlunos.close()


import csv
print('\nManipulando arquivo csv')
print('Lendo como lista')
with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    tabelaAlunos = csv.reader(arqAlunos, delimiter=';')
    print(type(tabelaAlunos))
    print(tabelaAlunos)
    print('\nPulando uma linha - cabecalho do arquivo')
    next(tabelaAlunos)
    #o python disponibiliza o objeto csv_reader como elemento iteral
    for linha in tabelaAlunos:
        print(linha)

print('\nConvertendo o objeto reader em uma lista')
with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    tabelaAlunos = list(csv.reader(arqAlunos, delimiter=';'))
    print(type(tabelaAlunos))
    print(tabelaAlunos)
    print('\nImprimindo um sobrenome especifico')
    print(tabelaAlunos[1][1])

with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    tabelaAlunos = list(csv.DictReader(arqAlunos, delimiter=';'))
    print(type(tabelaAlunos))
    print(tabelaAlunos)
    print('\nAcessando um elemento especifico')
    print(tabelaAlunos[1]['sobrenome'])

print('\nEscrevendo um arquivo csv')
dadosAlunos=[
    ['nome', 'sobrenome', 'idade'],
    ['Patricia', 'Angelini', 52],
    ['João', 'Pedro', 12]
]
with open('novos_alunos.csv', mode='w+', encoding='UTF-8', newline='') as arqAlunos:
    tabelaAlunos=csv.writer(arqAlunos,delimiter=';')
    tabelaAlunos.writerows(dadosAlunos)
print('\nEscrevendo um unico aluno')
aluno=['Caique','Nascimento',27]
with open('novos_alunos.csv', mode='a+', encoding='UTF-8', newline='') as arqAlunos:
    tabelaAlunos=csv.writer(arqAlunos,delimiter=';')
    tabelaAlunos.writerow(aluno)

print('\nEscrevendo um arquivo a partir de uma lista de dicionarios')
chaves = ['nome', 'sobrenome', 'idade']
dadosAlunos=[
    {'nome':'Patricia', 'sobrenome':'Angelini', 'idade':52},
    {'nome':'Fabio', 'sobrenome':'Pedro', 'idade':12}
]

with open('novos_alunos_dic.csv', mode='w+', encoding='UTF-8', newline='') as arqAlunos:
    tabelaAlunos=csv.DictWriter(arqAlunos,delimiter=';', fieldnames=chaves)
    tabelaAlunos.writeheader()
    tabelaAlunos.writerows(dadosAlunos)

#algumas facilidades de sistema operacional
print('\nRemovendo um arquivo')
import os
os.remove('lixo.txt')


# Abra o arquivo anterior com with e só imprima as linhas pares

import csv

with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos:
    tabelaAlunos = csv.reader(arqAlunos, delimiter=';')
    next(tabelaAlunos)
    numLinha = 1
    for linha in tabelaAlunos:
        if numLinha % 2 == 0:
            print(linha)
        numLinha += 1


# ▪ Abra o arquivo anterior com with e grave outro arquivo linha a linha acrescentando um
# NUMERO crescente ao inicio de cada linha
with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos, \
     open('alunos_idade_copia.csv', 'w', encoding='UTF-8', newline ='') as arqAlunosCopia:
    tabAlunoLeitura = csv.reader(arqAlunos)
    tabAlunoEscrita = csv.writer(arqAlunosCopia)
    seq = 0
    dado = []
    for linha in tabAlunoLeitura:
        if seq == 0:
            dado = ['seq' + ';' + linha[0]]
        else:
            dado = [str(seq) + ';' + linha[0]]
        print(dado)
        tabAlunoEscrita.writerow(dado)
        seq += 1


with open('alunos_idade.csv', 'r', encoding='UTF-8') as arqAlunos, \
     open('alunos_idade_copia.csv', 'w', encoding='UTF-8', newline ='') as arqAlunosCopia:
    tabAlunoLeitura = csv.reader(arqAlunos, delimiter=';')
    tabAlunoEscrita = csv.writer(arqAlunosCopia, delimiter=';')
    seq = 0
    dado = []
    for linha in tabAlunoLeitura:
        print(linha)
        if seq == 0:
            linha.insert(0,'seq')
            print(linha)
        else:
            linha.insert(0, seq)
        tabAlunoEscrita.writerow(linha)
        seq += 1

# ▪ Remova a copia do arquiv








