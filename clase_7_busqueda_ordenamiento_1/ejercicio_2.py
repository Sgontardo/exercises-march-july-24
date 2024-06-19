"""
Crea una función que encuentre todas las posiciones de un elemento objetivo 
en un arreglo de cadenas de caracteres y devuelva un arreglo de índices. 
Si el elemento no se encuentra, debe devolver una lista vacía.


"""

arr = ["manzana", "banana", "cereza", "manzana", "pera", "manzana"]
objetivo = "manzana"

def busqueda_secuencial(arr, objetivo):
	indices = []
	for i in range(len(arr)):
		if arr[i] == objetivo:
			indices.append(i)
	return indices