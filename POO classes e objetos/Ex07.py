"""
07.
Crie uma classe Aluno com atributos nome e nota. 
Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno). 
Crie alguns objetos Aluno e adicione-os à turma.
"""
class Aluno:
    def __init__(self,nome, nota):
        self.nome = nome
        self.nota = nota

class Turma:
    def __init__(self):
        self.lista_de_alunos = []

    def adicionar_aluno(self ,aluno):
        self.lista_de_alunos.append(aluno)

aluno1 = Aluno("Andre", 7.4)
aluno2 = Aluno("Felipe", 7.8)
aluno3 = Aluno("Ana", 6.9)

turma = Turma()

turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)

for aluno in turma.lista_de_alunos:
    print(f"Nome: {aluno.nome}, Nota: {aluno.nota}")