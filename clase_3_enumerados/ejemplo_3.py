from enum import Enum

class Semaforo(Enum):
    ROJO, AMARILLO, VERDE = range(1,4)

print(list(Semaforo))
print()

def maneja_semaforo(luz):
    match luz:
        case Semaforo.ROJO:
            print(f"Luz {Semaforo.ROJO.name}. Debe detenerse!!")
        case Semaforo.AMARILLO:
            print(f"Luz {Semaforo.AMARILLO.name}. La luz cambiará a rojo pronto, sea cuidadoso!!")
        case Semaforo.VERDE:
            print(f"Luz {Semaforo.VERDE.name}. Puede continuar!!")

maneja_semaforo(Semaforo.VERDE)
maneja_semaforo(Semaforo.AMARILLO)
maneja_semaforo(Semaforo.ROJO)