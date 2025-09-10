"""
3.
Crie um programa que peça ao usuário um número inteiro.
Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.
"""
try:
    num = input("Digite um numero inteiro:")
    num = int(num)
except ValueError:
     print(f"Erro!: '{num}' não é um número inteiro válido.")
else:
    print("sucesso!")