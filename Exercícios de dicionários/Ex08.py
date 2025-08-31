"""
8.
Dicionário com listas

Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. 
Depois, imprima a média de cada aluno.
"""
alunos = {
    "Paulo": [8.3, 7.4, 8.0],
    "Bia": [7.5, 6.8, 9.1],
    "Pedro": [5.4, 6.9, 7.7],
    "Antonio": [6.1, 5.4, 8.3]
}
for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"A media do aluno {aluno} foi: {media:.2f}")