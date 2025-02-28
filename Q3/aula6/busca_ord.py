def busca_v1 (l: list, n: int) -> int:
    if n > l[-1]: return len(l)
    copia, r = l, 0
    while copia != []:
        tamanho = len(copia)
        i = int(tamanho / 2)
        print(copia, i, tamanho, r)
        if l[i] > n:
            copia = copia[i:]
            print(copia, i)
        elif l[i] < n:
            copia = copia[i - 1:]
            print(copia, i)
    return len(l)

def busca_v2 (l: list, n: int) -> int:
    return

print(busca_v1([2,4,6,7,8,9,11,13,15,17,19], 13))