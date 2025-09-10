"""
1.
Escreva um programa que peça ao usuário para digitar um número. 
Trate o erro caso ele digite algo que não seja um número inteiro.
"""
try:
    num = input("Digite um numero inteiro:")
    num = int(num)
except ValueError:
     print(f"Erro!: '{num}' não é um número inteiro válido.")