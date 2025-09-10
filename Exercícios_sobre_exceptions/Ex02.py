"""
2.
Peça ao usuário dois números e tente multiplicá-los. 
Se o usuário digitar algo inválido, exiba uma mensagem de erro.
"""
try:

    num1 = input("Digite um numero:")
    num2 = input("Digite outro numero:")

    num1 = float(num1)
    
    resut = num1*num2

    print(resut)
except ValueError:
    print("Erro! A primeira variavel precissa ser um numero!")
except TypeError:
    print("Erro! A segunda variavel precissa ser um numero!")

