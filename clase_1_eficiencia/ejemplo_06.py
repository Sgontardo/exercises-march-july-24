def multiplicacion_de_n(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} * {j} = {i*j}")

multiplicacion_de_n(9)

# igualmente con arraya de N elementos
print()
frutas = ["manzana", "naranja", "pera", "kiwi", "melón"]

def vocales_en_array(arr):
    vocales = "aeiouáéíóú"
    for item in arr:
        for ch in item:
            if ch in vocales:
                print(ch, end=" ")

    print()

vocales_en_array(frutas)
print()

# simplificación al peor caso:
def multiplicacion_de_n_plus(n):
    for i in range(1, n+1):
        print(i, end = " ")
    print()

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} * {j} = {i*j}")

multiplicacion_de_n_plus(9)