"""
08.
Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe,
apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.
"""
class Aluno:
    def __init__(self,nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Nome: {self.nome}, Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.lista_de_alunos = []

    def adicionar_aluno(self ,aluno):
        self.lista_de_alunos.append(aluno)

aluno1 = Aluno("Andre", 7.4)
aluno2 = Aluno("Felipe", 7.8)
aluno3 = Aluno("Ana", 6.9)
aluno4 = Aluno("Maria", 9.5)

turma = Turma()

turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)
turma.adicionar_aluno(aluno4)

print(aluno1)
print(aluno2)
print(aluno3)
print(aluno4)
    
