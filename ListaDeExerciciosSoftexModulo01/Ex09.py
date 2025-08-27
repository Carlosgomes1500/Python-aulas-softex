#9-Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores

valores = [10, 20, 30, 40]

soma = 0

for valores in valores:
    soma += int(valores)

print(soma)