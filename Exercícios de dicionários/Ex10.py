"""
10
Ordenando dicionário por valor

Dado o dicionário:

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.
"""
pontuacoes = {
    "João": 50, 
    "Maria": 80, 
    "Pedro": 70
}

pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}

trup = list(pontuacoes.items())
n = len(trup)

for i in range(n):
    indice_do_maior = i

    for j in range(i + 1, n):
        if trup[j][1] > trup[indice_do_maior][1]:
            indice_do_maior = j

    trup[i], trup[indice_do_maior] = trup[indice_do_maior], trup[i]

print("Itens ordenados:")
for nome, pontuacao in trup:
    print(f"{nome}: {pontuacao}")