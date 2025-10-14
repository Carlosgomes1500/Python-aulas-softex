"""
5.
Crie a classe Carro que possui um Motor. 
O Motor deve ser criado dentro do Carro.
Se o Carro deixar de existir, o Motor também deixa. 
Mostre isso criando e depois apagando o objeto.
"""
import weakref

class Motor:
    def __init__(self, potencia:int):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligado.")

    def __del__(self):
        print(f"Motor de {self.potencia} cavalos foi destruído.")


class Carro:
    def __init__(self, modelo: str, potencia_motor: int):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def ligar_carro(self):
        print(f"Ligando o carro {self.modelo}...")
        self.motor.ligar()
    
    def __del__(self):
        print(f"O carro '{self.modelo}' foi destruído.")

carro1= Carro("Gol", 150)
carro2 =Carro("Ferrari", 800)

motor1_ref = weakref.ref(carro1.motor)
motor2_ref = weakref.ref(carro2.motor)

print(f"Após deletar, o motor do Gol ainda existe? {'Sim' if motor1_ref() is not None else 'Não'}")
print(f"Após deletar, o motor da Ferrari ainda existe? {'Sim' if motor2_ref() is not None else 'Não'}")

carro1.ligar_carro()
carro2.ligar_carro()

del carro1
del carro2

print(f"Após deletar, o motor do Gol ainda existe? {'Sim' if motor1_ref() is not None else 'Não'}")
print(f"Após deletar, o motor da Ferrari ainda existe? {'Sim' if motor2_ref() is not None else 'Não'}")
