import numpy as np

# Definir coeficientes de las ecuaciones
# El sistema de ecuaciones de esta manera:
# 2x + 3y = 8
# x -2y = 1

coeficientes = np.array([[2, 3], [1, -2]])
resultados = np.array([8, 1])

# Resolver el sistema de ecuaciones lineales
solucion = np.linalg.solve(coeficientes, resultados)
print(f"la solución es: {solucion}")
print(f"En otras palabras: x = {solucion[0]:.2f}, y = {solucion[1]:.2f}")
