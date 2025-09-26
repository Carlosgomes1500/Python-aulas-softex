"""
6
Crie uma classe Autenticacao com um método login(). 
Crie outra classe Permissao com um método verificar_permissao(). 
Em seguida, crie uma classe Administrador que herda de ambas.
Como usar os métodos herdados?
"""
class Autenticacao:
    def login(self):
        print("Usuário logado com sucesso.")

class Permissao:
    def verificar_permissao(self):
        print("Permissões verificadas. Acesso concedido.")

class Administrador(Autenticacao, Permissao):
    ...

adm = Administrador()

#Os metodos herdados podem ser usados diretamente pela classe administrador
adm.login()
adm.verificar_permissao()