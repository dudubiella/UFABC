def num_diferentes(A: [int]) -> int:
    distintos = 0
    for a in range(len(A)):
        tem_igual = False
        for b in range(a + 1, len(A)):
            if A[a] == A[b]: tem_igual = True
        if not tem_igual: distintos += 1
    return distintos

def num_distintos(A: [int]) -> int:
    D = []
    for a in A:
        if a not in D: D.append(a)
    return len(D)