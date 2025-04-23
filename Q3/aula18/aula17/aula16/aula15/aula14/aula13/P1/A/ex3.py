def soma_max (A: [int]):
    maximo, n = 0, len(A)
    if n != 0: maximo = A[0]
    for i in range(n):
        for j in range(i, n):
            soma = sum(A[i:j + 1])
            if soma > maximo: maximo = soma
    return maximo