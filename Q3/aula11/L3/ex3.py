def permutacao(S: [int], T: [int]):
    tam = len(S)
    for a in range(tam - 1):
        print(S[:a + 1], T[tam - a - 1:])
        if S[:a + 1] == T[tam - a - 1:] and S[a + 1:] == T[:tam - a - 1]: return True
    return False
print(permutacao([2, 3, 5, 4, 1], [2, 4, 1, 3, 5]))