"""
6.
Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.).
Cada Comodo deve ser criado dentro da Casa.    
"""
class Comodo:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return f"Cômodo: {self.nome}"
    
class Casa:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self._comodos = []

    def adicionar_comodo(self, nome_do_comodo: str):
        novo_comodo = Comodo(nome_do_comodo)
        self._comodos.append(novo_comodo)
        print(f"O cômodo '{nome_do_comodo}' foi adicionado à casa no endereço '{self.endereco}'.")

    def listar_comodos(self):
        if not self._comodos:
            print(f"A casa no endereço '{self.endereco}' ainda não possui cômodos.")
            return
        print(f"Cômodos da casa no endereço: {self.endereco}")
        for comodo in self._comodos:
            print(f"- {comodo.nome}")

casa1 = Casa("Recife, 123")

casa1.listar_comodos()

print("\nAdicionando cômodos...")
casa1.adicionar_comodo("Sala")
casa1.adicionar_comodo("Cozinha")
casa1.adicionar_comodo("Quarto")
casa1.adicionar_comodo("Banheiro")
casa1.adicionar_comodo("Escritório")

casa1.listar_comodos()