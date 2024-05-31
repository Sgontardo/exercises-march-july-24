# Hacer una función que lea el archivo nombres_apellidos.txt y lo coloque en un array de estructuras con los campos nombre y apellido por sepàrado. Guardar estos nombre y apellidos en un archivo binario usando pickle. Luego una función final que lea el archivo binario y muestre los nombres y apellidos en pantalla.

import pickle

def leer():
    archivo = open("nombres_apellidos.txt", "rb")
    nombres = []
    for linea in archivo:
        nombre, apellido = linea.strip().split(" ")
        nombres.append({nombre, apellido})
    return nombres

def guardar(nombres):
    archivo = open("nombres_apellidos.bin", "wb")
    pickle.dump(nombres, archivo)

def mostrar():
    archivo = open("nombres_apellidos.bin", "rb")
    nombres = pickle.load(archivo)
    for nombre in nombres:
        print(nombre["nombre"], nombre["apellido"])