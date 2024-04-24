def suma_cuadrados(n):
    if n == 1:
        return n
    else:
        return n**2 + suma_cuadrados(n-1)

n = int(input("Ingrese un número: "))
print(f"El resultado de la suma de cuadrados es: {suma_cuadrados(n)}")