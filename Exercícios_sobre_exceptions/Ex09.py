"""
9.


Crie uma função sacar(saldo, valor) que:

Lance (raise) uma exceção personalizada SaldoInsuficienteError se o valor for maior que o saldo.
Caso contrário, retorne o novo saldo. Teste a função dentro de um try-except e exiba uma mensagem apropriada ao usuário.
"""
class SaldoInsuficienteError(Exception): ...

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente!")
    else:
     return saldo-valor

try:
    saldo = 2
    valor = 3
    saldo = sacar(saldo,valor)
    print(f"novo saldo:{saldo}")
except SaldoInsuficienteError:
    print("Saldo insuficiente!")