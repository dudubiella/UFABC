def busc_pares(A: [int], x: int) -> int:
    A.sort()
    tam = len(A)
    i, j = 0, tam - 1
    while i < j:
        soma = A[i] + A[j]
        print(soma, A, i, j)
        if soma > x: j -= 1
        elif soma < x: i += 1
        else: return (i, j)
    return (tam, tam)

print(busc_pares([2, 3, 5, 4, 1], 9))