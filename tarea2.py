import numpy as np
from random import randint
from enum import Enum

## 1) Complejidad algoritmo sumatoria(n) = O(n) (Lineal)

## 2) Complejidad algoritmo search_target(array, target) = O(n) (Lineal)

## 3) Complejidad algoritmo duplicar_elementos(array) = O(n) (Lineal)

## 4) Complejidad algoritmo ordenacion(array) = O(n^2) (Cuadrática)

## 5) Complejidad algoritmo permutaciones(lista) = O(n!) (Factorial)

## 6) Complejidad algoritmo suma de n números = O(n) (Lineal)

## 7) Cree una función recursiva llamada cuenta_regresiva(n), la cual debe imprimir los números desde el n ingresado hasta cero.

def cuenta_regresiva(n):
    if n == 0:
        print(n)
    else:
        print(n)
        cuenta_regresiva(n-1)

n = 5
resultado = cuenta_regresiva(n)
print(resultado)

## 8) Cree una función recursiva llamada suma_digitos(numero), la cual debe sumar los digitos que componen el número ingresado

def suma_digitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + suma_digitos(numero // 10)

numero = 123
resultado = suma_digitos(numero)
print(resultado)

## 9) Cree una función llamada potencia(base, exponente) la cual debe devolver como resultado baseexponente , usando recursividad

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = 2
exponente = 3
resultado = potencia(base, exponente)
print(resultado)

## 10) Cree una función recursiva llamada imprimir_reversa(string) que reciba como parámetro una cadena de caracteres y los imprima al revez, por ejemplo imprimir_reversa(“Hola mundo”) debe dar odnuM aloH

def imprimir_reversa(string):
    if len(string) == 0:
        return string
    else:
        return imprimir_reversa(string[1:]) + string[0]

string = "Hola mundo"
resultado = imprimir_reversa(string)
print(resultado)

## 11) Cree un programa en Python que invierta el orden de un arreglo, ejemplo, se tiene: np.array([1, 2, 3, 4, 5]) el resultado debe ser [5, 4, 3, 2, 1]

arr = np.array([1, 2, 3, 4, 5])

nuevo_arr = arr[::-1]
print(nuevo_arr)

arr1 = np.array([1, 2, 3, 4, 5])
invertido_arr = np.flip(arr1)
print(invertido_arr)


## 12) Cree un función en Python llamada suma_espejo(arr1, arr2) que reciba como parámetros dosarreglos de igual longitud y devuelva otro arreglo con la suma de los valores del primer índice del primer arreglo con el último índice del segundo arreglo, la suma del valor del segundo índice del primer arreglo con el penúltimo valor del segundo arreglo

arr1 = [1, 2, 3]
arr2 = [1, 2, 3]

def suma_espejo(arr1, arr2):
    suma = []
    for i in range(len(arr1)):
        suma.append(arr1[i] + arr2[-i - 1])
    return suma

resultado = suma_espejo(arr1, arr2)
print(resultado)


## 13) Cree una función llamada concatena_array(arr1, arr2), la cual va a recibir dos array de strings deigual longitud y va a dar como resultado un string con la concatenación de los strings de cada par de indices de los arreglos.

arr1 = np.array(["la", "de", "pradera", "de"])
arr2 = np.array(["casa", "la", "es", "madera"])

def concatena_array(arr1, arr2):
    resultado = ""
    for i in range(len(arr1)):
        resultado += arr1[i] + " " + arr2[i] + " "
    return resultado

resultado = concatena_array(arr1, arr2)
print(resultado)


## 14) Complete las funciones preguntas() y respuestas(), para que al ejecutar el programa principal indique si la respuesta fue correcta, incorrecta o si se dejo sin contestar. En las funciones DEBE usar los tipos Enum mostrados. La función preguntas() no recibe parámetros y debe devolver de forma aleatoria algunas de las preguntas del Enum Preguntas, la función respuesta(preg, resp) recibe dos parámetros, el primero es la pregunta que generó el sistema, la segunda la respuesta que ingresó el usuario, y debe devolver del Enum Respuesta, según sea el caso.


class Respuestas(Enum):
    CORRECTO = "Respuesta correcta"
    INCORRECTO = "La respuesta es incorrecta"
    SIN_RESPUESTA = "Sin responder"

class Preguntas(Enum):
    PRIMERA = "¿Capital de Venezuela?"
    SEGUNDA = "¿Cuánto es 2 x 7"
    TERCERA = "¿Dónde queda la UCAB?"

def preguntas():
    number = randint(1,3)
    if number == 1:
        return Preguntas.PRIMERA.value
    elif number == 2:
        return Preguntas.SEGUNDA.value
    else:
        return Preguntas.TERCERA.value

def respuesta(preg, res):
    if preg == Preguntas.PRIMERA.value and res == "Caracas":
        return Respuestas.CORRECTO.value
    elif preg == Preguntas.SEGUNDA.value and res == "14":
        return Respuestas.CORRECTO.value
    elif preg == Preguntas.TERCERA.value and res == "Montalban":
        return Respuestas.CORRECTO.value
    else:
        return Respuestas.INCORRECTO.value

# Programa principal
if __name__ == "__main__":
    while True:
        pregunta = preguntas()
        print(pregunta)
        print()

        resp = input("Indique su respuesta: ")

        result = respuesta(pregunta, resp)
        print(result)

        continuar = input("Desea continuar [s/n]: ").lower()
        if continuar == "n":
            break

    print("Hasta Luego")