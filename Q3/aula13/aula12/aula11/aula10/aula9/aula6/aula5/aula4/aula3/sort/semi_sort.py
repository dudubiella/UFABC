def semi_sort(lista: list, p: int, q: int, r: int = -1) -> list:
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
        lista_ord[k:] = lista[i:r]
    return lista_ord

def merge_sort

print(semi_sort([1,1,3,4,0,2,3,5,8], 0, 4, 10))

