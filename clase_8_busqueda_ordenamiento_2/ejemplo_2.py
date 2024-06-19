"""
Algoritmo de burbuja optimizado
"""

def burbuja_optimizada_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


arreglo = [15, 27, 1, 12, 6, 18, 9, 21, 13, 5]
print(arreglo)

ordenado = burbuja_optimizada_sort(arreglo)
print(ordenado)