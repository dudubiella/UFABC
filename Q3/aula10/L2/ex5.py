def josephus(n: int, m: int) -> int:
    N = [a + 1 for a in range(n)]
    tam, pos = len(N), 0
    while tam > 1:
        pos = (pos + m - 1) % tam
        del(N[pos])
        tam = len(N)
    return N[0]