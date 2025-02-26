import math

def latas (r: float, h: float, l: float, c: float, p: float) -> (int, float):
    num = math.ceil ((2 * math.pi * r * (h + r)) / p * l)
    return num, num * c