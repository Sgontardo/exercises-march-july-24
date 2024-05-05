"""
Encontrar todos los dígitos en un texto dado
"""
import re

room_description = "El número de la habitación es 42."
digits = re.findall(r'\d', room_description)
print(digits)
