def merge(lista: list, q: int, p: int = 0, r: int = -1) -> list:
    if r == -1: r = len(lista)
    lista_ord = [0 for a in range(len(lista))]
    i, j, k = p, q, 0
    while i < q and j < r:
        if lista[i] <= lista[j]:
            lista_ord[k] = lista[i]
            i += 1
        else:
            lista_ord[k] = lista[j]
            j += 1
        k += 1
    if j < r:
        lista_ord[k:] = lista[j:r]
    else:
        lista_ord[k:] = lista[i:q]
    return lista_ord

def merge_sort(lista):
    if len(lista) < 2: return lista
    else:
        meio = len(lista) // 2
        print(meio)
        direita = merge_sort(lista[meio:])
        esquerda = merge_sort(lista[:meio])
        print(merge(direita + esquerda, len(direita)))
        return merge(direita + esquerda, len(direita))

print(merge_sort([0,12,4,1,-1,3,5]))
