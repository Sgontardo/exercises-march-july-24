import numpy as np

# Ejemplo de análisis de datos

# Crear un array de datos
datos = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calcular la media y la desviación estándar de los datos
media = np.mean(datos)
desviacion_estandar = np.std(datos)

print(f"la media es {media}")
print(f"la desviación estandar es {desviacion_estandar:.4f}")