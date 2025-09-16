"""
06.
Modifique a classe ContaBancaria para que o método sacar retorne True 
se a operação for bem-sucedida e False caso contrário.
Teste o retorno e imprima mensagens adequadas.
"""
class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print("Deposito realizado com sucesso!")
    
    def sacar(self, valor):
        if(valor > self.saldo):
            print("Erro! Saldo insuficiente para saque!")
            return False 
        else:
           self.saldo -= valor
           print("Saque realizado com sucesso!")
           return True


conta1 = ContaBancaria("Carlos", 50)

conta1.depositar(20)

if conta1.sacar(30):
    print(f"Operação realizada! Novo saldo: R${conta1.saldo}")
else:
    print("Operação não realizada!")

if conta1.sacar(50):
    print(f"Operação realizada! Novo saldo: R${conta1.saldo}")
else:
    print("Operação não realizada!")

print(conta1.saldo)