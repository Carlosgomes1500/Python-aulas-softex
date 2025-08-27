#10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
#notas = [[7, 8, 9], [6, 5, 7]]. No fim, imprima a média de cada aluno.

notas = []

for i in range(0,2):
    notas_aluno = []
    print(f"Digite a nota do {i + 1}° aluno")
    for j in range(3):
        nota = input(f"digite a { j +1 }° nota do aluno: ")
        notas_aluno.append(int(nota))
    notas.append(notas_aluno)

print("Lista de notas completa:", notas)

media_aluno01 = sum(notas[0]) / len(notas[0])

media_aluno02 = sum(notas[1]) / len(notas[1])

print("Media do 1° aluno", media_aluno01)
print("Media do 2° aluno", media_aluno02)