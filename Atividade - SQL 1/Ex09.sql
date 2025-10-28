/*
9.
Mostre o ano 
e a quantidade de turmas apenas para os anos que têm mais de 2 turmas. (Use GROUP BY e HAVING)
*/
SELECT ano, COUNT() AS quantidade_de_turmas
FROM Turma
GROUP BY ano
HAVING quantidade_de_turmas > 2;