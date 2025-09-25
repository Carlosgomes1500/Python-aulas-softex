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
    
pessoa1 = Pessoa("João", "01/01/1990", 12345678900, 1234567)

print(f"Pessoa criada: {pessoa1.nome}")
print(f"CPF inicial: {pessoa1.get_cpf()}")
print(f"Identidade inicial: {pessoa1.get_identidade()}")


#Teste de Falha CPF
pessoa1.set_cpf(-321)
print(f"CPF após a tentativa inválida:: {pessoa1.get_cpf()}")

#Teste de Sucesso CPF
pessoa1.set_cpf(98765432100)
print(f"CPF após a atribuição válida: {pessoa1.get_cpf()}")

#Teste de Falha Identidade
pessoa1.set_identidade(-999)
print(f"Identidade após a tentativa inválida: {pessoa1.get_identidade()}")

#Teste de Sucesso Identidade
pessoa1.set_identidade(7654321)
print(f"Identidade após alteração válida: {pessoa1.get_identidade()}")