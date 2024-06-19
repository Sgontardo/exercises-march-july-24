"""
Escribe una función que realice una búsqueda secuencial en un arreglo de números 
enteros y devuelva el índice del primer elemento que sea igual a un número objetivo. 
Si el elemento no se encuentra, la función debe devolver -1.
	arreglo = [10, 23, 45, 70, 11, 15] 
	objetivo = 70
"""

arr = [10, 23, 45, 70, 11, 15]
objetivo = 70

def busqueda_secuencial(arr, objetivo):
	for i in range(len(arr)):
		if arr[i] == objetivo:
			return i
	return -1

print(busqueda_secuencial(arr, objetivo))