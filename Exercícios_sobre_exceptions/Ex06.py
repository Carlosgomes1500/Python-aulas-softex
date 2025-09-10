"""
6.
Crie uma exceção personalizada chamada IdadeInvalidaError. 
Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.
"""
class IdadeInvalidaError(Exception): ...

def cadastrar_idade(idade):
    if idade <= 0:
        raise IdadeInvalidaError("Idade tem que ser maior que Zero")
    else:
        print(f"A idade da pessoa é {idade}")

try:
    idade = 10
    cadastrar_idade(idade)
except IdadeInvalidaError:
    print("Erro! Ao cadastra a idade!")

try:
    idade = -2
    cadastrar_idade(idade)
except IdadeInvalidaError:
    print("Erro! Ao cadastra a idade!")