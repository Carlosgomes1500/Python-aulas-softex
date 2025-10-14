"""
2.
Crie as classes Aluno e Onibus.
Crie um método em Aluno que use a classe Onibus.
"""
class Onibus:
    def __init__(self, linha: str, capacidade: int):
        self.linha = linha
        self.capacidade = capacidade
        self.passageiros = []

    def adicionar_aluno(self, aluno):
        if len(self.passageiros) < self.capacidade:
            self.passageiros.append(aluno)
            print(f"O Aluno {aluno.nome} embarcou no ônibus {self.linha}.")
            return True
        else:
            print(f"Ônibus lotado! O Aluno {aluno.nome} não conseguiu embarcar no onibus.")
            return False

    def listar_alunos(self):
        print(f"Passageiros no ônibus {self.linha}")
        if not self.passageiros:
            print("Nenhum passageiro a bordo do onibus")
        else:
            for aluno in self.passageiros:
                print(f"Aluno: {aluno.nome}")


class Aluno:
    def __init__(self, nome: str):
        self.nome = nome
    
    def pegar_onibus(self, onibus: Onibus):
        print(f"O aluno {self.nome} está tentando pegar o ônibus da linha {onibus.linha}...")
        onibus.adicionar_aluno(self)


onibus_circular = Onibus("Circular", 2)
aluno1 = Aluno("Ana")
aluno2 = Aluno("Bia")
aluno3 = Aluno("Carlos")

aluno1.pegar_onibus(onibus_circular)
aluno2.pegar_onibus(onibus_circular)

onibus_circular.listar_alunos()

aluno3.pegar_onibus(onibus_circular)

onibus_circular.listar_alunos()