#a) A estrutura de uma matriz 0-espiral é tal que seus elementos formam uma progressão aritmética de razão 0 com início em 1. Desta forma, a matriz A ∈ Z ^ n×n possui todos seus n ** 2 elementos iguais a 1.

#b)
def passos():
    return [
        (0, 1), (1, 0),
        (0, -1), (-1, 0)
    ]

def verifica_r_espiral(A: [[int]]) -> int:
    n, r, anterior = len(A), None, None
    if n == 0 or len(A[0]) != n:
        return r
    inicio, fim = [0, 0], [n - 1, n - 1]
    direcoes = passos()
    cont = 0
    i, j = inicio
    while inicio[0] <= fim[0] and inicio[1] <= fim[1]:
        atual = A[i][j]
        if anterior is None:
            if atual != 1:
                return None
        else:
            if r is None:
                r = atual - anterior
            elif atual != anterior + r:
                return None
        anterior = atual
        di, dj = direcoes[cont]
        proximo = (i + di, j + dj)
        if proximo[1] > fim[1] or proximo[0] > fim[0] or proximo[1] < inicio[1] or proximo[0] < inicio[0]:
            match cont:
                case 0: inicio[0] += 1
                case 1: fim[1] -= 1
                case 2: fim[0] -= 1
                case 3: inicio[1] += 1
            cont = (cont + 1) % 4
            di, dj = direcoes[cont]

            
        i, j = i + di, j + dj
    return r if r is not None else 0

#c)
def gera_espiral(r: int, n: int) -> list[list[int]]:
    A = [[0] * n for _ in range(n)]
    direcoes = passos()
    i = j = direcao = 0
    valor = 1
    for _ in range(n * n):
        A[i][j] = valor
        valor += r
        di, dj = direcoes[direcao]
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and A[ni][nj] == 0:
            i, j = ni, nj
        else:
            direcao = (direcao + 1) % 4
            di, dj = direcoes[direcao]
            i, j = i + di, j + dj
    return A