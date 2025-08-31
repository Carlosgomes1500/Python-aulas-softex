"""
6.
Contando frequência de palavras

Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
"""
def cont(palavras):
    conta = {}
    for palavra in palavras:
        if palavra in conta:
            conta[palavra] += 1
        else:
            conta[palavra] = 1
    return conta

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
res = cont(palavras)
print(res)