def hanoi(n, source, dest, temp):
    global contador # Se declara contador como global para que pueda ser utilizada dentro de la función
    if n == 1:
        print("Paso", contador + 1, "de", source, "a", dest)
        contador += 1
    else:
        hanoi(n-1, source, temp, dest)
        print("Paso", contador + 1, "de", source, "a", dest)
        contador += 1
        hanoi(n-1, temp, dest, source)

n = 3
source = 1
temp = 2
dest = 3
contador = 0

hanoi(n, source, dest, temp)
print("La función hanoi se ha llamado", contador, "veces")