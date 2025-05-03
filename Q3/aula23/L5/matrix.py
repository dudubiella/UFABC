def letra_em (palavra, lin, col):
    L = len (palavra)
    return palavra[(col - lin) % L]

def conta_caminhos (i0, j0, palavra):
    L = len (palavra)
    if letra_em (palavra, i0, j0) != palavra[0]:
        return 0
    caminho = { (i0, j0): 1}
    for k in range (1, L):
        prox_letra = palavra[k]
        prox_caminho = {}
        for  (l, c), atual_caminho in caminho.items ():
            prox_c = c + 1
            if prox_c < L and letra_em (palavra, l, prox_c) == prox_letra: prox_caminho[(l, prox_c)] = prox_caminho.get ((l, prox_c), 0) + atual_caminho
            prox_l = l - 1
            if prox_l >= 0 and letra_em (palavra, prox_l, c) == prox_letra: prox_caminho[(prox_l, c)] = prox_caminho.get ((prox_l, c), 0) + atual_caminho
        if not prox_caminho:
            return 0
        caminho = prox_caminho
    return sum (caminho.values ())

def main ():
    instancia = 1
    entrada = input().split()
    while entrada and not (entrada[0] == '-1' and entrada[1] == '-1'):
        i, j = map (int, entrada[:2])
        palavra = entrada[2]
        total = conta_caminhos (i, j, palavra)
        if instancia > 1: print ()
        print (f"Instancia {instancia}\n{total}")
        instancia += 1
        entrada = input().split()

if __name__ == "__main__":
    main ()