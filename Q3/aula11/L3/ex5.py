def inversoes(A: [int]) -> [(int, int)]:
    resposta = []
    for a in range(len(A)):
        for b in range(a + 1, len(A)):
            print(a, b, A[a], A[b])
            if A[a] > A[b]: resposta.append((a, b))
    return resposta

print(inversoes( [2, 3, 8, 6, 1]))