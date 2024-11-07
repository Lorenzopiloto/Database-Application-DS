#Map
#Nada mais é que vc aplicar uma funcao em todos os itens de uma colecao

print('\nEntendendo o MAP')
def Ad5 (p):
    res = p + 5
    return res

#TESTE
print(Ad5(10))

lVal = [8, 9, 27, 33]
print(lVal)
print('Aplicando a funcao do modo tradicional')
lVal5 = []
for item in lVal:
    #print(Ad5(item))
    lVal5.append(Ad5(item))
print(lVal5)

def Ad5 (p):
    res = p + 5
    return res
lVal = [10, 8, 9, 27, 33]
print('Usando o MAP')
lVal5Map =list(map(Ad5, lVal))
print(lVal5Map)

#Exercicio FUNCAO DE 20%
def Desc20 (p):
    return round(p*0.8, 2)
lValDesc = list(map(Desc20, lVal))
print(lValDesc)
print(list(map(Desc20, lVal)))

def Desc(v, d):
    if d > 1:
        d = d / 100
    valor = round(v * (1 - d), 2)
    return valor

#teste
print(Desc(100, 30))

lVal = [10, 8, 9, 27, 33]
lDesc = [30, 0.2, 42, 6, .32]

print('\nDo modo dificil')
print('Valores', lVal)
print('Descontos', lDesc)
lDescNovos = []
for i in range(len(lVal)):
    lDescNovos.append(Desc(lVal[i], lDesc[i]))
print('Valores com desconto', lDescNovos)

print('\nCom o MAP')
lDescNovos = list(map(Desc, lVal, lDesc))
print('Descontos com MAP', lDescNovos)



def Desc(v, d=20):
    if d > 1:
        d = d / 100
    valor = round(v * (1 - d), 2)
    return valor
lDescNovos20 = list(map(Desc, lVal))
print('Descontos com MAP 20', lDescNovos20)

#REDUCE
#O reduce ao contrario do MAP junta (segundo uma funcao) todos os elementos de uma lista
print('\nREDUCE')
def Add2 (p1, p2):
    return p1+p2
print(Add2(4,5))

lVal = [10, 8, 9, 27, 33]
print('Valores', lVal)
print('Do jeito dificil')
total = 0
for item in lVal:
    total = Add2(total, item)
print(total)

print('Com REDUCE')
from functools import reduce
total = reduce(Add2, lVal)
print(total)


#Exercicio
#Dada a lista abaixo crie uma funcao de concatenacao de string e use o
#REDUCE para concatenar todos os nomes
lNomes = ['Pat', 'Ana Clara', 'Renata', 'Levi']

def Concatena (s1, s2):
    return s1 + "-" + s2
print(reduce(Concatena, lNomes))


#LAMBDA
#Lambda nada mais é que uma funcao de uma linha só
def Add2 (p1, p2):
    return p1+p2
ldAdd2 = lambda p1, p2 : p1 + p2

print('Teste Funcao Add2', Add2(40, 20))
print('Teste de Lambda ldAdd2', ldAdd2(40, 20))

ldAma = lambda n1, n2: n1 + ' ama ' + n2
print(ldAma('Pat', 'Mel'))
print((lambda n1, n2: n1 + ' ama ' + n2)('Maria', 'Joao'))

#Exercicio
#Descontos com Lambda + MAP
lVal = [10, 8, 9, 27, 33]
lDesc = [0.3, 0.2, 0.42, 0.6, .32]
#Matheus
print(list(map((lambda v,d : round(v*(1-d),2)),lVal,lDesc)))
#Luiz
lval = [10,8,9,27,33]
ldesc = [30,0.2,42,6,.32]

print('Prof',list(map(lambda v, d:round(v * (1 - (d / 100)),2) if d > 1 \
else round(v*(1-d), 2), lval, ldesc)))

descontoslambda = list(map(lambda v, d: round(v * (1 - (d / 100 if d > 1 else d)), 2),lval,ldesc))
print('Luiz', descontoslambda)

# Dada a lista, listaOriginal = [234, 64, 13467, 45.89, 23]
# ▪ Retorne o PROPRIO valor se ele for PAR
listaOriginal = [234, 64, 13467, 45.89, 23]
print(list(map((lambda p : p if p % 2 == 0 else None),listaOriginal)))

#Levi

lst = [47, 11, 42, 13, 9, 10, 12, 18, 20, 31]

print(list(filter(lambda x: x % 2 == 0, lst)))

#Luiz
lista = [234,64,13467,45.89,23]
x = list(map(lambda i: i if i%2==0 else -1, lista))
print(x)

#Maria Clara
lOriginal=[234,64,13467,45.89,23]
func=lambda p: p if p%2==0 else None
print(list(map(func,lOriginal)))

#List Comprehension
#gerador de listas a partir do for
lOriginal=[234,64,13467,45.89,23]
#objetivo é multiplicar cada um dos valores por 3
print('\nList Comprehension')
print(lOriginal)
print('\nDo modo mais dificil')
lTriplos = []
for item in lOriginal:
    lTriplos.append(round(item * 3, 2))
print(lTriplos)

lTriplos = [round(item * 3, 2) for item in lOriginal]
print(lTriplos)

















