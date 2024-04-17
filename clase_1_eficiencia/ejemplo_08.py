def busqueda_binaria(arr, target):
    low = 0 
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"La fruta {buscar} está en la posición {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"La fruta {buscar} NO fue encontrada"

frutas = ["cambur", "kiwi", "limón", "manzana", "melón", "naranja", "pera"]
buscar = "naranja"
print(busqueda_binaria(frutas, buscar))