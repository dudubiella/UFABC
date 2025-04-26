def inversoes (A: [int]) -> [(int, int)]:
    resposta = []
    for a in range (len (A)):
        for b in range (a + 1, len (A)):
            if A[a] > A[b]: resposta.append ((a, b))
    return resposta