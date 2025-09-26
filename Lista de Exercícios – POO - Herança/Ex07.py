"""
7.
Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao.
Se a classe Administrador herda das duas, qual versão de status() será chamada?
Use Administrador.__mro__ para mostrar a ordem.
"""
class Autenticacao:
    def login(self):
        print("Usuário logado com sucesso.")

    def status(self):
        print("Status da Autenticação: OK")

class Permissao:
    def verificar_permissao(self):
        print("Permissões verificadas. Acesso concedido.")
    def status(self):
        print("Status da Permissao: OK")

class Administrador(Autenticacao, Permissao):
    ...

adm = Administrador()

#A versão que será chamada é a da primeira classe listada na declaração de herança.
#Neste caso vai ser a classe Autenticacao
adm.status()

#Ordem de Resolução de Métodos (__mro__)
print("Ordem de Resolução de Métodos (__mro__)")
print(Administrador.__mro__)

