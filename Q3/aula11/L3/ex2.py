def busc_pares (A: [int], x: int) -> int:
    A.sort ()
    tam = len (A)
    i, j = 0, tam - 1
    while i < j:
        soma = A[i] + A[j]
        if soma > x: j -= 1
        elif soma < x: i += 1
        else: return (i, j)
    return (tam, tam)