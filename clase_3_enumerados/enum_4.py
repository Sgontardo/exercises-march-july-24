from enum import Enum

class Animal(Enum):
    perro = 1
    gato = 2
    leon = 3

# Comparación usando "is"
if Animal.perro is Animal.gato:
    print("Perro y gato son los mismos animales")
else:
    print("Perro y gato son animales distintos")

# Comparación usando "!="
if Animal.leon != Animal.gato:
    print("Leon y gato son animales distintos")
else:
    print("Leon y gato son los mismos animales")
