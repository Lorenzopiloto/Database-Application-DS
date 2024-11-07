#Manipulacao de Arquivos
#é util para o dia a dia do cientista de dados
#possui uma serie de funcoes de leitura e gravacao de arquivos - algumas NATIVAS (open e close)
#o formato .TXT é NATIVO tb

#ja os formatos .CSV e .JSON precisam de bibliotecas proprias

print('Abrindo o arquivo')
arqAlunos = open('alunos_idade.txt', encoding='UTF-8')

print('\nLer linha do arquivo e imprimir')
linha = arqAlunos.readline()
print(linha)
linha = arqAlunos.readline()
print(linha)
linha = arqAlunos.readline()
print(linha, end='')
linha = arqAlunos.readline()
print(linha, end='')

for linha in arqAlunos:
    print(linha)

print('\nLer e imprimir novamente o arquivo a partir do inicio')
arqAlunos.seek(0)
for linha in arqAlunos:
    print(linha, end='')

print('\nLer e imprimir todas as linhas no formato de lista')
arqAlunos.seek(0)
listaLinhas = arqAlunos.readlines()
print(listaLinhas)

print('\nImprimindo uma linhas especifica a partir da lista')
print(listaLinhas[2])

print('\nLer e imprimir o arquivo completo')
arqAlunos.seek(0)
textoCompleto = arqAlunos.read()
print(textoCompleto)

#Entendendo a posicao do ponteiro/cursor/apontador do arquivo
print('\nDescobrindo onde esta o ponteiro')
print(f'Posicao do cursor:{arqAlunos.tell()}')

print('\nVoltando para uma posicao e imprimindo uma linha a partir da posicao')
arqAlunos.seek(38)
print(arqAlunos.readline())
print(f'Posicao do cursor:{arqAlunos.tell()}')

#Aproveitando a leitura do texto completo para falar de slicing
#slicing
#texto[inicio:fim:passo] --> passo = pulo
print('\nPegando um trecho do arquivo')
arqAlunos.seek(0)
textoCompleto = arqAlunos.read()
trecho = textoCompleto[38:112]
print(trecho)

print('\nPegando um trecho do arquivo com pulo')
arqAlunos.seek(0)
textoCompleto = arqAlunos.read()
trecho = textoCompleto[38:112:3]
print(trecho)

print('\nTrechos de arquivos com a funcao READ')
arqAlunos.seek(38)
pedacoTexto = arqAlunos.read(74)
print(pedacoTexto)

print('\nÉ obrigacao fechar um arquivo')
arqAlunos.close()
print('\nVerificadndo se esta fechado')
if arqAlunos.closed:
    print('Arquivo fechado')

#Escrevendo um .TXT
print('\nEscrever um arquivo .txt')
arqOlaMundo = open('ola_mundo.txt', 'w',  encoding='UTF-8')
print('\nEscrevendo uma linha no arquivo')
arqOlaMundo.write('Ola mundo')
arqOlaMundo.write('Bom dia')
arqOlaMundo.write('\nComo esta?')
arqOlaMundo.close()

print('\nEscrever um arquivo a partir de uma lista')
listaHobbys = ['jardinagem', 'viagem', 'jogo de tabuleiro', 'leitura']
arqHobbys =open('hobbys.txt', 'w', encoding='UTF-8')
arqHobbys.writelines(listaHobbys)

print('\nEscrever um arquivo a partir de uma lista com pula linha')
listaHobbys = ['jardinagem','\n', 'viagem', '\n','jogo de tabuleiro', '\nleitura']
arqHobbys =open('hobbys.txt', 'w', encoding='UTF-8')
arqHobbys.writelines(listaHobbys)

# Leia o arquivo disponibilizado em aula e escreva imprima os primeiros 10 carateres
print('1a abordagem OPEN CLOSE READ')
arqProduto = open('Fiap_aula_arquivos.txt', 'r',  encoding='UTF-8')
print(arqProduto.read(10))
arqProduto.close()

print('2a abordagem OPEN CLOSE READLINE - NAO RECOMENDADO')
arqProduto = open('Fiap_aula_arquivos.txt', 'r',  encoding='UTF-8')
print(arqProduto.readline(10))
arqProduto.close()

print('3a abordagem OPEN CLOSE SLICING')
arqProduto = open('Fiap_aula_arquivos.txt', 'r',  encoding='UTF-8')
textoCompleto = arqProduto.read()
print(f'{textoCompleto[0:10]}')
arqProduto.close()

# ▪ Leia o arquivo disponibilizado em aula e separe em linhas. Conte quantas linhas tem o arquivo.
print('\n1a abordagem contagem de linhas READLINES + LEN')
arqProduto = open('Fiap_aula_arquivos.txt', 'r',  encoding='UTF-8')
listaLinhas = arqProduto.readlines()
print(f'{len(listaLinhas)} linhas')
arqProduto.close()

# ▪ Feche o arquivo e verifique se ele está fechado.
# ▪ Leia um arquivo e imprima suas linhas uma a uma. (não use lista)

print('\n2a abordagem contagem de linhas FOR')
print('verificando se esta fechado')
print('imprimindo linha a linha')
arqProduto = open('Fiap_aula_arquivos.txt', 'r',  encoding='UTF-8')
i = 0
for linha in arqProduto:
    print(linha, end='')
    i += 1
print(f'{i} linhas')
arqProduto.close()
if arqProduto.closed:
    print('Arquivo fechado')



# ▪ Imprima o arquivo anterior novamente.
# ▪ Transforme o arquivo em uma lista de linhas para serem impressas!
print('\nImprime novamente e lista de linhas')
arqProduto = open('Fiap_aula_arquivos.txt', 'r',  encoding='UTF-8')
print(arqProduto.readline())
#se o arquivo ja estiver aberto anteriormente use o seek
arqProduto.seek(0)
listaLinhas = arqProduto.readlines()
print('Imprimindo a lista de linhas como lista')
print(listaLinhas)
print('Imprimindo a lista de linhas com itens')
for item in listaLinhas:
    print(item, end='')
arqProduto.close()



# ▪ Dada a lista abaixo, escreva em um aquivo
# ▪ ListaCapitais = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba’]
ListaCapitais = ['São Paulo\n', 'Rio de Janeiro\n', 'Belo Horizonte\n', 'Curitiba\n']
print('\n1a Abordagem Criando arq Capitais e escrevendo com WRITELINES')
arqCapitais = open('capitais.txt', 'w', encoding='UTF-8')
arqCapitais.writelines(ListaCapitais)
arqCapitais.close()


ListaCapitais = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
print('\n2a Abordagem Criando arq Capitais e escrevendo com WRITE')
arqCapitais = open('capitais.txt', 'a', encoding='UTF-8')
arqCapitais.write('\n2o exercicio\n')
for item in ListaCapitais:
    arqCapitais.write(item + '\n')
arqCapitais.close()


# ▪ DESAFIO: reescreva o algoritmo anterior para pedir todos os itens de compras separados por
# vírgula e mantenha escrevendo os itens em linhas separadas.
# A entrada de dados: pao, macarrao,café, tomate
# A saida em arquivo
# pao
# macarrao
# café
# tomate
# ▪ Leia um arquivo e escreva outro igual
#compras='pao,macarrao,café,tomate'
print('\ntestes com strip e split')
compras='         pao macarrao café tomate'
print(compras)
print(compras.strip())
print(compras.split())
compras='pao,macarrao,café,tomate'
print(compras.split())
print(compras.split(sep=','))

print('\nCriando arquivo de lista de compras')
listaCompras = compras.split(sep=',')
arqCompras = open('compras.txt','w',encoding='utf-8')
for item in listaCompras:
    arqCompras.write(item + '\n')



# ▪ Leia um arquivo e escreva outro com as primeiras 3 letras de cada linha
# ▪ Manipule o arquivo anterior para acrescentar mais 5 linhas em com a palavra música









