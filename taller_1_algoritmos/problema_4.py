from enum import Enum

class Gramaje(Enum):
    MUYPESADO = 40
    PESADO = 30
    NORMAL = 20
    LIVIANO = 10

def obtener_costo(peso):
    if peso >= 4.0:
        return Gramaje.MUYPESADO.value, Gramaje(40).name
    elif peso >= 2.5 and peso < 4.0:
        return Gramaje.PESADO.value, Gramaje(30).name
    elif peso >= 1.0 and peso < 2.5:
        return Gramaje.NORMAL.value, Gramaje(20).name
    else:
        return Gramaje.LIVIANO.value, Gramaje(10).name


peso = float(input("Ingrese el peso del paquete: "))
if peso <= 0:
    print("El peso del paquete no puede ser menor o igual a 0")
else:
    costo, gramaje = obtener_costo(peso)
    print(f"El costo del envio es de {costo}, debido a que el paquete es de gramaje {gramaje}")