"""
1
Crie as classes Pessoa e Livro 
e demonstre uma relação de associação entre eles.
"""
class Livro:
    def __init__(self, titulo: str, autores: str, paginas: int):
        self.titulo = titulo
        self.autores = autores
        self.paginas = paginas

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def ler_livro(self, Livro: Livro):
        print(f"{self.nome}, esta lendo o livro {Livro.titulo} do/s autor/es {Livro.autores}")

pessoa1 = Pessoa("Carlos", 29)
livro1 = Livro("O Senhor dos Anéis", "J. R. R. Tolkien" ,1211)

pessoa1.ler_livro(livro1)