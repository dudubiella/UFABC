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

def num_distintos_ord(A: [int]) -> int:
    if A == []: return 0
    A.sort()
    ant, contador = A[0], 1
    print(A)
    for a in A[1:]:
        print(contador)
        if a > ant: contador += 1
        ant = a
    return contador

print(num_distintos_ord([3,1,55,2,23,43,2321,1,33,2,3,2,2,5]))