"""
2.
Crie uma classe, Pessoa, que tenha os atributos: 
nome, data de nascimento, cpf, identidade.
Deixe os atributos cpf e identidade como privado 
e monte os métodos setters e getters para acessar e editar os valores
"""
class Pessoa:
     def __init__(self, nome, data_de_nascimento, cpf, identidade):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.__cpf = cpf
        self.__identidade = identidade

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, new_cpf):
        if new_cpf < 0:
            print("Erro! Novo CPF menor que 0!")
        else:
            self.__cpf = new_cpf
    
    def get_identidade(self):
        return self.__identidade

    def set_identidade(self, new_identidade):
        if new_identidade < 0:
            print("Erro! Nova identidade menor que 0!")
        else:
            self.__identidade = new_identidade