def exp(x: float, n: int) -> float:
    e = f = 1
    for a in range(1, n + 1):
        f *= x / a
        e += f
    return e