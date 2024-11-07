# #Dicionario
# #Colecao do tipo chave/valor
# #mutaveis
# #indexadas
# #tipos de dados diferentes (incluindo as chaves)
# #Exemplo
# #nome: Patricia
# #sexo nasc: feminino
# #idade: 52
# #construtor da classe: {}, dict
#
# print('Dicionarios')
# meuDicionario = {'nome':'Patricia', 'sexo':'feminino', 'idade': 52}
# print(type(meuDicionario))
# print(meuDicionario)
#
# outroDic = dict((('nome', 'Patricia'),('sexo','feminino'),(52,'idade')))
# print(outroDic)
#
# print('\nAcessando um valor')
# meuNome = meuDicionario['nome']
# print(meuNome)
# print(meuDicionario['idade'])
# print(outroDic[52])
#
# print('\nRecuperando as chaves')
# chaves=meuDicionario.keys()
# print(chaves)
#
# print('\nRecuperando os valores')
# valores=meuDicionario.values()
# print(valores)
#
# print('\nRecuperando os elementos\\itens')
# itens = meuDicionario.items()
# print(itens)
#
# print('\nRecuperando todos as chaves um a um')
# for chave in meuDicionario:
#     print(chave)
# for chave in meuDicionario.keys():
#     print(chave)
#
# print('\nRecuperando todos os valores um a um')
# for valor in meuDicionario.values():
#     print(valor)
#
# print('\nRecuperando todos os valores um a um')
# for item in meuDicionario.items():
#     print(item)
#
# print('\nTruques')
# print('Recuperando os valores a partir da chave')
# for chave in meuDicionario:
#     print(meuDicionario[chave])
#
# print('Recuperando o par chave/valor separado')
# for chave, valor in meuDicionario.items():
#     print(f'Chave:{chave} e o valor:{valor}')
#
# #atribuicao multipla
# temperatura_minima, temperatura_maxima = 6, 27
# print('Max', temperatura_maxima)
# print('Min', temperatura_minima)
#
# print('\nAcrescentando items no dicionario')
# meuDicionario['tipo sanguineo'] = 'O Rh -'
# print(meuDicionario)
#
# print('\nMudando valores')
# meuDicionario['idade']=53
# print(meuDicionario)
#
# print('Mudando valores com update')
# meuDicionario.update({'nome':'Patricia Angelini'})
# print(meuDicionario)
# meuDicionario.update({'estado civil':'casada'})
# print(meuDicionario)
# print('\nApagando itens')
# print('Funcao NATIVA DEL')
# del meuDicionario['estado civil']
# print(meuDicionario)
# print('Popitem - retira o ULTIMO par do dicionario')
# meuDicionario.popitem()
# print(meuDicionario)
# print('Pop - escolho o que eu quero retirar')
# meuDicionario.pop('sexo')
# print(meuDicionario)
#
# meuDicionario = {'nome': 'Patricia Angelini', 'sexo': 'feminino', 'idade': 53, 'tipo sanguineo': 'O Rh -', 'estado civil': 'casada'}
# print(meuDicionario)
# print('\nLocalizando itens')
# if 'idade' in meuDicionario:
#     print('Tem idade nas chaves do meu dicionario')
# if 'Patricia Angelini' in meuDicionario.values():
#     print('Pat esta la')
# if 'idade' in meuDicionario:   
#     print('A idade é:',meuDicionario['idade'])


print('Como gerar uma copia do dicionario')
meuDicionario = {'nome': 'Patricia Angelini', 'sexo': 'feminino', 'idade': 53, 'tipo sanguineo': 'O Rh -', 'estado civil': 'casada'}

copiaDicFake = meuDicionario
print('Original\n', meuDicionario)
print('Copia\n',copiaDicFake)

copiaDicFake.popitem()
print('Depois do popitem')
print('Original\n', meuDicionario)
print('Copia\n',copiaDicFake)

print('\n\nA copia real precisa ser feita pelo metodo copy')
copiaDic = meuDicionario.copy()
print('Original\n', meuDicionario)
print('Copia\n',copiaDic)

copiaDic.popitem()
copiaDic.popitem()
print('Depois do popitem')
print('Original\n', meuDicionario)
print('Copia\n',copiaDic)

# ▪ Como faz muito tempo que vocês não se veem (voce e os convidados) você está
# organizando uma agenda colocando a informação de cada pessoa. Utilize a colecao que
# imita formulario para pegar itens como nome, endereco, telefone, idade
# resp = 's'
lAgenda = []
while resp in ('s','sim'):
    nome = input('Entre com o nome:')
    tel = int(input('Entre com o tel: '))
#    pessoa = {'nome':nome, 'tel':tel}
    interesses = []
    for i in range(3):
        interesses.append(input(f'entre com {i+1}o interesse:'))
#    pessoa['interesse'] = interesses
    pessoa = {'nome':nome, 'tel':tel, 'interesse':interesses}
    lAgenda.append(pessoa)
    resp = input('vc quer cadastrar mais um? ').lower()
print(lAgenda)

resp = 's'
lAgenda = []
while resp in ('s','sim'):
    pessoa = {}
    pessoa['nome'] = input('Entre com o nome:')
    pessoa['tel'] = int(input('Entre com o tel: '))
    lAgenda.append(pessoa)
    resp = input('vc quer cadastrar mais um? ').lower()
print(lAgenda)


resp = 's'
lAgenda = []
while resp in ('s','sim'):
    # pessoa = {}
    # pessoa['nome'] = input('Entre com o nome:')
    # pessoa['tel'] = int(input('Entre com o tel: '))
    lAgenda.append({'nome':input('Entre com o nome: '), 'tel':int(input('Entre com o tel: '))})
    resp = input('vc quer cadastrar mais um? ').lower()
print(lAgenda)

# ▪ Acrescente os dados estado civil na colecao. Você vai montar um novo tinder em breve
lAgenda = [{'nome': 'Pat', 'tel': 123}, {'nome': 'Ro', 'tel': 456}]
for pessoa in lAgenda:
    #print(f'{pessoa['nome']}')
    pessoa['estado civil'] = input(f"Entre com o estado civil de {pessoa['nome']}: ")
    #pessoa.update({'estado civil': input(f"Entre com o estado civil de {pessoa['nome']}: ")})
print(lAgenda)

# ▪ Exclua aquela amigo que colocou um apelido antigo
lAgenda = [{'nome': 'Pat', 'tel': 123}, {'nome': 'Ro', 'tel': 456}, {'nome': 'Jonny Bravo', 'tel': 789}]
apelido = 'Jonny Bravo'
print(lAgenda)
for pessoa in lAgenda:
    if apelido in pessoa.values():
        # print(pessoa)
        # print(lAgenda.index(pessoa))
        #1a versao
        # posicao = lAgenda.index(pessoa)
        # lAgenda.pop(posicao)
        # #2a versao
        # lAgenda.pop(lAgenda.index(pessoa))
        #3a versao
        lAgenda.remove(pessoa)

print(lAgenda)

lista_compras = ['cafe', 'acucar', 'creme chantilly']
print(lista_compras)
print(lista_compras.index('acucar'))



# ▪ Sua Irmã é muito desorganizada, quando ela foi anotar os dados dos convidados ela anotou
# em listas separadas e voce tera que juntar. Crie tres jeitos diferentes de juntar# [nome,
# endereco, telephone, idade]# [Andre, Rua do Alfaiates 10, 9887342, 22]
lChaves = ['nome', 'endereco', 'telephone', 'idade']
lValores = ['Andre', 'Rua do Alfaiates 10', 9887342, 22]

#racional
# print(len(lChaves))
# pessoa = {lChaves[0]:lValores[0]}
# print(pessoa)

pessoa = {}
for i in range(len(lChaves)):
    pessoa[lChaves[i]]=lValores[i]
print(pessoa)

pessoazip = dict(zip(lChaves,lValores))
print(pessoazip)

# ▪ Para facilitar voce resolveu criar um dicionario cuja a chave é o nome da pessoa e no valor
# voce ira armazenar outro dicionario com todos os dados da pessoa.