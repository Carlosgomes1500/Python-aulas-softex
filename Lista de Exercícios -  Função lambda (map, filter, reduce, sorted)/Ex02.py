"""
2
Filtrar pares (filter + lambda)

Dada a lista [10, 15, 20, 25, 30], use filter com lambda para obter apenas os números pares.
"""
lista = [10, 15, 20, 25, 30]
print(list(filter(lambda num: num % 2 == 0, lista)))