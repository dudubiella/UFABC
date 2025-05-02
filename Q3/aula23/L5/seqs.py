#cmd: python seqs.py < seqs.in > seqs.out
#o pipe:" | " faz a saido de um ser a entrada do outro
#ex: python seqs.py < seqs.in | python t3.py > t3.out

def ler_inteiros () -> [int]:
    return list (map (int, input().split()))

def seqs (dim: [int, int]) -> bool:
    n, m = dim
    if m >= 1:
        ant = ler_inteiros ()
        for _ in range (n - 1):
            atual = ler_inteiros ()
            diferencas = [atual[j] - ant[j] for j in range (m)]
            if not all (d == diferencas[0] for d in diferencas[1:]): return False
            ant = atual
    return True

def main ():
    instancia = 1
    dimensoes = ler_inteiros ()
    while dimensoes[0] > 0:
        resultado = "SIM" if seqs (dimensoes) else "NAO"
        print (f"Instancia {instancia}\n{resultado}\n")
        instancia += 1
        dimensoes = ler_inteiros ()
    return

if __name__ == "__main__":
    main ()