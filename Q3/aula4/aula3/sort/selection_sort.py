def decision_sort(lista: list) -> list:
    for a in range(len(lista) - 1):
        for b in range(a + 1, len(lista)):
            if lista[b] < lista[a]: lista[b], lista[a] = lista[a], lista[b]
    return lista
            
print(decision_sort([5, 7, 10, -2, -13, 100, 101, 104]))
for a in range(10): print(a)