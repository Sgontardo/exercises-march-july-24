import numpy as np

# resoluion de ecuaciones por medio de la matriz inversa
# ver https://www.matesfacil.com/matrices/metodo-matriz-inversa-resolver-sistemas-ecuaciones-lineales-ejemplos.html

# se tiene el siguiente sistema de ecuaciones lineales:
#
# 2x + y = 7
# -3x + 2y = 7
#
# Se pide encontrar los valores de x, y usando la matriz inversa

matriz_a = np.array([
    [2, 1],
    [-3, 2]
])

matriz_b = np.array([
    [7],
    [7]
])

# para saber si es una matriz reguar calculamos el determinante de matriz_a:
determinante_a =  np.linalg.det(matriz_a)
print(determinante_a)

# como su valor es ~7 es regular
# calculamos la inversa:
inversa_a = np.linalg.inv(matriz_a)
print(inversa_a)

# Ahora los valores de x, y son:

solucion = np.dot(inversa_a, matriz_b)
print(f" el valor de x: {solucion[0][0]:.1f}, el de y: {solucion[1][0]:.1f}")

