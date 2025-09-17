"""
09.
Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" 
e atributos de instância nome e idade. 
Mostre a diferença entre acessar especie pelo objeto e pela classe.
"""
class Cachorro:

    especie = "Canis familiaris"

    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade

cachorro1 = Cachorro("toto",9)
cachorro2 = Cachorro("doginho", 11)

#Acessando o atributo especie diretamente pela classe 
print(f"Especie da classe:{Cachorro.especie}")

#Acessando o atributo especie pelos objetos
print(f"Especie de {cachorro1.nome}:{cachorro1.especie}")
print(f"Especie de {cachorro2.nome}:{cachorro2.especie}")

#podesse perceber que todos os objetos hedam o atributo especie
#Se eu altera especie diretamente na classe, acabarei alterando em todos os objetos

Cachorro.especie = "pinscher"

print(f"apos as alterações")
print(f"Especie da classe:{Cachorro.especie}")
print(f"Especie de {cachorro1.nome}:{cachorro1.especie}")
print(f"Especie de {cachorro2.nome}:{cachorro2.especie}")

#mudando diretamente na classe muda em todos os objetos

