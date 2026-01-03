#cmd: python seqs.py < seqs.in > seqs.out
#o pipe:" | " faz a saido de um ser a entrada do outro
#ex: python seqs.py < seqs.in | python testes.py > notas_testes.out

def ler_inteiros():
    return list(map(int, input().split()))

def seqs (dim: [int, int]) -> bool:
    n, m = dim
    ant = ler_inteiros ()
    for _ in range (n - 1):
        atual = ler_inteiros ()
        diferencas = [atual[j] - ant[j] for j in range (m)]
        if not all (d == diferencas[0] for d in diferencas[1:]): return False
        ant = atual
    return True

def main():
    instancia = 1
    entrada = ler_inteiros()            #ler entrada antes de iniciar o laço
    while entrada and entrada[0] > 0:   #verificar se existe entrada, previnindo erros ao não encontrar o arquivo.in 
        resultado = "SIM" if seqs(entrada) else "NAO"
        if instancia > 1: print()
        print(f"Instancia {instancia}\n{resultado}")
        instancia += 1
        entrada = ler_inteiros()

if __name__ == "__main__":
    main ()