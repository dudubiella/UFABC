def num_diferente(A: [int]) -> int:
    distintos = 0
    for a in range(len(A)):
        tem_igual = False
        for b in range(a + 1, len(A)):
            if A[a] == A[b]: tem_igual = True
        if not tem_igual: distintos += 1
    return distintos

print(num_diferente([1,23, 1, 1,54,6,7,3,2,4,45,2]))