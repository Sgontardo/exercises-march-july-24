# Escribir datos binarios en un archivo
numero = 16909060
data= (numero).to_bytes(length=4)
print(data)

with open('data.bin', 'wb') as file:
    file.write(data)