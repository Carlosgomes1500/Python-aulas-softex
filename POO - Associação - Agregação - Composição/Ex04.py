"""
4.
Crie as classes Time e Jogador. 
Um Jogador tem nome e posição como atributos, 
enquanto Time agrega jogadores em uma lista.
"""
class Jogador:
    def __init__(self, nome: str, posição: str):
        self.nome = nome
        self.posição = posição

class Time :
    def __init__(self, nome: str):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, Jogador: Jogador):
        self.jogadores.append(Jogador)

    def listar_jogadores(self):
        for Jogador in self.jogadores:
            print(f"Jogador: {Jogador.nome} na posição {Jogador.posição} do time {self.nome}")


jogador1 = Jogador("Pedro", "Arremessador")
jogador2 = Jogador("João", "Receptor")

time1  = Time ("Oakland Athletics")
time1.adicionar_jogador(jogador1)
time1.adicionar_jogador(jogador2)

time1.listar_jogadores()
