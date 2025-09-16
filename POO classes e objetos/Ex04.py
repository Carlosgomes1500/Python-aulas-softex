"""
04.
Usando a classe Carro, crie um objeto e depois altere o valor de um de seus atributos 
(por exemplo, mudar o ano). Imprima antes e depois da alteração.
"""
class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def inforacoes(self):
        print(f"Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}")

carro1 = Carro("Toyota", "Corolla", 2023)

carro1.inforacoes()

carro1.ano = 2021

carro1.inforacoes()