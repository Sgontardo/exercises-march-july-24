import numpy as np

matriz_b = np.array([
    [1, 2, 3],
    [4 ,5, 6],
    [7, 8, 9]
])

# ojo: solo funciona cuando la matriz es definida con NumPy
matriz_transpuesta = matriz_b.T

print(matriz_b)
print(matriz_transpuesta)