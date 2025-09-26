"""
4
Na classe Cliente, adicione o atributo saldo. 
Adicione um método construtor em Cliente 
que inicialize também os atributos de Usuario usando super().
"""
class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome do clinete:{self.nome} email:{self.email}")
    
    def saudacao(self):
        print("Olá, usuário")



class Cliente(Usuario):
    def __init__(self,nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo
    
    def exibir_informacoes(self):
        print(f"Nome do clinete:{self.nome} email:{self.email}")

    def saudacao(self):
        print("Olá, cliente")

usuario1 = Usuario("usuario","ana@gmail.com")

cliente1 = Cliente("Pedro","pedro@yahoo.com", "100")
