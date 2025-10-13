"""
1.
Criando uma interface

Crie uma interface chamada Pagamento com um método abstrato processar(valor). 
Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface. 
Mostre como chamar processar() para cada uma.
"""
from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass
class CartaoCredito(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de {valor} com cartão de crédito.")

class Boleto(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de {valor} no boleto")

cartaocredito1 = CartaoCredito()
boleto1= Boleto()

cartaocredito1.processar(10)
boleto1.processar(50)