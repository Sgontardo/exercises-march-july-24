matriz1 = [
    [8, -2, 5, 4],
    [3, 5, 7, 13],
    [-5, 1, 9, -8],
    [2, 6, -4, -2]
]

matriz2 = [
    [4, -5],
    [-3, 6]
]

def determinante(matriz):
    if len(matriz) != len(matriz[0]):
        return "No se puede calcular la determinante de una matriz no cuadrada"
    else:
        if len(matriz) == 2:
            return matriz[0][0]*matriz[1][1] - matriz[0][1]*matriz[1][0]
        else:
            det = 0
            for i in range(len(matriz)):
                det += ((-1)**i)*matriz[0][i]*determinante([fila[:i] + fila[i+1:] for fila in matriz[1:]])
            return det

print(f"El determinante de la matriz es {determinante(matriz1)}")
print(f"El determinante de la matriz es {determinante(matriz2)}")