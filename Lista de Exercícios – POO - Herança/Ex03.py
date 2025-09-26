"""
3
Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário". 
Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente". 
Mostre como funciona a chamada.
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
    def saudacao(self):
        print("Olá, cliente")

usuario1 = Usuario("usuario","ana@gmail.com")

cliente1 = Cliente("Pedro","pedro@yahoo.com")


usuario1.saudacao()

#O metodo saudacao e sobreescrito na classe filha
print("O metodo saudacao e sobreescrito na classe filha")

cliente1.saudacao()

