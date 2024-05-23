import numpy as np

matriz_b = np.array([
    [1, 2, 3],
    [4 ,5, 6],
    [7, 8, 9]
])

# determinante de la matriz
determinante = np.linalg.det(matriz_b)

print(determinante)