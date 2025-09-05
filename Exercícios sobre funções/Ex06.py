"""
6.
Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. 
Teste com 3, 5 e 7 valores diferentes.
"""
#Verificar se args for zero pode dar erro
def media(*args):
    if len(args) == 0:
        return "Erro! Nem um numero foi informado!"
    return sum(args) / len(args)

print(media())
print(media(1,2,3))
print(media(1,2,3,4,5))
print(media(1,2,3,4,5,6,7))