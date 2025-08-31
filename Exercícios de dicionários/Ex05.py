"""
5.
Verificando existência de uma chave

Verifique se a chave "telefone" existe no dicionário:

contato = {"nome": "Ana", "email": "ana@email.com"}

"""
contato = {
    "nome": "Ana", 
    "email": "ana@email.com"
    }

if "telefone" in contato:
  print("A chave 'telefone' existe em contato")
else:
  print("A chave 'telefone' não existe contato")