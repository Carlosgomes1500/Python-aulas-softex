"""
Listas

"""
#lista = []
#print(type(lista))

frutas = ["linão", "banana", "morango", "coco"]
print(frutas)

###Adicionar elementos na lista
frutas.insert(2,"maca")
print(frutas)

frutas.append("kiwi")
print(frutas)

frutas_vermelhas = ["morango", "uva", "amora", "framboesa"]

frutas+=frutas_vermelhas
print(frutas)

###Remover elementos
#print("Removendo elementos")
#print(frutas.count("morango"))
#frutas.remove("morango")
#print(frutas)

#print("Primeiro Pop")
#frutas.pop()
#print(frutas)

#print("Segundo Pop")
#frutas.pop(4)
#print(frutas)

#del frutas[5]
#print(frutas)

#copia de lista
print("-----")
frutas2 = frutas[:]
frutas2.copy()
print(frutas)
print(id(frutas))
print(id(frutas2))