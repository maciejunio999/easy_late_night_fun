import math
from decimal import Decimal

def calculate_area(lista):
    a, b, c = lista[0], lista[1], lista[2]
    p = a + b + c
    return round(Decimal(math.sqrt(p * (p - a) * (p - b) * (p - c))), 2)