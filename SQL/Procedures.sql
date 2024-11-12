--procedures sao objetos do banco de dados que executam um algoritmo
--reutilizaveis

-- 1a parte CRIAR A PROCEDURE
DECLARE
    v_nome VARCHAR2(20) := 'Julia';
BEGIN
    DBMS_OUTPUT.PUT_LINE(v_nome);
END;
/
--DROP PROCEDURE pr_imprime_nome;
CREATE OR REPLACE PROCEDURE pr_imprime_nome AS 
    v_nome VARCHAR2(20) := 'Julia';
BEGIN
    DBMS_OUTPUT.PUT_LINE(v_nome);
END;
/
ALTER PROCEDURE PR_IMPRIME_NOME COMPILE;
ALTER PROCEDURE P_REC_LIVROS COMPILE;


-- 2a parte VERIFICAR SE TEM ERROS
SHOW ERRORS;
--
DESC USER_ERRORS;
SELECT LINE, SUBSTR(TEXT, 1, 40) TEXTO FROM USER_ERRORS WHERE NAME = 'PR_IMPRIME_NOME';



-- 3a parte EXECUTAR/USAR A PROCEDURE
-- jeito simples
EXEC pr_imprime_nome;
-- mais complexto
BEGIN
    pr_imprime_nome;
END;
/

CREATE OR REPLACE PROCEDURE pr_imprime_nome (p_nome VARCHAR2) AS 
BEGIN
    DBMS_OUTPUT.PUT_LINE(p_nome);
END;
/
EXEC pr_imprime_nome('Renata');

--MODELANDO O CRESCIMENTO POPULACIONAL DE COELHOS
--SABEMOS QUE O CRESCIMENTO NATURAL ANUAL É DE UMA TAXA DE 50%
--FACA UMA PROCEDURE COM PARAMETRO DE UMA POPULACAO INICIAL, E ESTIME EM QUANTOS ANOS
--A POPULACAO ATINGE 1000 COELHOS
--IMPRIMA O RESULTADO

--DICAS VERIFICA SE A POPULACAO INICIAL NAO É MAIOR QUE 1000, SENAO LANCA EXCEÇÃO
--USA UM LOOP PARA IR SOMANDO OS ANOS (WHILE)

SET SERVEROUTPUT ON;
/*
DECLARE
    v_populacao_inicial NUMBER := 100;
    v_limite NUMBER := 1000;
    v_pop NUMBER;
    v_taxa NUMBER := 0.5;
    v_anos NUMBER := 0;
    ex_populacao EXCEPTION;
BEGIN
    IF v_populacao_inicial > v_limite THEN
        RAISE ex_populacao;
    END IF;
    v_pop := v_populacao_inicial;
    WHILE v_pop < v_limite LOOP
        v_pop := v_pop + (v_pop * v_taxa);
        v_anos := v_anos + 1;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE ('Dada a  populacao inicial de ' || v_populacao_inicial 
    || ' individuos, levara ' || v_anos || ' anos para a populacao ultrapassar ' || v_limite || ' individuos');
EXCEPTION
    WHEN ex_populacao THEN
        DBMS_OUTPUT.PUT_LINE('Populacao inicial maior que limite');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(sqlerrm);
END;
*/
CREATE OR REPLACE PROCEDURE pr_calcula_crescimento_pop 
(p_pop_ini IN NUMBER DEFAULT 100, p_limite IN NUMBER DEFAULT 1000, 
p_taxa IN NUMBER DEFAULT 0.5)
AS
    v_populacao_inicial NUMBER := p_pop_ini;
    v_limite NUMBER := p_limite;
    v_pop NUMBER;
    v_taxa NUMBER := p_taxa;
    v_anos NUMBER := 0;
    ex_populacao EXCEPTION;
BEGIN
    IF v_populacao_inicial > v_limite THEN
        RAISE ex_populacao;
    END IF;
    v_pop := v_populacao_inicial;
    WHILE v_pop < v_limite LOOP
        v_pop := v_pop + (v_pop * v_taxa);
        v_anos := v_anos + 1;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE ('Dada a  populacao inicial de ' || v_populacao_inicial 
    || ' individuos, levara ' || v_anos || ' anos para a populacao ultrapassar ' || v_limite || ' individuos');
EXCEPTION
    WHEN ex_populacao THEN
        DBMS_OUTPUT.PUT_LINE('Populacao inicial maior que limite');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(sqlerrm);
END;

SHOW ERRORS;


EXECUTE PR_CALCULA_CRESCIMENTO_POP(300, 600, 0.2);
























