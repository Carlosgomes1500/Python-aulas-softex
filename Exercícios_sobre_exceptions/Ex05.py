"""
5.
Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. 
Caso contrário, retorne o resultado da divisão.

"""
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError ("Erro! Não é possivel dividir por zero!")
    else:
        return a / b

res1 = dividir(10, 2)
print(res1)

res2 = dividir(7, 0)
print(res2)