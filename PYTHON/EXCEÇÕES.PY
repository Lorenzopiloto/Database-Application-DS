#Exceções
#Qdo acontece um erro INESPERADO durante a EXECUÇAO do programa

# #programa base
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
valor = float(input('Entre com o valor gasto no supermercado: R$'))
qtd = int(input('Entre com a qtde de itens comprados: '))
media = valor / qtd
print(f'Em media gastou R${media} por item')
# #fim programa base

print('Tratamento de Exceção com bloco try/except')
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
try:
    valor = float(input('Entre com o valor gasto no supermercado: R$'))
    qtd = int(input('Entre com a qtde de itens comprados: '))
    media = valor / qtd
    print(f'Em media gastou R${media:.2f} por item')
except:
    print('Houve uma exceção')

print('Tratamento de Exceção com bloco try/except divisao zero')
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
continuada = True
while continuada:
    try:
        valor = float(input('Entre com o valor gasto no supermercado: R$'))
        qtd = int(input('Entre com a qtde de itens comprados: '))
        media = valor / qtd
        print(f'Em media gastou R${media:.2f} por item')
        continuada = False
    except ZeroDivisionError:
        print('Entre com a quantidade correta de itens')
    except ValueError:
        print('Entre somente com numeros')
    except:
        print('Houve uma exceção')

print('Tratamento de Exceção com bloco try/except divisao zero')
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
try:
    valor = float(input('Entre com o valor gasto no supermercado: R$'))
    qtd = int(input('Entre com a qtde de itens comprados: '))
    media = valor / qtd
    print(f'Em media gastou R${media:.2f} por item')
except ZeroDivisionError:
    print('Entre com a quantidade correta de itens')
except ValueError as v:
    print(f'Entre somente com numeros:{v}')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}-{e}')

print('Tratamento de Exceção com bloco try/except finally')
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
try:
    valor = float(input('Entre com o valor gasto no supermercado: R$'))
    qtd = int(input('Entre com a qtde de itens comprados: '))
    media = valor / qtd
except ZeroDivisionError:
    print('Entre com a quantidade correta de itens')
except ValueError as v:
    print(f'Entre somente com numeros:{v}')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}-{e}')
else:
    #esse bloco é executado somente se nao houve qq erro
    print(f'Em media gastou R${media:.2f} por item')
finally:
    #usamos o bloco finally qdo queremos executar o codigo independente de erro
    #ex: abro conexao com banco
    #processo alguns arquivos e acontece um erro
    #o bloco finally servira para fechar a conexao com o banco
    print('Fim do programa')

print('Tratamento de Exceção e Lancamento de excecao ESPECIALIZADA')
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
class NumeroNegativo(Exception):
    pass

try:
    valor = float(input('Entre com o valor gasto no supermercado: R$'))
    qtd = int(input('Entre com a qtde de itens comprados: '))
    #vou testar se é negativo e vou provocar uma excecao
    if valor < 0 or qtd < 0:
        raise NumeroNegativo('Voce entrou com numeros negativos')
    media = valor / qtd
    print(f'Em media gastou R${media:.2f} por item')
except ZeroDivisionError:
    print('Entre com a quantidade correta de itens')
except ValueError as v:
    print(f'Entre somente com numeros:{v}')
except NumeroNegativo as n:
    print(f'{n.__class__.__name__}-{n}')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}-{e}')
finally:
    #usamos o bloco finally qdo queremos executar o codigo independente de erro
    #ex: abro conexao com banco
    #processo alguns arquivos e acontece um erro
    #o bloco finally servira para fechar a conexao com o banco
    print('Fim do programa')

print('Tratamento de Exceção e Lancamento de excecao GENERICA')
titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
try:
    valor = float(input('Entre com o valor gasto no supermercado: R$'))
    qtd = int(input('Entre com a qtde de itens comprados: '))
    #vou testar se é negativo e vou provocar uma excecao
    if valor < 0 or qtd < 0:
        raise Exception('Voce entrou com numeros negativos')
    media = valor / qtd
    print(f'Em media gastou R${media:.2f} por item')
except ZeroDivisionError:
    print('Entre com a quantidade correta de itens')
except ValueError as v:
    print(f'Entre somente com numeros:{v}')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}-{e}')
finally:
    print('Fim do programa')



titulo = 'Calculo da media de gastos no supermercado'
print(f'{titulo:^50}')
while True:
    try:
        valor = float(input('Entre com o valor gasto no supermercado: R$'))
        qtd = int(input('Entre com a qtde de itens comprados: '))
        #vou testar se é negativo e vou provocar uma excecao
        if valor < 0 or qtd < 0:
            raise Exception('Voce entrou com numeros negativos')
        media = valor / qtd
        print(f'Em media gastou R${media:.2f} por item')
        break
    except ZeroDivisionError:
        print('Entre com a quantidade correta de itens')
    except ValueError as v:
        print(f'Entre somente com numeros:{v}')
    except Exception as e:
        print(f'Houve uma exceção:{e.__class__.__name__}-{e}')
    finally:
        print('Fim do programa')


#Tiago
try:
    n1 = float(input('Insira o primeiro número para a comparação: '))
    n2 = float(input('Insira o segundo número para a comparação: '))
    if n1 > n2:
        print(f'{n1} é maior que {n2}')
    elif n2 > n1:
        print(f'{n2} é maior que {n1}')
    elif n1 == n2:
        raise Exception(f' Os números {n1} e {n2} são iguais')
except ValueError as v:
    print(f'Insira somente números.\nPara decimais, use ".".\nErro: {v}')
except Exception as e:
    print(f'Houve uma exceção:{e.__class__.__name__}-{e}')

#Maria Clara
class NumerosIguais(Exception):
    pass

while True:
    try:
        a = float(input('Escreva o primeiro número: '))
        b = float(input('Escreva o segundo número: '))
        if a == b:
            raise NumerosIguais('Os dois numeros são iguais')
        if a > b:
            print(a)
        elif b > a:
            print(b)

    except NumerosIguais as n:
        break
    except Exception as e:
        print('Houve uma excecao', e)

class OutAlfa(Exception):
    pass

while True:
    try:
        letra = str(input('Digite uma letra de A a D')).lower()
        restricao = ['a', 'b', 'c', 'd', 'e']
        palavras={'a':'abacaxi','b':'banana','c': 'carambola', 'd':'damasco'}
        if letra in restricao:
            abc=palavras[letra]
            print(abc)
        else:
            raise OutAlfa('Você escolheu uma letra fora da regra')
    except OutAlfa:
        print('Você escolheu uma letra que não está entre A e D')
        break
    except Exception as e:
        print(f'Houve uma exceção: {e.__class__.__name__} - {e}')


#
class OutAlfa(Exception):
    pass

while True:
    try:
        letra = str(input('Digite uma letra de A a D')).lower()
        palavras={'a':'abacaxi','b':'banana','c': 'carambola', 'd':'damasco'}
        if letra in palavras:
        #if letra in palavras.keys():
            abc=palavras[letra]
            print(abc)
        else:
            raise OutAlfa('Você escolheu uma letra fora da regra')
    except OutAlfa:
        print('Você escolheu uma letra que não está entre A e D')
        break
    except Exception as e:
        print(f'Houve uma exceção: {e.__class__.__name__} - {e}')


# #Matheus
print('Abecedário das frutas!')
while True:
    try:
        letra = input('Digite uma letra entre A, B, C, D: ').lower()
        frutas = {'a':'Abacaxi', 'b':'Banana', 'c':'Carambola', 'd':'Damasco'}
        if not letra in frutas:
            raise Exception('Digite uma letra válida.')
        print(f'Uma fruta que começa com a letra "{letra.upper()}" é {frutas[letra]}!')
        break
    except Exception as e:
        print(f'{e}')

#Maria Clara
while True:
    try:
        salarioMin = 1412.00  # Corrigido para um número float
        salario = float(input('Digite seu salário: '))

        variavel = salario / salarioMin

        print(round(variavel, 2), 'salários mínimos')
        break
    except ValueError:
        print('Entre com numeros!')
    except Exception as e:
        print(f'Houve uma exceção: {e.__class__.__name__} - {e}')


#Funcoes
#sao usadas para organizar e reaproveitar
#Procedures - funcoes sem retorno

def OlaMundo():
    print('Ola Mundo')

OlaMundo()

def Soma2():
    total = 1 + 2
    print(total)

#imprimir dentro de uma funcao NAO É UMA BOA PRATICA, a nao ser que a funcao seja funcao de relatorio
Soma2()

def Soma2par(p1, p2):
    total = p1 + p2
    print(total)

#posicional
Soma2par(2, 4)
#nomeado
Soma2par(p2=6, p1=7)

def Soma2parRet(p1, p2):
    total = p1 + p2
    return total
print(Soma2parRet(6,9))

#parametro default
def Soma2parRetD(p1, p2=0):
    total = p1 + p2
    return total
print(Soma2parRetD(8))
print(Soma2parRetD(8, 7))

#SO POSSO TER PARAMETROS SEM DEFAULT NO INICIO.
# A PARTIR DO MOMENTO Q EU DEFINI UM DEFAULT, TUDO DEPOIS TEM QUE TER DEFAULT
# def Soma2parRetD(p1=99, p2):
#     total = p1 + p2
#     return total

#qdo eu quiser somar numeros independente de qtos numeros eu tenho
#crio uma colecao do tipo tupla
def SomaVarios(*p):
    #print(type(p))
    soma=0
    for elemento in p:
        soma += elemento
    return soma
print(SomaVarios(1))
print(SomaVarios(1, 8, 2, 45, 244))

## parametros variaveis do tipo chave / valor
def fApresentacao (**nomes):
    print(type(nomes))
    print(f'Ola amigo {nomes['primeiro']}')
    print(f'Ola amigo {nomes['segundo']}')

fApresentacao(primeiro='Gustavo', segundo='Maciel')

#Matheus
def ValorAbsoluto(n):
    return abs(n)

try:
    n=float(input('Entre com um numero: '))
    print(ValorAbsoluto(n))
except Exception as e:
    print(e)