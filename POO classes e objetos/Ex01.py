"""
01.
Crie uma classe chamada Pessoa que tenha os atributos nome e idade.
Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.
"""
class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Pedro", 21)

print(pessoa1.nome, pessoa1.idade, sep="\n")
print(pessoa2.nome, pessoa2.idade, sep="\n")
