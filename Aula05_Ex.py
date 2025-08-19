#1) Crie uma lista que contenha diferentes tipos de dados (string, inteiro, outra lista…)

lista = ["morango", 1, 'A']
print(lista)

#2) Usando a lista criada na questão anterior, use o método insert ou append para adicionar mais dois elementos a lista e use remove, pop ou del para remover um elemento da lista.

lista.insert(4,"maca")
print(lista)

lista.insert(4,123)
print(lista)

lista.remove(123)
print(lista)

"""
3) Faça uma cópia da lista da questão anterior. Use a função id para verificar se
realmente criou uma lista nova (obs: mesmo valor de ID indica que é o mesma lista
e não uma nova)
"""
lista2 = lista[:]
lista2.copy()
print(lista)
print(id(lista))
print(id(lista2))

"""
4) Crie uma nova lista só com números (inteiro e/ou ponto flutuante) e multiplique os
elementos da lista por 5. O resultado deve ser uma nova lista com os elementos
multiplicados.

"""

lista_nova = [1, 2.1, 7, 10.5]
lista_res = []

for i in lista_nova:
    lista_res.append(i*5)
print(lista_res)

"""
5) Use o slice para criar uma nova lista que inclua apenas os elementos com índice
3 e 4 da lista a seguir:
[ 1,2,3,4,5,6 ]
Resultado esperado: [4,5]
"""
lista_tres = []
for i in range(1,7):
    lista_tres.append(i)

lista_corta = lista_tres[3:5]

print(lista_corta)