import numpy as np

matriz_b = np.array([
    [1, 2, 3],
    [4 ,5, 6],
    [7, 8, 9]
])

# Obtener dimensiones de la matriz
dimensiones = matriz_b.ndim
print(f"la dimensiones de matriz_b son: {dimensiones}")

# Obtener forma de la matriz (número de filas y columnas)
forma = matriz_b.shape
print(f"la forma de matriz_b son: {forma}")

# Obtener tamaño (número total de elementos) de la matriz
tamano = matriz_b.size
print(f"el tamaño de matriz_b es: {tamano} elementos")
