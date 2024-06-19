"""
Crea una función que realice una búsqueda binaria iterativa en una lista ordenada 
de cadenas de caracteres y devuelva el índice del elemento objetivo. Si el 
elemento no se encuentra, debe devolver -1.


"""

lista = ["avion", "barco", "coche", "tren"]
objetivo = "coche"

def busqueda_binaria(lista, objetivo):
	inicio = 0
	final = len(lista) - 1
	while inicio <= final:
		medio = (inicio + final) // 2
		if lista[medio] == objetivo:
			return medio
		elif lista[medio] < objetivo:
			inicio = medio + 1
		else:
			final = medio - 1
	return -1