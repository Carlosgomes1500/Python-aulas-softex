"""
5.
Crie uma classe Funcionario que herda de Usuario e, 
em seguida, crie uma classe Gerente que herda de Funcionario. 
Mostre como instanciar um gerente e acessar seus atributos.
"""
class Usuario:
    def __init__(self,nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome do clinete:{self.nome} email:{self.email}")
    
    def saudacao(self):
        print("Olá, usuário")

class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Salário: {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, departamento):
        super().__init__(nome, email, salario)
        self.departamento = departamento

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Departamento: {self.departamento}")

#instanciar um gerente 
gerente = Gerente("Maria", "maria@gmail.com", 500, "Engenharia")
gerente.exibir_informacoes()
gerente.saudacao()

#Acessar seus atributos
print(gerente.nome)
print(gerente.email)
print(gerente.salario)
print(gerente.departamento)
