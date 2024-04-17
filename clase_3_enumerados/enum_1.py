from enum import Enum

class Dia(Enum):
    LUNES     = "lunes"
    MARTES    = "martes"
    MIERCOLES = "miercoles"
    JUEVES    = "jueves"
    VIERNES   = "viernes"
    SABADO    = "sábado"
    DOMINGO   = "domingo"

print(Dia.MARTES)
print()

print(Dia.MARTES.name)
print()

print(Dia.MARTES.value)
print()

print(type(Dia.MARTES))
print()

print(list(Dia))