"""
2.

Proibição de instanciamento

Tente instanciar diretamente a classe Animal da questão anterior e explique o erro gerado pelo Python.
"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
#animal = Animal() #Erro! 
#Erro: TypeError: Can't instantiate abstract class Animal with abstract methods falar
#Este erro acontece pois a classe Animal é uma abstrata 
#que possui um método abstrato falar() que ainda não foi implementado. 
#Classes abstratas não podem ser instanciadas diretamente.
#Para que possamos usar a classe Animal, é necessário criar uma classe concreta que implemente o método falar().

class cachorro(Animal):
    def falar(self):
        print("Au Au")

class gato(Animal):
    def falar(self):
        print("miau")
cachorro1 = cachorro()
gato1 = gato()
cachorro1.falar()
gato1.falar()