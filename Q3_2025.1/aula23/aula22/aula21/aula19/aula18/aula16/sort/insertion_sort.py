def insertion_sort(lista: list) -> list:
    for i in range(0, len(lista)):
        j, minimo = i + 1, i
        while j < len(lista):
            if lista[minimo] > lista[j]: minimo = j
            j += 1
        lista[i], lista[minimo] = lista[minimo], lista[i]
        print(lista[i])  
    return lista

print(insertion_sort([5,4,3,101,102,500,-5,13.05]))