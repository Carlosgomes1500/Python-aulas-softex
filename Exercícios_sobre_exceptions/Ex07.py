"""
7.
Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro:

ValueError se o usuário digitar algo inválido

ZeroDivisionError se tentar dividir por zero
"""

try:
    num1 = input("Digite um numero:")
    num2 = input("Digite outro numero:")

    num1 = float(num1)
    num2 = float(num2)

    div = num1/num2

    print(div)
except ValueError:
    print("Erro! Um dos valores digitados não é um número válido.")

except ZeroDivisionError:
    print("Erro! O segundo valor precisa ser diferente de Zero")
