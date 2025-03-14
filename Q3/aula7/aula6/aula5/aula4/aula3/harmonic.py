def harmonic (n: int) -> float:
    return sum(1 / a for a in range(1, n + 1))