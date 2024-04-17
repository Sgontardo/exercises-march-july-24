# generar una enum con los diás de la semana usando un range

from enum import Enum

class Estaciones(Enum):
    INVIERNO, PRIMAVERA, VERANO, OTOGNO = range(1, 5)

print(list(Estaciones))

