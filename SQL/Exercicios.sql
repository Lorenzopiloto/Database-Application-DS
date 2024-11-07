-- Escreva um bloco anonimoque recupere os titulos dos livros cujos códigos estejam entre 10 e 15.
-- Use %TYPE para declarar a variavel que vai receber o titulo do livro
-- SELECT BASE
SELECT cd_codigo, tx_titulo FROM T_BS_LIVRO WHERE cd_codigo BETWEEN 10 AND 15;

-- Jeito duro
/*
SET SERVEROUTPUT ON
DECLARE
--  V_tx_titulo VARCHAR(100);
    v_tx_titulo T_BS_LIVRO.tx_titulo%TYPE;
    
BEGIN
    FOR i IN 10..15
    LOOP
        SELECT tx_titulo
        INTO v_tx_titulo
        FROM T_BS_LIVRO WHERE cd_codigo = i;
        DBMS_OUTPUT.PUT_LINE(v_tx_titulo);
    END LOOP;
END;
/
*/

-- Jeito Fácil (Cursor -> Colecao interna que o Oracle faz)
BEGIN
    FOR linha IN (SELECT cd_codigo, tx_titulo
                  FROM T_BS_LIVRO WHERE cd_codigo BETWEEN 10 AND 15)
    LOOP
        DBMS_OUTPUT.PUT_LINE(linha.tx_titulo);
        -- não funciona pois estou recuperando os campos codigo e titulo de uma vez
        -- DBMS_OUTPUT.PUT_LINE(linha);
    END LOOP;
END;
/

-- 2 - Baseado no bloco anonimo anterior recupere agora todos os campos da tabela T_BS_LIVRO
-- Pesquise %ROWTYPE e use na declaração da sua variável
SET SERVEROUTPUT ON
DECLARE
--  v_tx_titulo VARCHAR(200);
--  v_cd_codigo T_BS_LIVRO.cd_codigo%TYPE;
--  v_tx_titulo T_BS_LIVRO.tx_titulo%TYPE;
    v_linha T_BS_LIVRO%ROWTYPE;
    
BEGIN
    FOR i IN 10..15
    LOOP
        SELECT *
        -- INTO v_cd_codigo, v_tx_titulo
        INTO v_linha
        FROM T_BS_LIVRO WHERE cd_codigo = i;
        DBMS_OUTPUT.PUT_LINE(v_linha.tx_titulo || ' - ' || NVL(v_linha.nr_ano_publicacao,0));
    END LOOP;
END;
/

UPDATE T_BS_LIVRO SET nr_ano_publicacao = TRUNC(DBMS_RANDOM.VALUE(1950, 2024));
COMMIT;
SELECT TRUNC(DBMS_RANDOM.VALUE(1950, 2024)) FROM DUAL;

-- 3 Observe o trecho abaixo e execute no Oracle. E explique o que aconteceu
-- O codigo da erro, pois o select retorna mais que ma linha e o INTO espera em uma unica linha para poder
-- atribuir a quantidade para a variavel de quantidade
DECLARE
    qtde  t_bs_livro_livraria.nr_quant%type;
BEGIN
    SELECT  SUM(nr_quant)
    INTO    qtde
    FROM    t_bs_livro_livraria
    --WHERE   cd_codigo = 18 AND cd_livraria = 1
    GROUP BY cd_livraria, cd_codigo;
    dbms_output.put_line('Qtde livros= ' || qtde);
END;

CREATE OR REPLACE VIEW vw_estoque_livraria AS
    SELECT  cd_codigo, cd_livraria, SUM(nr_quant) as qtde
    FROM    t_bs_livro_livraria
    GROUP BY cd_livraria, cd_codigo;
    
SELECT * FROM vw_estoque_livraria

CREATE OR REPLACE VIEW vw_estoque_livraria AS
    SELECT l.cd_codigo, l.tx_título, lv.cd_livraria, lv.nm_livraria, SUM(nr_quant) as qtde
    FROM   t_bs_livro_livraria 11
    INNER JOIN
            t_bs_livraria lv ON (11.cd_livraria = lv.cd_livraria)
    INNER JOIN
            t_bs_livro 1 ON (1.cd_codigo = 11.cd_codigo)
    GROUP BY 1.cd_codigo, 1.tx_titulo, lv.cd_livraria, lv.nm_livraria;
    
select * from vw_estoque_livraria
   

