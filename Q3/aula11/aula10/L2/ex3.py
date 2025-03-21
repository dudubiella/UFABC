def e_distantes(L: [int], d: int) -> int:
    max = 0
    for a in range(len(L)):
        for b in range(a + d, len(L)):
            if L[a] + L[b] > max: max = L[a] + L[b]
    return max