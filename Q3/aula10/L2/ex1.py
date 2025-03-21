def taylor(x: float, E: float) -> float:
    tk = x
    ant = 0
    k = 2
    while abs(tk - ant) > E:
        tk, ant = tk + (-1) ** (k + 1) * x ** k / k, tk
        k += 1
    return tk