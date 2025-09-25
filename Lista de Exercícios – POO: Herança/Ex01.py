"""
1.
Crie uma classe Usuario com atributos nome e email.
Depois, crie uma classe Cliente que herde de Usuario.
Crie uma instancia de um cliente e acesse todos os atributos.
"""

class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email



class Cliente(Usuario):
    ...


cliente1 = Cliente("Pedro","pedro@yahoo.com")


print(f"Nome do clinete:{cliente1.nome} email:{cliente1.email}")