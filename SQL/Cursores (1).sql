-- Ativar saída para o console
SET SERVEROUTPUT ON;

-- ABORDAGEM SEM CURSOR PARA UM ÚNICO TÍTULO
DECLARE
    v_cod NUMBER;
    v_titulo VARCHAR2(200);
BEGIN
    SELECT cd_codigo, tx_titulo
    INTO v_cod, v_titulo
    FROM T_BS_LIVRO WHERE cd_codigo = 3;
    DBMS_OUTPUT.PUT_LINE(v_cod || '-' || v_titulo);
END;
/

-- ABORDAGEM SEM CURSOR PARA TODOS OS TÍTULOS
DECLARE
    v_cod T_BS_LIVRO.cd_codigo%TYPE;
    v_titulo T_BS_LIVRO.tx_titulo%TYPE;
BEGIN
    FOR i IN 1..18 LOOP
        BEGIN
            SELECT cd_codigo, tx_titulo
            INTO v_cod, v_titulo
            FROM T_BS_LIVRO WHERE cd_codigo = i;
            DBMS_OUTPUT.PUT_LINE(v_cod || '-' || v_titulo);
        EXCEPTION
            WHEN NO_DATA_FOUND THEN
                NULL; -- Ignorar caso não encontre um registro com o código
        END;
    END LOOP;
END;
/

-- ABORDAGEM COM CURSOR PARA TODOS OS TÍTULOS
DECLARE
    v_cod T_BS_LIVRO.cd_codigo%TYPE;
    v_titulo T_BS_LIVRO.tx_titulo%TYPE;

    CURSOR c_livro IS
        SELECT cd_codigo, tx_titulo FROM T_BS_LIVRO;
BEGIN
    OPEN c_livro;
    LOOP
        FETCH c_livro INTO v_cod, v_titulo;
        EXIT WHEN c_livro%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_cod || '-' || v_titulo);
    END LOOP;
    CLOSE c_livro;
END;
/

-- CURSOR COM JOIN ENTRE T_BS_LIVRO E T_BS_AUTOR
DECLARE
    CURSOR c_tit_autor IS
    SELECT
        UPPER(l.tx_titulo) AS tx_titulo,
        l.nr_numero_paginas,
        a.nm_autor
    FROM 
        T_BS_LIVRO l
        INNER JOIN
        T_BS_AUTOR a
        ON (a.cd_codigo = l.cd_codigo_autor);
    
    v_titulo T_BS_LIVRO.tx_titulo%TYPE;
    v_pag T_BS_LIVRO.nr_numero_paginas%TYPE;
    v_autor T_BS_AUTOR.nm_autor%TYPE;

BEGIN
    OPEN c_tit_autor;
    LOOP
        FETCH c_tit_autor INTO v_titulo, v_pag, v_autor;
        EXIT WHEN c_tit_autor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_titulo || '-' || v_pag || '-' || v_autor);
    END LOOP;
    CLOSE c_tit_autor;
END;
/

-- USO DE ROWTYPE PARA SIMPLIFICAR A DECLARAÇÃO DE VARIÁVEIS
DECLARE
    CURSOR c_tit_autor IS
    SELECT
        UPPER(l.tx_titulo) AS tx_titulo,
        l.nr_numero_paginas,
        a.nm_autor
    FROM 
        T_BS_LIVRO l
        INNER JOIN
        T_BS_AUTOR a
        ON (a.cd_codigo = l.cd_codigo_autor);
    
    ltit_autor c_tit_autor%ROWTYPE;

BEGIN
    OPEN c_tit_autor;
    LOOP
        FETCH c_tit_autor INTO ltit_autor;
        EXIT WHEN c_tit_autor%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(ltit_autor.tx_titulo || '-' || ltit_autor.nr_numero_paginas || '-' || ltit_autor.nm_autor);
    END LOOP;
    CLOSE c_tit_autor;
END;
/

-- ABORDAGEM SIMPLIFICADA COM CURSOR IMPLÍCITO PARA TODOS OS TÍTULOS
DECLARE
BEGIN
    FOR linha IN
    (
        SELECT
            UPPER(l.tx_titulo) AS tx_titulo,
            l.nr_numero_paginas,
            a.nm_autor
        FROM 
            T_BS_LIVRO l
            INNER JOIN T_BS_AUTOR a
            ON (a.cd_codigo = l.cd_codigo_autor)
    ) LOOP
        DBMS_OUTPUT.PUT_LINE(linha.tx_titulo || '-' || linha.nr_numero_paginas || '-' || linha.nm_autor);
    END LOOP;
END;
/
