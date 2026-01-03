def direcoes_3d ():
    return [
        (1, 0, 0), (0, 1, 0), (0, 0, 1), # direções dos eixos (linhas, colunas, altura)
        (1, 1, 0), (1, -1, 0), # diagonais da face linha-coluna (XY)
        (1, 0, 1), (1, 0, -1), # diagonais da face linha-altura (XZ)
        (0, 1, 1), (0, 1, -1), # diagonais da face coluna-altura (YZ)
        (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1) # diagonais espaciais (cubo 3D)
    ]

def esta_dentro_limites (tamanho, l, c, a):
    return 0 <= l < tamanho and 0 <= c < tamanho and 0 <= a < tamanho

def verificar_vitoria (tabuleiro, tamanho, l, c, a, cor):
    for dx, dy, dz in direcoes_3d ():
        cont = 1
        for sinal in  (1, -1):
            prox_l, prox_c, prox_a = l + sinal * dx, c + sinal * dy, a + sinal * dz
            while esta_dentro_limites (tamanho, prox_l, prox_c, prox_a) and tabuleiro[prox_l][prox_c][prox_a] == cor:
                cont += 1
                prox_l += sinal * dx
                prox_c += sinal * dy
                prox_a += sinal * dz
        if cont >= tamanho:
            return True
    return False

def processar_jogadas (tamanho, jogadas):
    tabuleiro = [[[None] * tamanho for _ in range (tamanho)] for _ in range (tamanho)]
    ganhador = None
    for idx,  (lin, col) in enumerate (jogadas):
        if ganhador:
            continue
        lin -= 1; col -= 1
        for alt in range (tamanho):
            if tabuleiro[lin][col][alt] is None:
                break
        cor = 'Branco' if idx % 2 == 0 else 'Azul'
        tabuleiro[lin][col][alt] = cor
        if verificar_vitoria (tabuleiro, tamanho, lin, col, alt, cor):
            ganhador = cor
    return ganhador

def main ():
    instancia = 1
    entrada = input()
    while entrada and entrada != "0":
        tamanho = int (entrada)
        jogadas_totais = tamanho ** 3
        jogadas = [tuple (map (int, input().split())) for _ in range (jogadas_totais)]
        ganhador = processar_jogadas (tamanho, jogadas)
        if instancia > 1: print ()
        print (f"Instancia {instancia}\n{ganhador} ganhou" if ganhador else "Empate")
        instancia += 1
        entrada = input ()

if __name__ == '__main__':
    main ()