"""
9.
Mesclando dois dicionários

Escreva uma função que recebe dois dicionários 
e retorna um novo dicionário contendo todos os pares chave-valor. 
Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
"""
d1 = {
    "a": 1, 
    "b": 2, 
    "c": 3
}

d2 = {
    "b": 4, 
    "c": 5, 
    "d": 6
}

d12 = d1 | d2

print(d12)