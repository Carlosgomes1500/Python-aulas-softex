"""
2.

Interface múltipla

Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). Crie uma classe Computador que implemente ambas. Mostre seu uso.
"""
from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def ligar(self):
        pass
class Desligavel(ABC):
    @abstractmethod
    def desligar(self):
        pass   
class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("Computador ligado")
    def desligar(self):
        print("Computador desligado")
pc1 = Computador()
pc1.ligar()
pc1.desligar()

