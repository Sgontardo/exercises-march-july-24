def sumaHasta(n):
    if n == 0:
        return 0
    else:
        return n + sumaHasta(n-1)

n = int(input("Ingrese un número entero positivo: "))
print(sumaHasta(n))
