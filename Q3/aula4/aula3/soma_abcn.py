def soma (a: float, b: float, c: int, n: int) -> float:
    return sum((-1) ** (i * c) / b ** (i * a) for i in range(n))