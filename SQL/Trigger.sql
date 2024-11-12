--Trigger
--DROP TRIGGER trt;
CREATE OR REPLACE TRIGGER tr_bef_ins_livro_titulo 
BEFORE INSERT OR UPDATE ON T_BS_LIVRO FOR EACH ROW
DECLARE
BEGIN
--    :NEW.TX_TITULO := UPPER(:NEW.TX_TITULO);
    :NEW.TX_TITULO := 'A TURMA 1TSCPG É A MAIS ANIMADA';

END tr_bef_ins_livro_titulo;
/
/*
INSERT INTO t_bs_livro (
    cd_codigo, tx_titulo, nr_numero_paginas, nr_ano_publicacao, nr_edicao, cd_codigo_autor
) VALUES (
    81, 'HalloWeen', 200, null, null, 1
);


ALTER TRIGGER TRT DISABLE;

INSERT INTO t_bs_livro (
    cd_codigo, tx_titulo, nr_numero_paginas, nr_ano_publicacao, nr_edicao, cd_codigo_autor
) VALUES (
    84, 'DDPEWRT', 200, null, null, 1
);

INSERT INTO t_bs_livro (
    cd_codigo, tx_titulo, nr_numero_paginas, nr_ano_publicacao, nr_edicao, cd_codigo_autor
) VALUES (
    88, 'NOVO INSERT', 200, null, null, 1
);

INSERT INTO t_bs_livro (
    cd_codigo, tx_titulo, nr_numero_paginas, nr_ano_publicacao, nr_edicao, cd_codigo_autor
) VALUES (
    89, 'NOVO INSERT DI NOVO', 200, null, null, 1
);
*/

--SELECT EXTRACT(YEAR FROM SYSDATE) FROM DUAL;
CREATE OR REPLACE TRIGGER TR_BEF_UPD_LIVRO_ANO_PUBL 
BEFORE UPDATE OF NR_ANO_PUBLICACAO ON T_BS_LIVRO FOR EACH ROW
DECLARE
BEGIN
    IF :NEW.NR_ANO_PUBLICACAO > EXTRACT (YEAR FROM SYSDATE) THEN
        --DBMS_OUTPUT.put_line('aNO INVALIDO');
        RAISE_APPLICATION_ERROR(-20000, 'Ano de publicacao invalido');
    END IF;
END;
/

SET SERVEROUTPUT ON;
UPDATE T_BS_LIVRO
SET NR_ANO_PUBLICACAO = 2088
WHERE CD_CODIGO = 88;
/
CREATE OR REPLACE TRIGGER tr_bef_del_livro_cd 
BEFORE DELETE ON T_BS_LIVRO FOR EACH ROW
DECLARE
BEGIN
    IF :OLD.cd_codigo = 10 THEN
        RAISE_APPLICATION_ERROR(-20000,'NAO É PERMITIDO EXCLUIR O LIVRO 10');
    END IF;
END;
/

DELETE FROM T_BS_LIVRO WHERE cd_codigo = 10;

DROP TABLE T_LOG_ESTOQUE;
CREATE TABLE T_LOG_ESTOQUE
(ID_ESTOQUE INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, 
CD_LIVRARIA NUMBER(10),
CD_LIVRO NUMBER(10),
DT_MOVIMENTO DATE,
QT_ESTOQUE_ANTERIOR INTEGER,
QT_ESTOQUE_ATUAL INTEGER
);
/

CREATE OR REPLACE TRIGGER tr_aft_upd_livro_livraria_qt
AFTER UPDATE ON T_BS_LIVRO_LIVRARIA
FOR EACH ROW
DECLARE
BEGIN
    IF :OLD.NR_QUANT <> :NEW.NR_QUANT THEN
        INSERT INTO T_LOG_ESTOQUE 
        (cd_livraria, cd_livro, dt_movimento, qt_estoque_anterior, qt_estoque_atual)
        VALUES
        (:OLD.CD_LIVRARIA, :OLD.CD_CODIGO, SYSDATE,:OLD.NR_QUANT, :NEW.NR_QUANT);
    END IF;
END;
/

SELECT * FROM T_LOG_ESTOQUE;
UPDATE T_BS_LIVRO_LIVRARIA SET NR_QUANT = NR_QUANT - 1 WHERE CD_CODIGO = 18 AND CD_LIVRARIA = 3;

--o objetivo agora nao é examinar linha a linha da tabela, mas ver que operacoes estao ocorrendo na tabela
--é uma trigger no nivel de tabela
CREATE OR REPLACE TRIGGER tr_bef_insupdel_t_bs_autor
BEFORE INSERT OR DELETE OR UPDATE OF nm_autor, cd_codigo ON T_BS_AUTOR
BEGIN
    CASE
        WHEN INSERTING THEN 
            DBMS_OUTPUT.PUT_LINE('OCORRENDO UM INSERT NA TABELA DE AUTOR');
        WHEN DELETING THEN
            DBMS_OUTPUT.PUT_LINE('OCORRENDO UM DELETE NA TABELA DE AUTOR');
        WHEN UPDATING('nm_autor') THEN
            DBMS_OUTPUT.PUT_LINE('OCORRENDO UM UPDATE NO NOME DO AUTOR NA TABELA DE AUTOR');        
        WHEN UPDATING('cd_codigo') THEN -- este é um exemplo ficticio pois nao é legal fazer update em pk
            DBMS_OUTPUT.PUT_LINE('OCORRENDO UM UPDATE NO CODIGO DO AUTOR NA TABELA DE AUTOR');        

    END CASE;
END;
/

SET SERVEROUTPUT ON
INSERT INTO T_BS_AUTOR (cd_codigo, nm_autor) VALUES (16, 'Dan Brown');
DELETE T_BS_AUTOR WHERE cd_codigo = 15;
UPDATE T_BS_AUTOR SET nm_autor = UPPER(nm_autor) WHERE cd_codigo = 16;





