#a)

def determinante (A: (int, int), B: (int, int), C: (int, int)) -> float:
    return A[0] * (B[1] - C[1]) - A[1] * (B[0] - C[0]) + (B[0] * C[1] - B[1] * C[0])

def area_triangulo (A: (int, int), B: (int, int), C: (int, int)) -> float:
    return abs (determinante (A, B, C)) / 2

#b)

def ponto_interior (X: [int], Y: [int], C: (int, int)) -> bool:
    for i in range (len(X) + 1):
        if determinante ((X[i - 1], Y[i - 1]), (X[i], Y[i]), C) > 0: return False
    return True