#5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado"

livros =["Power Skills", "Midset", "rápido devagar"]

if "Duna" in livros:
    livros.remove("Duna")
else:
    print("Livro não encontrado")

print(livros)