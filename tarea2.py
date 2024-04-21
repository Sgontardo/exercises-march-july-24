import numpy as np

## 1) Complejidad algoritmo sumatoria(n) = O(n) (Lineal)

## 2) Complejidad algoritmo search_target(array, target) = O(n) (Lineal)

## 3) Complejidad algoritmo duplicar_elementos(array) = O(n) (Lineal)

## 4) Complejidad algoritmo

## 5) Complejidad algoritmo

## 6) Complejidad algoritmo

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

arr[::-1]
print(arr)

invertido_arr = np.flip(arr)
print(invertido_arr)


