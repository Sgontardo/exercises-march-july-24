import re # regular expressions

# cadenas de caracteres:

    # cálculo de la longitud de una cadena
cadena = "Hola mundo"
print(len(cadena))

    # comparación de cadenas
cadena1 = "Hola mundo"
cadena2 = "Hola cadena"

if cadena1 == cadena2:
    print("Las cadenas son iguales")
else:
    print("Las cadenas son diferentes")
    # se puede aplicar los operadores >, <, >=, <=, !=

    # concatenación de cadenas
cadena3 = cadena1 + " " + cadena2
print(cadena3)

    # extracción de subcadenas, se llama slicing
cadena4 = "Esta es una cadena de caracteres"

# con los 6 primeros caracteres
cadena5 = cadena4[0:6]
print(cadena5)
# usando indice negativo
cadena6 = cadena4[-10:-1]
print(cadena6)
#desde el comienzo hasta final, pero de dos en dos
cadena7 = cadena4[::2]
print(cadena7)
# invertir una cadena
cadena8 = cadena4[::-1]
print(cadena8)

    # búsqueda de subcadenas
if cadena4 in "cadena":
    print("La subcadena está en la cadena")
else:
    print("La subcadena no está en la cadena")

    # algunos métodos de cadenas
    cadena9 = cadena4.count("a") # cuenta cuantas veces aparece la letra "a"
    cadena10 = cadena4.find("a") # devuelve la posición de la primera aparición de la letra "a"
    cadena11 = cadena4.upper() # convierte la cadena a mayúsculas
    cadena12 = cadena4.lower() # convierte la cadena a minúsculas
    cadena13 = cadena4.replace("a", "e") # reemplaza la letra "a" por la letra "e"
    cadena14 = cadena4.split(" ") # divide la cadena en subcadenas, usando el espacio como separador
    cadena15 = cadena4.strip() # elimina los espacios en blanco al principio y al final de la cadena
    cadena16 = cadena4.isalnum() # devuelve True si la cadena contiene solo letras y números
    cadena17 = cadena4.isalpha() # devuelve True si la cadena contiene solo letras
    cadena18 = cadena4.isdigit() # devuelve True si la cadena contiene solo números
    cadena19 = cadena4.islower() # devuelve True si la cadena contiene solo letras minúsculas
    cadena20 = cadena4.isupper() # devuelve True si la cadena contiene solo letras mayúsculas


# expresiones regulares (regex), para comparación de patrones y manipulación de cadenas. Casos:
# Validar expresiones como dirección de email, números de teléfono, fortaleza de contraseñas, etc.
# Búsqueda de patrones como fechas, URL, menciones, etc.
# Reemplazo de patrones en cadenas de texto

# comparación de cadenas:

re.search(r"cadena", "Esta es una cadena de caracteres") # busca la palabra "cadena" en la cadena
re.match(r"Esta", "Esta es una cadena de caracteres") # busca la palabra "Esta" al principio de la cadena
re.findall(r"cadena", "Esta es una cadena de caracteres, otra cadena") # busca todas las ocurrencias de "cadena" en la cadena
re.sub(r"cadena", "cadena2", "Esta es una cadena de caracteres") # reemplaza "cadena" por "cadena2" en la cadena
re.compile(r"cadena") # compila la expresión regular para su uso posterior

re.IGNORECASE # ignora las mayúsculas y minúsculas en la búsqueda
re.MULTILINE # busca en todas las líneas de la cadena
re.DOTALL # busca en todas las líneas de la cadena, incluyendo saltos de línea

pattern = re.compile(r"hello", re.IGNORECASE)
match = pattern.search("Hello, world!")
