def min_max (lista: tuple) -> (float, float):
    max, min = lista[0], lista[0]
    if len (lista) > 1:
        for a in lista[1:]:
            if a > max:
                max = a
            if a < min:
                min = a
    print (min, max)
    return min, max

if __name__ == '__main__':
    min_max (tuple (map (float, input ('envie os números separados por espaços para que encontremos o maior e menor valor:\n').split ())))