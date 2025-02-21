def quadra(n: int = 20) -> None:
    [print(a, b, c, d) for a in range(1, n + 1) for b in range(a + 1, n + 1) for c in range(b + 1, n + 1) for d in range(c + 1, n + 1)]
    return 
