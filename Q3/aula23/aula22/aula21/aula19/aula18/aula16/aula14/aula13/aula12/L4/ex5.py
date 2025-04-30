#a)

def mat_hilbert(n: int) -> [[float]]:
    return [[1 / (i + j + 1) for j in range(n)] for i in range(n)]

#b)

def mat_inversa(H: [[float]]) -> [[float]]:
    n = len(H)
    aumentada = [linha + [1 if i == j else 0 for j in range(n)] for i, linha in enumerate(H)]
    for coluna in range(n):
        linha_pivo = max(range(coluna, n), key=lambda r: abs(aumentada[r][coluna]))
        aumentada[coluna], aumentada[linha_pivo] = aumentada[linha_pivo], aumentada[coluna]
        pivo = aumentada[coluna][coluna]
        for j in range(coluna, 2*n):
            aumentada[coluna][j] /= pivo
        for i in range(n):
            if i != coluna and aumentada[i][coluna] != 0:
                fator = aumentada[i][coluna]
                for j in range(coluna, 2*n):
                    aumentada[i][j] -= fator * aumentada[coluna][j]
    inversa = [linha[n:] for linha in aumentada]
    return inversa

def mult_mat(A: [[float]], B: [[float]]) -> [[float]]:
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def mat_identidade(n: int) -> [[float]]:
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def mat_dif(A: [[float]], B: [[float]]) -> float:
    return max(abs(A[i][j] - B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

#c)

def teste_matriz_hilbert(n: int):
    H = mat_hilbert(n)
    H_inv = mat_inversa(H)
    I_calculada = mult_mat(H, H_inv)
    I_esperada = mat_identidade(n)
    erro_maximo = mat_dif(I_calculada, I_esperada)
    print(f"Para n={n}, erro máximo: {erro_maximo:.2e}")

teste_matriz_hilbert(50)

#Devido ao mal-condicionamento da matriz de Hilbert, para n ≥ 10 o produto H·H⁻¹ pode diferir significativamente da matriz identidade por erros numéricos e arredondamentos acumulados.