"""
1.
Na classe, ContaBancaria, converta saldo para uma atributo privado. 
Crie um método setter e um getter para acessar e modificar essa atributo,
seguindo uma regra lógica (Ex: saldo não pode ser negativo)
"""
class ContaBancaria:
    def __init__(self,titular, num_conta, saldo=0):
        self.titular = titular
        self.num_conta = num_conta
        self.__saldo = 0
        self.set_saldo(saldo)

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor < 0:
            print("Erro! Saldo tem que ser maior que 0!")
        else:
            self.__saldo = valor

conta1 = ContaBancaria("Ana","1357-9", 100)

print(f"Conta de {conta1.titular} criada com saldo de R$ {conta1.get_saldo()}")

#Teste de Falha
conta1.set_saldo(-50)

# Verificação se o saldo não deve ter mudado
print(f"Saldo após a tentativa inválida: R$ {conta1.get_saldo()}")


#Teste de Sucesso
conta1.set_saldo(500)

# Verificação se o saldo foi atualizado
print(f"Saldo após a atribuição válida: R$ {conta1.get_saldo()}")


#Teste de Borda
conta1.set_saldo(0)

# Verificação se saldo for zero
print(f"Saldo após a atribuição de zero: R$ {conta1.get_saldo()}")


