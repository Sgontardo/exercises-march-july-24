import numpy as np

# Se inicializa el vector con sus valores
edades = np.zeros((8,))
suma = 0
contador = 0
suma_fuera = 0

# se resuelve el algoritmo
i = 0
while i < 8:
    edades[i] = int(input(f'Ingrese la edad {i + 1}: '))

    if edades[i] >= 18 and edades[i] <= 22:
        suma += edades[i]
        contador += 1
    else:
        suma_fuera += edades[i]

    i = i + 1

promedio = suma / contador

# se expresan los resultados
print("la cantidad de estudiantes en el rango (18 ~ 22 ) es ", contador)
print( "la suma de las edades de estudiantes en el rango (18 ~ 22 ) es ", suma)
print("el promedio de edad de los estudiantes en el rango (18 ~ 22 ) es ", promedio)
print("la suma de edades de estudiantes fuera del rango (18 ~ 22 ) es ", suma_fuera)
