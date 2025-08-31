"""
7.
Dado o dicionário:

d = {"a": 1, "b": 2, "c": 3}
Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.
"""
d = {
    "a": 1,
    "b": 2, 
    "c": 3
}

d_linha = {}

for chave, dados in d.items():
  d_linha[dados] = chave

print(d_linha)