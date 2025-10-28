/*
7
Liste o ano das turmas 
e a quantidade de turmas por ano.
*/
SELECT ano, COUNT() AS quantidade_de_turmas
FROM Turma
GROUP BY ano;
