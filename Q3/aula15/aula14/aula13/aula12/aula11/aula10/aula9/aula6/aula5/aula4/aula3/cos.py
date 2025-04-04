def cos(x: float, eps: float) -> float:
    c, f, fk, k = 0.0, 0.0, 1, 0
    while eps < abs(fk - f):
       c, f, k = c + fk, fk, k + 1
       fk *= -x * x / (2 * k * (2 * k - 1))
    return c