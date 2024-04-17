from enum import Enum

class Dia(Enum):
    LUNES     = "lunes"
    MARTES    = "martes"
    MIERCOLES = "miercoles"
    JUEVES    = "jueves"
    VIERNES   = "viernes"
    SABADO    = "sábado"
    DOMINGO   = "domingo"

for dia in Dia:
    print(dia.value, " - ", dia)