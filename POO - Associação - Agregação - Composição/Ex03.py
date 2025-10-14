"""
3.
Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
Departamento deve agregar funcionários já criados.
"""
class Funcionario:
    def __init__(self, nome: str):
        self.nome = nome

class Departamento :
    def __init__(self, nome: str):
        self.nome = nome
        self.Funcionario = []

    def adicionar_funcionario(self, Funcionario: Funcionario):
        self.Funcionario.append(Funcionario)

    def listar_funcionario(self):
        for Funcionario in self.Funcionario:
            print(f"Funcionario: {Funcionario.nome} do departamento de {self.nome}")


funcionario1 = Funcionario("Ana")
funcionario2 = Funcionario("Bia")

departamento1  = Departamento ("Compras")
departamento1.adicionar_funcionario(funcionario1)
departamento1.adicionar_funcionario(funcionario2)

departamento1.listar_funcionario()
