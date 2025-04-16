def decision_sort(lista: list) -> list:
    for j in range(1, len(lista)):
        item, i = lista[j], j - 1
        while i >= 0 and item < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1
        lista[i + 1] = item
    return lista
