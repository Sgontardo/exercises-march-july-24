# Leer 4 bytes de un archivo binario
with open('data.bin', 'rb') as file:
    data = file.read(4)
    print(data)  # Muestra los bytes leídos

    numero = int.from_bytes(data)
    print(numero)