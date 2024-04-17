from enum import Enum

class Dia(Enum):
    LUNES     = 1
    MARTES    = 2
    MIERCOLES = 3
    JUEVES    = 4
    VIERNES   = 5
    SABADO    = 6
    DOMINGO   = 7


# Por valor:
print(f"El miembro del enum con valor 2 es: {Dia(2).name}")

# Por naombre:
print(f"El miembro del enum con nombre MARTES es: {Dia['MARTES'].value}")