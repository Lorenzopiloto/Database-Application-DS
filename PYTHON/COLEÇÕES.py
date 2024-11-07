#####
# COLECOES
###

#sao variaveis (end de memoria) q apresentam mais de um valor
#os elementos/itens podem ser do mesmo tipo de dados ou podem ser tipos de dados diferentes
#TODA colecao é um elemento ITERAVEL, aquele que eu posso percorrer elemento a elemento

#Lista
#Caracteristicas
#a mais comum
#PODEROSA, FLEXIVEL e COMPLETA
#MUTAVEIS - depois de criadas, permitem acrescentar, retirar, modificar elementos
#EXPANSIVEIS - juntar listas numa lista
#PERMITE DUPLICADOS
#PERMITE ACESSO AOS ELEMENTOS POR INDICE - INDEXADA
#ORDENAVEIS **********> se os elementos forem do mesmo tipo

print('LISTAS')
minhaLista = ['cafe', 'agua', 'acucar']
print(minhaLista)

#Entendendo como acessar cada elemento
#               0       1       2          3        4
#              -5       -4       -3         -2        -1
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(len(minhaLista))
print('primeiro elemento:', minhaLista[0])
print('primeiro elemento pelo lado negativo:', minhaLista[-5])
print('ultimo elemento:', minhaLista[4])
print('ultimo elemento pelo lado negativo:', minhaLista[-1])
print('terceiro elemento:', minhaLista[2])

print('\n\nSlicing')
#Slicing ou fatiamento
# capacidade de pegar uma parte do elemento iteravel
# slicing [posicao inicial:posicao final + 1:pulo/incremento]

#               0       1       2          3        4
#              -5       -4       -3         -2        -1
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(minhaLista)
#agua pos 1 e o acucar 2
pequenaLista = minhaLista[1:2+1]
print(pequenaLista)
pequenaLista = minhaLista[0:5:2]
print(pequenaLista)
#agua pos -4 e o acucar -3
pequenaLista = minhaLista[-4:-2]
print(pequenaLista)

#               0       1       2          3        4     5
#     -6     -5       -4       -3         -2        -1
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'canela']
pequenaLista = minhaLista[-4:-2:-1]
print(pequenaLista)
minhaListaInversa = minhaLista[-1:-6:-1]
print(1, minhaListaInversa)
#nao funciona
minhaListaInversa = minhaLista[-1:0:-1]
print(2, minhaListaInversa)

minhaListaInversa = minhaLista[::-1]
print(3, minhaListaInversa)
print(f'3 {minhaListaInversa}')

print('\n\nSlicing em palavras')
frase = 'Meu mundo é bonito'
print(frase)
palavras = frase.split()
print(palavras)
palavrasInversas = palavras[::-1]
print(palavrasInversas)

palavra = 'JOCA'
print(f'{palavra} palavra invertida {palavra[::-1]}')

print('\n\nAcrescentando Elementos')
#               0       1       2          3        4     5
#     -6     -5       -4       -3         -2        -1
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(minhaLista)
print('Acrescentando no final com append')
minhaLista.append('pimenta')
print(minhaLista)
print('Acrescentando em uma posicao especifica')
minhaLista.insert(2, 'nibs de cacau')
print(minhaLista)

print('\n\nEliminando Elementos')
#               0       1       2          3        4     5
#     -6     -5       -4       -3         -2        -1
minhaLista = ['cafe', 'agua', 'acucar', 'cafe', 'canela']
print(minhaLista)
print('Eliminar elemento do final')
minhaLista.pop()
print(minhaLista)
print('Eliminar um elemento especifico pelo indice')
minhaLista.pop(1)
print(minhaLista)
del minhaLista[-1]
print(minhaLista)
print('Eliminar um elemento especifico pelo nome')
minhaLista.remove('acucar')
print(minhaLista)
print('Limpando toda lista')
minhaLista.clear()
print(minhaLista)

print('Eliminando a lista')
del minhaLista
#print(minhaLista)

print('\n\nConstrutores')
outraLista = []
print(outraLista)
outraLista = list(('chantilly', 'baunilha'))
print(outraLista)

print('\n\nExtender uma lista')
complementoLista = ['raspas de limao', 'flor de sal']
print(complementoLista)
outraLista.extend(complementoLista)
print(outraLista)

print('\n\nCriar uma nova lista a partir de 2 listas')
pequenaLista = ['agua', 'acucar']
print(pequenaLista)
novaLista = pequenaLista + complementoLista
print(novaLista)

print('\n\nAchar elementos')
minhaLista = ['cafe', 'agua', 'nibs de cacau', 'acucar', 'cafe', 'canela', 'pimenta']
onde = minhaLista.index('nibs de cacau')
print(f'nibs de cacau na posicao: {onde}')
if 'canela' in minhaLista:
    print('tem canela')

print('\n\nORDENACAO: listas com elementos do mesmo tipo sao ORDENAVEIS')
minhaLista = ['cafe', 'agua', 'nibs de cacau', 'acucar', 'cafe', 'canela', 'pimenta']
print(minhaLista)
#aqui eu crio uma nova lista ordenada, entao minha lista original continua intacta
minhaListaOrdenada = sorted(minhaLista)
print(minhaListaOrdenada)

#fazendo um estudo dos .sort() e do sorted()
print('\n\nESTUDO DO SORTED E SORT')
print('SORTED')
print('original:', minhaLista)
print('o sorted() ordena temporariamente a minhaLista dentro do print')
print('sorted():', sorted(minhaLista))
print('o sorted() nao afeta a lista original')
print('original:', minhaLista)

print('SORT')
print('original:', minhaLista)
minhaLista.sort()
print('o sort() AFETA a lista original')
print('original:', minhaLista)

print('\n\nListas com tipos <> nao sao ordenaveis')
listaTiposDif = ['Renata', 'Luiz', 12, 2, True, ['Puppy', 'Mel']]
print(listaTiposDif)
#listaTiposDif.sort()

print('\n\nVarrendo a Lista')
for elemento in listaTiposDif:
    print(elemento)

print(len(listaTiposDif))
print(type(listaTiposDif))




# # Acabou a pandemia, chegou o dia e você está ajudando a montar a lista de uma pequena
# # reunião no seu apartamento. Conversando com o seu síndico ele proibiu que houvesse mais
# # de 15 pessoas no seu apartamento. Faça um algorimo que peça a quantidade de pessoas da
# # sua reunião. E utilizando a função FOR peça o nome dos convidados um a um. Certifique-se
# # que seu melhor amigo João está na sua lista
# titulo = 'Reuniao pos pandemia'
# print(f'{titulo:30}')
#
# qtd_max_pessoas = 15
# qtd_anfitrioes = 3
# qtd_convidados = int(input('Entre com a qtd de convidados: '))
# lConvidados = []
#
# if qtd_convidados > qtd_max_pessoas - qtd_anfitrioes:
#     print(f'O sindico TIM MAIA proibiu mais de {qtd_max_pessoas} pessoas e ja temos {qtd_anfitrioes} anfitrioes')
# else:
#     for i in range(qtd_convidados):
#         nome = input(f'Entre com o nome do {i+1}o convidado:')
#         lConvidados.append(nome)
#     if 'João' in lConvidados:
#         print('Lembrou do João')
#     else:
#         if qtd_convidados + 1 < qtd_max_pessoas - qtd_anfitrioes:
#             resp = input('Quer convidar o João? ').lower()
#             if resp in ('s', 'sim', 'yes', 'y'):
#                 lConvidados.append('João')
#                 print('o João foi acrescentado a lista')
#     print(lConvidados)
#     listaConvidadosOrdenada = sorted(lConvidados)
#     print(listaConvidadosOrdenada)
#     #esse muda a ordem na lista original
#     lConvidados.sort()
#     print(lConvidados)
#
# # Falando com a portaria, foi pedido que adicionasse o número do RG em frente cada um dos
# # nomes dos convidados. Altere seu algoritmo para colocar esses documentos na ordem
# # solicitada. Exemplo ['Pat', 345453, 'Hamilton', 924504]
# lConvRG = []
# for nome in lConvidados:
#     RG = int(input(f'Entre com o RG do {nome}:'))
#     lConvRG.append(nome)
#     lConvRG.append(RG)
# print(lConvRG)
# # lConvidados = lConvRG
# # del lConvRG

# Você percebeu que esse primeira reunião vai passar de 20 pessoas e você alugou o salão de
# festas do seu condomíno. Sendo assim você vai precisar alterar seu algoritmo e agora não
# vai mais utilizar o comando FOR, vai utilizar o comando WHILE e enquanto a resposta da
# pergunta “Tem mais convidados” for igual a SIM você cadastrará um novo amigo na sua lista.
resp = 's'
lConvidados = []
while resp in ('s', 'sim', 'yes', 'y'):
    nome = input(f'Entre com o nome do convidado:')
    lConvidados.append(nome)
    rg = int(input('Entre com o RG do convidado:'))
    resp = input('tem mais convidados? ')
print(lConvidados)
# A cada dia mais perto da sua festa, alguns amigos ainda estão meio noiados com a transmissão do virus (e não é para menos com tantas variantes de depois de tantos mortos).
# Seu amigo João é um deles. Infelizmente ele pediu para ser retirado da lista. Remova o João
# a List
if 'João' in lConvidados:
    lConvidados.remove('João')
print(lConvidados)

minhaLista = ['cafe', 'agua', 'nibs de cacau', 'acucar', 'cafe', 'canela', 'pimenta']
print(minhaLista)

for item in minhaLista:
    print(item)

for indice in range(len(minhaLista)):
    print(f'na posicao {indice} esta o elemento {minhaLista[indice]}')

