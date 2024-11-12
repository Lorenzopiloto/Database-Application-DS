--EXCEÇOES É O ERRO Q OCORRE NO MOMENTO DA EXECUCAO
--Tratamento de exceções
--Lançamento de exceçÕES

-- A AREA DE EXCEPTION PERMITE TRATAR AS EXCEÇÕES
/*
SET SERVEROUTPUT ON
UNDEFINE valor;
UNDEFINE qtd;
ACCEPT valor PROMPT 'Entre com o valor da compra';
ACCEPT qtd PROMPT 'Entre com a quantidade de itens';
DECLARE
    valor NUMBER :=&valor;
    qtd NUMBER :=&qtd;
    ticket_medio NUMBER;
    QTD_VL_INVALIDA EXCEPTION;
BEGIN
    IF valor < 0 OR qtd < 0 THEN
        RAISE QTD_VL_INVALIDA;
    END IF;
        
    ticket_medio := valor/qtd;
    DBMS_OUTPUT.PUT_LINE('O valor do ticket medio é R$' || round(ticket_medio, 2));
    DBMS_OUTPUT.PUT_LINE(CONCAT('O valor do ticket medio é R$', round(ticket_medio, 2)));
    
EXCEPTION
    WHEN ZERO_DIVIDE THEN
        DBMS_OUTPUT.PUT_LINE('Entre com o valor maior que zero');
    WHEN QTD_VL_INVALIDA THEN
        DBMS_OUTPUT.PUT_LINE('Entre com o valor ou a quantidade maiores que zero');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Houve uma exceção - '|| sqlerrm );
END;
*/
-- exercicio
-- peca uma cor para o usuario e se ela for diferente de verde ou vermelho lance uma excecao
ACCEPT cor PROMPT 'Entre com uma cor';
DECLARE
    cor VARCHAR2(10) := UPPER('&cor'); 
    COR_ERRADA EXCEPTION;
BEGIN
    --IF cor <> 'VERDE' OR cor <> 'VERMELHO' THEN
    IF cor NOT IN ('VERDE', 'VERMELHO') THEN
        RAISE COR_ERRADA;
    END IF;
    DBMS_OUTPUT.PUT_LINE(cor);
EXCEPTION
    WHEN COR_ERRADA THEN
        DBMS_OUTPUT.PUT_LINE('COR INVALIDA');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE(sqlerrm);
END;














