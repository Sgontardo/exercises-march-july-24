import numpy as np

matriz_a = np.array([
    [1, 2, 3],
    [4 ,5, 6],
    [7, 8, 9]
])

matriz_b = np.array([
    [3, 2, 1],
    [7 ,8, 9],
    [4, 5, 6]
])

# multiplicación de matrices
matriz_producto = np.dot(matriz_a, matriz_b)

print(matriz_producto)