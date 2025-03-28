def mat_hilbert(n: int) -> [[float]]:
    return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]

def mat_inversa(H: [[float]]) -> [[float]]:
    n = len(H)
    I = [[1 if i == j else 0 for i in range (n)] for j in range (n)]
    aumentada = []
    for a in range(len(H)):
        aumentada.append(H[a] + I[a])
    
    return aumentada

    


print(mat_inversa(mat_hilbert(3)))