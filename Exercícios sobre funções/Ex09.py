"""
Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros. 
A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:

 def soma(a, b): return a + b
 aplicar_operacao(3, 4, soma)
"""
def somar(num1, num2):
    return(num1+num2)

def subtrair(num1, num2):
    return(num1-num2)

def multiplicar(num1, num2):
    return(num1*num2)

def dividir(num1, num2):
    if num2 == 0:
        return "Erro! não se pode dividir por zero!"
    return(num1/num2)

operacoes_validas = {
    "somar": somar,
    "subtrair": subtrair,
    "multiplicar": multiplicar,
    "dividir": dividir
}

def aplicar_operacao(num1, num2, nome_operacao):
    operacao = operacoes_validas.get(nome_operacao)
    if operacao:
        return operacao(num1, num2)
    else:
        return f"Operação inválida: '{nome_operacao}'"

print(aplicar_operacao(20, 10, "somar")) 
print(aplicar_operacao(20, 10, "subtrair")) 
print(aplicar_operacao(20, 10, "multiplicar")) 
print(aplicar_operacao(20, 10, "dividir")) 
print(aplicar_operacao(20, 0, "dividir")) 
print(aplicar_operacao(20, 10, "sodgsfgr")) 