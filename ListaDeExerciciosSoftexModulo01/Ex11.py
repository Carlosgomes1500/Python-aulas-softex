"""
11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois adicione todas as peças do jogo na posição inicial. Para melhorar a visualização do tabuleiro, identifique as posições do tabuleiro da seguinte forma:

    [ ] - para posições vazias
    tor - para a torre
    cav - para o cavalo
    bis - para o bispo
    rai - para a rainha
    rei - para o rei
    pea - para o peão

Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. (Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)
"""
import numpy as np

pecas_principais = ['tor', 'cav', 'bis', 'rai', 'rei', 'bis', 'cav', 'tor']
peoes = ['pea'] * 8

tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

for coluna, peao in enumerate(peoes):
    tabuleiro[1][coluna] = peao
    tabuleiro[-2][coluna] = peao

for coluna, pecas_principais in enumerate(pecas_principais):
    tabuleiro[0][coluna] = pecas_principais
    tabuleiro[-1][coluna] = pecas_principais

tabuleiro_np = np.array(tabuleiro)
print(tabuleiro_np)