"""
03.
Crie uma classe Carro com os atributos marca,  e ano. 
Use o método __init__ para inicializar esses valores.
Crie três objetos e mostre suas informações.modelo
"""
class Carro:
    def __init__(self,marca, modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def inforacoes(self):
        print(f"Marca:{self.marca}, Modelo:{self.modelo}, Ano:{self.ano}")

carro1 = Carro("Volkswagen", "Polo", 2025)
carro2 = Carro("Hyundai ", "HB20", 2024)
carro3 = Carro("Toyota", "Corolla", 2023)

carro1.inforacoes()
carro2.inforacoes()
carro3.inforacoes()

