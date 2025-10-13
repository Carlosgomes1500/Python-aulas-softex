"""
1

Definição de classe abstrata

Crie uma classe abstrata chamada Animal que possua um método abstrato falar(). 
Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. 
Mostre o uso criando objetos e chamando o método falar().
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
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
