"""
05.
Crie uma classe ContaBancaria com os atributos titular e saldo. 
Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor)
que diminui o saldo (se houver saldo suficiente).
Teste com depósitos e saques
"""
class ContaBancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if(valor > self.saldo):
            print("Erro! Saldo insuficiente para saque!")
        else:
           self.saldo -= valor 


conta1 = ContaBancaria("Carlos", 50)

conta1.depositar(20)

conta1.sacar(30)

conta1.sacar(50)

print(conta1.saldo)
