def permutacao (S: [int], T: [int]):
    tam = len (S)
    for a in range (tam - 1):
        if S[:a + 1] == T[tam - a - 1:] and S[a + 1:] == T[:tam - a - 1]: return True
    return False
