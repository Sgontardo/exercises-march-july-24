def numero_armonico(n):
    if n == 0:
        return 0
    else:
        return 1/n + numero_armonico(n-1)

n = int(input("Ingrese un número: "))
print(f"El resultado del número armónico es: {numero_armonico(n)}")