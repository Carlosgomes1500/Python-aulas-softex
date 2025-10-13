"""
4

Forçando contrato

Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
O que acontece quando você tenta instanciá-la? Corrija o código.
"""
from abc import ABC, abstractmethod

class Repositorio(ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass
    @abstractmethod
    def buscar(self, id):
        pass

class RepositorioMemoria(Repositorio):
    def salvar(self, objeto):
        print(f"Salvando o objeto {objeto} na memória...")

#repositorio = RepositorioMemoria()
#repositorio.salvar("objeto1")
#Erro!
#TypeError: Can't instantiate abstract class RepositorioMemoria with abstract method buscar
#O erro ocorre porque a classe RepositorioMemoria não implementa todos os métodos da interface Repositorio.
#Para corrigir, precisamos implementar o método buscar() na classe Carro.

    def buscar(self, id):
       print(f"Buscando o objeto com id {id} na memória...")

repositorio = RepositorioMemoria()
repositorio.salvar("objeto1")
repositorio.buscar(1)