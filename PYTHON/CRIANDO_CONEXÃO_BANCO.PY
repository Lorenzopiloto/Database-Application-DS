import oracledb


#CRIANDO A CONEXAO COM BANCO
#NAO ERREM A SENHA  - 3 X ERRADA ELA BLOQUEIA

try:
    conn = oracledb.connect(user='xxxx', password='teste',dsn='oracle.fiap.com.br:1521/orcl')
except Exception as e:
    print('Erro:', e)
    conexao, continua = False, False
else:
    conexao, continua = True, True

if conexao:
    while continua:
        print("""Escolha uma das opções
        1-Consulta da Tabela
        2-Inserir na Tabela
        3-Carga de Arquivo 
        4-Carga de Arquivo com Pandas
        5-Sair
        """)
        escolha=int(input("Escolha uma opção: "))

        if escolha == 1:
            c_consulta = conn.cursor()
            comando = f'SELECT * FROM T_PY_ALUNO'
            c_consulta.execute(comando)
            lAlunos = c_consulta.fetchall()
            print(lAlunos)
        elif escolha == 2:
            #exercicio
            #Fazer uma rotina q pergunte nome, idade, endereco, curso e inserir na tabela
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            endereco = input('Endereco: ')
            curso = input('Curso: ')
            comando=(f"INSERT INTO T_PY_ALUNO (nome, idade, endereco, curso) VALUES "\
                     f"('{nome}',{idade},'{endereco}','{curso}')")
            print(comando)
            c_insert = conn.cursor()
            c_insert.execute(comando)
            conn.commit()
        elif 5:
            conn.close()
            continua = False

