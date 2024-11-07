/*
1. Escreva um Procedure PR_RECUPERALIVROS que recupere odos os livros da tabela TB_S_LIVROS
e exiba na tela. Trate a exceção se nã houver dados na tabela
*/

-- Habilitar o Server Output para exibir os dados na tela

SET SERVEROUTPUT ON;
 
-- Criar a procedure para exibir os livros da tabela T_BS_LIVRO

CREATE OR REPLACE PROCEDURE PR_RECUPERALIVROS AS

    -- Variáveis para armazenar os dados dos livros

    CURSOR c_livros IS

        SELECT cd_codigo, tx_titulo, nr_numero_paginas, nr_ano_publicacao, nr_edicao, cd_codigo_autor

        FROM T_BS_LIVRO;
 
    v_cd_codigo        T_BS_LIVRO.cd_codigo%TYPE;

    v_tx_titulo        T_BS_LIVRO.tx_titulo%TYPE;

    v_nr_numero_paginas T_BS_LIVRO.nr_numero_paginas%TYPE;

    v_nr_ano_publicacao T_BS_LIVRO.nr_ano_publicacao%TYPE;

    v_nr_edicao        T_BS_LIVRO.nr_edicao%TYPE;

    v_cd_codigo_autor  T_BS_LIVRO.cd_codigo_autor%TYPE;
 
BEGIN

    -- Abrir o cursor e buscar os dados

    OPEN c_livros;

    LOOP

        FETCH c_livros INTO v_cd_codigo, v_tx_titulo, v_nr_numero_paginas, v_nr_ano_publicacao, v_nr_edicao, v_cd_codigo_autor;

        EXIT WHEN c_livros%NOTFOUND;
 
        -- Exibir cada registro no console

        DBMS_OUTPUT.PUT_LINE('Código: ' || v_cd_codigo || 

                             ', Título: ' || v_tx_titulo || 

                             ', Páginas: ' || COALESCE(TO_CHAR(v_nr_numero_paginas), 'N/A') || 

                             ', Ano: ' || COALESCE(TO_CHAR(v_nr_ano_publicacao), 'N/A') || 

                             ', Edição: ' || COALESCE(TO_CHAR(v_nr_edicao), 'N/A') || 

                             ', Código Autor: ' || COALESCE(TO_CHAR(v_cd_codigo_autor), 'N/A'));

    END LOOP;

    CLOSE c_livros;
 
    -- Caso a tabela não tenha registros, levantar uma exceção

    IF c_livros%ROWCOUNT = 0 THEN

        DBMS_OUTPUT.PUT_LINE('Nenhum registro encontrado na tabela T_BS_LIVRO.');

    END IF;
 
EXCEPTION

    -- Tratamento de exceção caso ocorra algum erro

    WHEN NO_DATA_FOUND THEN

        DBMS_OUTPUT.PUT_LINE('Nenhum dado encontrado na tabela T_BS_LIVRO.');

    WHEN OTHERS THEN

        DBMS_OUTPUT.PUT_LINE('Ocorreu um erro ao recuperar os dados.');

END PR_RECUPERALIVROS;

/
 
-- Executar a procedure para exibir os livros

EXEC PR_RECUPERALIVROS;

/

/*
2. Escreva uma função que retorne o nome da livraria da tabela T_BS_LIVRARIA
quando for passado o nome exato do bairro;
*/
 
 SET SERVEROUTPUT ON 

-- Criar a função para retornar o nome da livraria pelo nome exato do bairro

CREATE OR REPLACE FUNCTION FN_RECUPERAR_NOME_LIVRARIA(p_bairro IN VARCHAR2)

    RETURN VARCHAR2

IS

    v_nm_livraria T_BS_LIVRARIA.nm_livraria%TYPE;

BEGIN

    -- Buscar o nome da livraria com base no nome exato do bairro

    SELECT nm_livraria

    INTO v_nm_livraria

    FROM T_BS_LIVRARIA

    WHERE tx_bairro = p_bairro

    AND ROWNUM = 1;  -- Garantir que só um resultado será retornado, caso haja duplicidade de bairros

    -- Retornar o nome da livraria

    RETURN v_nm_livraria;
 
EXCEPTION

    -- Caso o bairro não seja encontrado

    WHEN NO_DATA_FOUND THEN

        RETURN 'Nenhuma livraria encontrada para o bairro informado';

    WHEN OTHERS THEN

        RETURN 'Ocorreu um erro ao buscar a livraria';

END FN_RECUPERAR_NOME_LIVRARIA;
 
/
 
 
-- Exemplo de uso da função para recuperar o nome da livraria pelo bairro "Centro"

SELECT FN_RECUPERAR_NOME_LIVRARIA('Paraiso') AS nome_livraria

FROM dual;
 
-- papai, trouxe pãozinho

 