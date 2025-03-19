def e_distantes(L: [int], d: int) -> int:
    max = 0
    for a in range(len(L)):
        for b in range(a + d, len(L)):
            if L[a] + L[b] > max: max = L[a] + L[b]
            print(a, b)
    return max

print(e_distantes([1,2,67,835,2845,254452,2131,421,1,0],9))