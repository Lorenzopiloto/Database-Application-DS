#Tuplas
#Colecao imutavel, ou seja, nao é possivel acrescentar, retirar ou modificar elementos

#Caracteristicas
#IMUTAVEL
#Indexadas, cada elemento tem uma posicao
#Permitem duplicados
#Permitem elementos de tipos de dados diferentes

# tuple --> ()
# list --> []
# dict --> {}


print('TUPLAS')
minhaTupla = ('sono', 'sol', 'comida', 'sono')
print(minhaTupla)
print(type(minhaTupla))
print(len(minhaTupla))

# ---> direca da esquerda para direita SOMA 1
# <--- direcao da direita para esquerda RETIRA 1
#    0     1       2         3
#   -4    -3      -2        -1
#('sono', 'sol', 'comida', 'sono')
print('Primeiro elemento positivo', minhaTupla[0])
print('Primeiro elemento negativo', minhaTupla[-4])

print('\n\nSlicing / Fatiamento')
# sol, comida --> 1, 2
# [primeiro elemento: ultimo elemento + 1: incremento ou pulo]
minhaTuplinha = minhaTupla[1:2+1]
print(minhaTuplinha)
minhaTuplinha = minhaTupla[-3:-2+1]
print(minhaTuplinha)
#se eu quiser inverter ou seja comida, sol tenho q fazer o incremento negativo
# ---> direca da esquerda para direita SOMA 1
# <--- direcao da direita para esquerda RETIRA 1
#    0     1       2         3
#   -4    -3      -2        -1
#('sono', 'sol', 'comida', 'sono')
minhaTuplinha = minhaTupla[-2:-3-1:-1]
print(minhaTuplinha)

#Tupla tem uma representacao diferente qdo se trata de ter um elemento sozinho na tupla
#Normalmente nos esperariamos assim
#minhaTuplaUmElemento = ('um')
#mas isso nao acontece
print('\n\n Tupla de um elemento')
print('Falsiane')
minhaTuplaUmElementoFalsiane = ('um')
print(minhaTuplaUmElementoFalsiane)
print(type(minhaTuplaUmElementoFalsiane))
#e como fazer uma tupla de um elemento
print('Verdadeira')
minhaTuplaUmElemento = ('um',)
print(minhaTuplaUmElemento)
print(type(minhaTuplaUmElemento))

print('\n\nOrdenacao')
#é possivel fazer ordenacao?
#nao é possivel pq ela é IMUTAVEL
#mas se eu precisar ordenar
print('Gambiarra da Ordenacao')
#o sorted é o metodo nativo que faz ordenacao mas que converte o objeto tupla em lista
minhaColecao = sorted(minhaTupla)
print(minhaColecao)
print(type(minhaColecao))
#para voltar eu preciso sobreescrever, usando o metodo tuple
# para fazer a conversao de lista para tupla
minhaTupla = tuple(minhaColecao)
print(minhaTupla)
print(type(minhaTupla))
del minhaColecao

#tem como acrescentar elementos numa tupla?
#nao temn
print('\n\nTupla Vazia')
tuplaInicial = ()
print(tuplaInicial)
tuplaInicial = tuple()
print(tuplaInicial)
print('COMPLETAMENTE INUTIL')

#e COMO ACRESCENTAR
print('\n\nAcrescentando Elementos GAMBIARRA - SOLUCAO DE CONTORNO')
minhaColecao = list(tuplaInicial)
minhaColecao.append('elemento')
print(minhaColecao)
print(type(minhaColecao))
tuplaInicial = tuple(minhaColecao)
print(tuplaInicial)

print('\n\nIndexacao em Tupla')
minhaTupla = ('sono', 'sol', 'comida', 'sono')
if 'sol' in minhaTupla:
    print('O sol mora na posicao', minhaTupla.index('sol'))

print('\n\nRemovendo Elementos GAMBIARRA - SOLUCAO DE CONTORNO')
minhaColecao = list(minhaTupla)
print(minhaColecao)
minhaColecao.remove('comida')
print(minhaColecao)
minhaColecao.pop(1)
del minhaColecao[0]
print(minhaColecao)
minhaTupla = tuple(minhaColecao)
print(minhaTupla)
del minhaColecao

print('\n\nApagando a tupla')
del minhaTupla

minhalista = ['sono', 'sol', 'comida', 'sono']
print(minhalista)
minhalista.remove('sono')
print(minhalista)

# Com esse grande evento você está planejando agora o cardápio. Você deve inicialmente
# montar uma lista de entradas para que sua irmã possa te ajudar. Monte uma lista com
# usando o WHILE com todas as delicias gourmets. Não se esqueça de colocar o queijo
# Roquefort.


listaEntradas = []
resp = 's'
while resp in ('s', 'sim'):
# while (??? condicao de saida do while)
#     #item --> cadatro (input)
    comida = input('Entre com a comida para a festa: ').lower()
#     #colecao + item (como acrescento um item nessa colecao)
    listaEntradas.append(comida)
    resp = input('Quer cadastrar mais uma comida? ').lower()

if 'queijo roquefort' in listaEntradas:
    print('queijo roquefort cadastrado')
else:
    listaEntradas.append('queijo roquefort')

# ▪ Sua irmã não quer providenciar mais nada e para não chateá-la você transformou essa lista
# em uma coleção imutável. Apresente a coleção
tuplaEntradas = tuple(listaEntradas)
del listaEntradas
print(tuplaEntradas)
#comandos equivalentes
# listaEntradas = tuple(listaEntradas)
# print(listaEntradas)




