"""
4.
Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir).
Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.
"""
arquivo = None

try:
    arquivo = open('dados.txt', 'w')
    print("Arquivo 'dados.txt' foi aberto")
    
    arquivo.write("Escrevendo no arquivo...")
    print("Escrevendo no arquivo...")

finally:
    arquivo.write("\nFim da escrita no arquivo")
    print("Fim da escrita no arquivo")
    
    print("Encerrando programa")
