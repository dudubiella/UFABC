#a) A matriz A é C-simétric se, e somente se, para todo 0 ≤ i,j < n vale: A[i][j] == A[k][l] tal que o k = n - i - 1 e l = n - j - 1, isso implica que A[i][j] =  A[n - i - 1][n - j - 1]

#b)
def verifica_C_simetrica(A: [[float]]) -> bool:
    n = len(A)
    if n == 1 and len(A[0]) == 0: return True
    B = [[False] * len(A[0]) for _ in range(n)]
    for i in range(n):
        for j in range(n - i):
            k, l = n - i - 1, n - j - 1
            if B[i][j] == False and (i,j) != (k, l):
                if A[i][j] != A[k][l]: return False
                else: B[i][j] = B[k][l] = True
    return True

#c)
def verifica_D_constante(T: [[float]]) -> bool:
    n = len(T)
    for i in range(1, n):
        for j in range(1, n):
            if T[i][j] != T[i-1][j-1]: return False
    return True

#d) A matriz T, sendo D‑constante, é também C‑simétrica se, e somente se, para todo 0 ≤ i,j < n valer T[i][j] = T[j][i], isso implica que os valores nas diagonais acima da diagonal principal coincidem com os valores nas diagonais abaixo da principal, garantindo a C‑simetria.

#e)
def cria_T(y: [float]) -> [[float]]:
    n = len(y)
    T = []
    for i in range(n):
        T.append([0] * i + y + [0] * (n - i - 1))
    return T

def z(x: [float], y: [float]) -> [float]:
    T = cria_T(y)
    n = len(x)
    m = 2 * n - 1
    z = [0] * m
    for j in range(m):
        for i in range(n):
            z[j] += x[i] * T[i][j]
    return z

#f) O produto z = x ^ T * T(y) equivale à convolução discreta entre x e y, pois cada coordenada z[k] = ∑(i = 0 à n - 1) x[i] * y[k - i], tal que y[k - i] = 0 se k - i está fpra do intervalo [0, n-1]