--FUNCOES SAO PROCEDURES COM RETORNO
CREATE OR REPLACE FUNCTION fu_imprime_nome 
RETURN VARCHAR2
AS 
    v_nome VARCHAR2(20) := 'Julia';
BEGIN
    DBMS_OUTPUT.PUT_LINE(v_nome);
    RETURN 'Bom dia ' || v_nome;
END fu_imprime_nome;
/
SHOW ERRORS;

--O USO PRINCIPAL DE FUNCOES É PODER CHAMAR DENTRO DE UM SELECT
--COMO É FEITO NO EXEMPLO DO SUBSTRING
SELECT SUBSTR(tx_titulo, 1, 10) FROM T_BS_LIVRO;


-- PARA TESTAR/EXECUTAR A FUNCAO BASTA CHAMAR NUM SELECT
SELECT fu_imprime_nome FROM DUAL;
-- OU NO BLOCO ANONIMO
SET SERVEROUTPUT ON
DECLARE
    v_nome VARCHAR2(40);
BEGIN
    SELECT fu_imprime_nome INTO v_nome FROM DUAL;
    DBMS_OUTPUT.PUT_LINE(fu_imprime_nome);
    
END;

CREATE OR REPLACE FUNCTION fu_qtd_titulos RETURN INTEGER
AS
    v_qt T_BS_LIVRO_LIVRARIA.nr_quant%TYPE;
BEGIN
    SELECT COUNT(DISTINCT tx_titulo) 
    INTO v_qt
    FROM T_BS_LIVRO;
    
    RETURN v_qt;
END;
/
SELECT fu_qtd_titulos FROM DUAL;


CREATE OR REPLACE FUNCTION contar_nomes_unicos RETURN NUMBER AS
    v_contagem NUMBER;
BEGIN
    SELECT COUNT(DISTINCT TX_TITULO) INTO v_contagem
    FROM t_bs_livro;
    --DBMS_OUTPUT.PUT_LINE('Contagem de nomes únicos: ' || v_contagem);
    --RETURN 'Contagem de nomes únicos: ' || v_contagem;
    RETURN v_contagem;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Ocorreu um erro: ' || SQLERRM);
END contar_nomes_unicos;
/

SELECT contar_nomes_unicos FROM DUAL;



CREATE OR REPLACE FUNCTION contar_nomes_unicos_m RETURN VARCHAR2 AS
    v_contagem NUMBER;
BEGIN
    SELECT COUNT(DISTINCT TX_TITULO) INTO v_contagem
    FROM t_bs_livro;
    --DBMS_OUTPUT.PUT_LINE('Contagem de nomes únicos: ' || v_contagem);
    RETURN 'Contagem de nomes únicos: ' || v_contagem;
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Ocorreu um erro: ' || SQLERRM);
END contar_nomes_unicos_m;
/

SELECT contar_nomes_unicos_m as "M de Mensagem"
FROM DUAL;

BEGIN
    DBMS_OUTPUT.PUT_LINE(contar_nomes_unicos_m);
END;
/

SELECT TX_TITULO, contar_nomes_unicos FROM T_BS_LIVRO;


-- DADO NOME DE LIVRO E DE LIVRARIA FAZER UMA FUNCAO QUE RECUPERA A QUANTIDADE
SELECT 
    l.tx_titulo,
    lv.nm_livraria,
    ll.nr_quant
FROM
    T_BS_LIVRO l
    INNER JOIN
    T_BS_LIVRO_LIVRARIA ll
    ON (l.cd_codigo = ll.cd_codigo)
    INNER JOIN
    T_BS_LIVRARIA lv
    ON (ll.cd_livraria = lv.cd_livraria)
WHERE
    UPPER(l.tx_titulo) = 'A MENINA QUE ROUBAVA LIVROS'
    AND
    UPPER(lv.nm_livraria) like '%SARAIVA%';

CREATE OR REPLACE FUNCTION fu_recupera_estoque
(p_tx_titulo T_BS_LIVRO.tx_titulo%TYPE, p_nm_livraria T_BS_LIVRARIA.nm_livraria%TYPE)
RETURN NUMBER
IS
    v_nr_quant T_BS_LIVRO_LIVRARIA.nr_quant%TYPE := 0;
BEGIN
    SELECT 
        ll.nr_quant
    INTO
        v_nr_quant
    FROM
        T_BS_LIVRO l
        INNER JOIN
        T_BS_LIVRO_LIVRARIA ll
        ON (l.cd_codigo = ll.cd_codigo)
        INNER JOIN
        T_BS_LIVRARIA lv
        ON (ll.cd_livraria = lv.cd_livraria)
    WHERE
        UPPER(l.tx_titulo) = UPPER(p_tx_titulo)
        AND
        UPPER(lv.nm_livraria) like '%'||UPPER(p_nm_livraria)||'%';
    RETURN v_nr_quant;
END;
/

SELECT 
NM_LIVRARIA, fu_recupera_estoque('A MENINA QUE ROUBAVA LIVROS', NM_LIVRARIA) 
FROM T_BS_LIVRARIA;
