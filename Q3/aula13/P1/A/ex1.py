def soma_multiplos (n: int, p: int, q: int) -> int:
    r = 0
    for i in range(2, n + 1):
        if i % p == 0 or i % q == 0: r += i
    return r