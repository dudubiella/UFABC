def fib (n: int) -> int:
    lista = [1, 1]
    for a in range(n - 1):
        lista.append(lista[-1] + lista[-2])
        print(lista[-1])
    return lista[-1]