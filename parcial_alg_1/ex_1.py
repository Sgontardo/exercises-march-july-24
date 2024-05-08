# Crear una función con recursividad que pida nombre de usuario, correo y fecha de nacimiento
# Validar que el nombre tenga al menos dos palabras, el correo en formato válido y la fecha de nacimiento en formato dd/mm/aaaa
# Usar expresiones regulares

import re

nombre = input("Ingrese su nombre: ")
correo = input("Ingrese su correo: ")
fecha = input("Ingrese su fecha de nacimiento: ")

def validar_nombre(nombre):
    if re.match(r"^[a-zA-Z]+\s[a-zA-Z]+$", nombre):
        return True
    else:
        return False