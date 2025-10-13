"""
4.
Herança parcial
Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). 
Depois, crie uma subclasse Carro que implemente apenas o método mover()
O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.
"""
from abc import ABC, abstractmethod
class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        print("O carro está se movendo")

# carro1 = Carro() #Erro!
# Erro: TypeError: Can't instantiate abstract class Carro with abstract methods parar
# O erro ocorre porque a classe Carro não implementa todos os métodos abstratos da classe Transporte.
# Para corrigir, precisamos implementar o método parar() na classe Carro.

    def parar(self):
        print("O carro parou")

carro1 = Carro()
carro1.mover()
carro1.parar() 