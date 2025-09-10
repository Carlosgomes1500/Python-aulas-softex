"""
8.
Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Use:

try para a conversão,
else para verificar se é par ou ímpar,
finally para exibir "Fim do programa".
"""
try:
    num = input("Digite um numero:")
    num = int(num)
except ValueError:
    print(f"Erro!: '{num}' não é um número inteiro válido.")
else:
    if num%2 == 0:
        print("Numero Par")
    else:
        print("Numero Impar")
finally:
    print("fim do programa")
