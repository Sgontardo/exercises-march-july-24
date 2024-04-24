import numpy as np

vector = np.array([23, 18, 36, 4, 57, 14, 22, 41, 12, 27, 9, 55])

def maxmin(arr):
    maximo_valor = arr[0]
    minimo_valor = arr[0]

    for i in arr:
        if i > maximo_valor:
            maximo_valor = i
        if i < minimo_valor:
            minimo_valor = i

    return (f"El valor máximo es: {maximo_valor} y el valor mínimo es: {minimo_valor}")

print(maxmin(vector))