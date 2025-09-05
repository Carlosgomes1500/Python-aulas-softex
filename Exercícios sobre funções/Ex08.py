"""
8.
Crie uma função chamada calculadora que tenha dentro dela outras funções
 (somar, subtrair, multiplicar, dividir).
 A função principal deve permitir escolher a operação e retornar o resultado.
"""


def calculadora(num1, num2, operacao):
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
    
    match operacao:
        case "soma":
            return somar(num1, num2)
        case "subtracao":
            return subtrair(num1, num2)
        case "multiplicacao":
            return multiplicar(num1, num2)
        case "divisao":
            return dividir(num1, num2)
        case _:
            return "Operação inválida"

print(calculadora(8, 7, "soma")) 
print(calculadora(8, 7, "subtracao"))
print(calculadora(8, 7, "multiplicacao")) 
print(calculadora(14, 7, "divisao"))
print(calculadora(14, 0, "divisao"))
print(calculadora(14, 7, "fdgh"))
 