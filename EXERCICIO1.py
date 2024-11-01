# . Lista de Compras
# o Crie uma lista com pelo menos 5 itens que você compraria em
# uma ida ao supermercado. Remova o terceiro item da lista e
# adicione dois novos itens ao final. Mostre a lista final.
lCompras = ['mamao', 'suco de laranja', 'cafe', 'pao integral', 'queijo canastra']
print(lCompras)

#dois tipos de remocao
#nativa do python
del lCompras[2]
print(lCompras)

#com metodo de lista
lCompras.pop(2)
print(lCompras)

#removendo o item pelo nome
lCompras.remove('mamao')
print(lCompras)

#acrestando no final
#elemento a elemento
lCompras.append('cafe')
lCompras.append('mamao')

print(lCompras)

#os dois elementos de uma vez
lCompras.extend(['leite','ovos'])
print(lCompras)


# Dada uma lista de nomes de alunos, ordene a lista em ordem
# alfabética. Em seguida, adicione um novo aluno no início da lista
# e outro no final.
lAlunos = ['Rebeca', 'Diego', 'Renata', 'Lis', 'Andre']
print(lAlunos)
#ordenacao (temporaria) com a funcao nativa
print(sorted(lAlunos))
print(lAlunos)

lAlunosOrdenada = sorted(lAlunos)
print(lAlunosOrdenada)

#metodo sort() DEFINITIVO proprio da lista
print(lAlunos)
lAlunos.sort()
print(lAlunos)

#Adicionando no inicio da lista
lAlunos.insert(0,'Wagner')
print(lAlunos)

#Adicionar no fim da lista
lAlunos.insert(-1, 'Alice')
print(lAlunos)

lAlunos.append('Antonio')
print(lAlunos)


# Crie uma lista com os títulos de 5 livros que você tem na sua
# estante. Substitua o terceiro livro por um novo título. Verifique se
# um determinado livro está na lista

lBiblioteca = ['Senhor dos Aneis', 'Meus dias na livraria Moriaki', 'Nosso Lar', 'O homem que calculava', 'Sertao Veredas']
print(lBiblioteca)
lBiblioteca[3-1]='Torre de Babel'
print(lBiblioteca)

if 'Senhor dos Aneis' in lBiblioteca:
    print ('temos o Senhor dos Aneis')


# o Você tem uma lista com as pontuações dos jogadores em um
# jogo. Encontre a pontuação mais alta, a mais baixa e a média das
# pontuações
lPontuacoes = [10, 2, 3]
print(lPontuacoes)

print(f'Max:{max(lPontuacoes)}, Min:{min(lPontuacoes)}\nMedia:{sum(lPontuacoes)/len(lPontuacoes)}')
print('\n\n')
print(f'''Max:{max(lPontuacoes)}
Min:{min(lPontuacoes)}
Media:{sum(lPontuacoes)/len(lPontuacoes):.2f}''')

lPontuacoes.sort()

print(f'Max:{lPontuacoes[-1]}, Min:{lPontuacoes[0]}\nMedia:{sum(lPontuacoes)/len(lPontuacoes)}')

print(lPontuacoes)
lPontuacoes.sort(reverse=True)
print(lPontuacoes)

# Simule uma fila de atendimento. Adicione três pessoas à fila,
# depois atenda (remova) duas pessoas. Mostre o estado atual da
# fila

lFila=['Sarah', 'Karine', 'Renata', 'Matheus']
print(lFila)
lFila.append('Vinicius')
print(lFila)
lFila.pop(0)
print(lFila)
lFila.pop(0)
print(lFila)

# Crie uma tupla com cinco cores de uma paleta. Acesse e mostre a
# segunda e a quarta cor. Verifique se uma determinada cor está na
# tupla
tPaleta = ('azul', 'verde','vermelho','laranja','cinza')
print(f'''Segunda cor:{tPaleta[1]}
Quarta cor:{tPaleta[3]}
''')
if 'vermelho' in tPaleta:
    print('temos vermelho')


# Crie uma tupla com cinco cores de uma paleta. Acesse e mostre a
# segunda e a quarta cor. Verifique se uma determinada cor está na
# tupla
tPaleta = ('azul', 'verde','vermelho','laranja','cinza')
print(f'''Segunda cor:{tPaleta[1]}
Quarta cor:{tPaleta[3]}
''')
if 'vermelho' in tPaleta:
    print('temos vermelho')


# Crie uma tupla que represente as coordenadas geográficas
# (latitude, longitude) de uma cidade. Mostre essas coordenadas de
# forma formatada.
tCoord = (25.36, -36.89)
sufLat = 'S'
sufLon = 'O'

if tCoord[0] > 0:
    sufLat = 'N'

if tCoord[1] > 0:
    sufLon = 'L'

print(f'''Latitude:{abs(tCoord[0])} {sufLat}
Longitude:{abs(tCoord[1])} {sufLon}''')