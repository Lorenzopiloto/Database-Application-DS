# #Arquivos JSON se assemelham a objetos conhecidos do python: dicionario e lista

import json

print('JSON')
with open('alunos_idade.json', mode ='r', encoding='UTF-8') as arqAlunos:
    #o python lê o arquivo JSON como um texto comum
    #o metodo para ler texto é o READ
    print('\nLendo o arquivo JSON como texto')
    textoJsonAlunos = arqAlunos.read()
    print(textoJsonAlunos)
    print(type(textoJsonAlunos))
    print('\nTransformando o texto lido em objetos do python - colecoes')
    listaAlunos = json.loads(textoJsonAlunos)
    print(listaAlunos)

#Depois de transformar em colecoes, dai fica facil, é só usar o que já conhecemos
for dicionarioAluno in listaAlunos:
    print(dicionarioAluno)

# [
# {'nome': 'Patrícia', 'sobrenome': 'Angelini', 'idade': 50},
# {'nome': 'Ricardo', 'sobrenome': 'Jesus', 'idade': 25},
# {'nome': 'Manuel', 'sobrenome': 'Santos', 'idade': 44},
# {'nome': 'Gisela', 'sobrenome': 'Almeida', 'idade': 22},
# {'nome': 'Fábio', 'sobrenome': 'Santos', 'idade': 39},
# {'nome': 'Andréa', 'sobrenome': 'Tchuss', 'idade': 88},
# {'nome': 'Agnes', 'sobrenome': 'Virma', 'idade': 34},
# {'nome': 'Joelma', 'sobrenome': 'Parnaq', 'idade': 33},
# {'nome': 'Margarida Florida', 'sobrenome': 'Jardim', 'idade': 17},
# {'nome': 'Serafina', 'sobrenome': 'Fina', 'idade': 25},
# {'nome': 'Mané', 'sobrenome': 'José', 'idade': 20}
# ]
#suponha que eu queria pegar o sobrenome Almeida. Como fazer?
print(listaAlunos[3]['sobrenome'])
#resultado: Almeida
print(listaAlunos[3].values())
#resultado: dict_values(['Gisela', 'Almeida', 22])
print(listaAlunos[3])
#resultado: {'nome': 'Gisela', 'sobrenome': 'Almeida', 'idade': 22}
print(list(listaAlunos[3].values()))
#resultado: ['Gisela', 'Almeida', 22]

print('\nEscrevendo um arquivo JSON a partir de um dicionario')
dicAlunoJosue = {'nome':'Josue','sobrenome':'Pires','idade':19}
#vou usar a biblioteca do JSON para transformar o dicionario em um texto formatado/identado
textoJsonAlunoJosue = json.dumps(dicAlunoJosue, indent='\t')
print(textoJsonAlunoJosue)
print(type(textoJsonAlunoJosue))

#E se eu quiser gravar ?
with open('alunos_idade_josue.json', mode ='w', encoding='UTF-8') as arqAluno:
#Agora q temos o texto podemos usar uma funcao simples (nativa) do python para escrever
    arqAluno.write(textoJsonAlunoJosue)

print('\nGravando direto um arquivo JSON num unico passo')
dicAlunoOlavo = {'nome':'Olavo','sobrenome':'Lavo','idade':20}
with open('alunos_idade_olavo.json', mode ='w', encoding='UTF-8') as arqAluno:
    json.dump(dicAlunoOlavo, arqAluno, indent='\t', separators=(',',':'))


print('\nLer um arquivo JSON e acrescentar um item')
dicAlunoSerafina = {'nome':'Serafina','sobrenome':'Fina','idade':22}
#1 parte ler o arquivo e transformar em lista
with open('alunos_idade.json', mode ='r', encoding='UTF-8') as arqAlunos:
    textoJsonAlunos = arqAlunos.read()
    listaAlunos = json.loads(textoJsonAlunos)
    print(listaAlunos)
#2 parte fazer o append do dicionario do aluno
listaAlunos.append(dicAlunoSerafina)
#3 parte gravar por cima a lista completa dentro arquivo
with open('alunos_idade.json', mode ='w', encoding='UTF-8') as arqAlunos:
    json.dump(listaAlunos, arqAlunos, indent='\t', separators=(',', ':'))
