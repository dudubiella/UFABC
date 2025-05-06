#a)
def inversa(q: [int]) -> [int]:
    n = len(q)
    inv = [0] * (n)
    for i, qi in enumerate(q):
        inv[qi - 1] = i + 1
    return inv

def sao_camaradas(p: [int], q: [int], r: [int]) -> bool:
    n = len(p)
    q_inv = inversa(q)
    for k in range(1, n + 1):
        if p[k - 1] != q[r[q_inv[k - 1] - 1] - 1]: return False
    return True

#b)
def decompor_ciclos(permut:[int]) -> (bool, [int]):
    n = len(permut)
    visitados = [False] * n
    ciclos = []
    for i in range(n):
        if not visitados[i]:
            ciclo = []
            atual = i
            while not visitados[atual]:
                visitados[atual] = True
                ciclo.append(atual + 1)
                atual = permut[atual] - 1
            idx = ciclo.index(min(ciclo))
            ciclos.append(ciclo[idx:] + ciclo[:idx])
    return sorted(ciclos, key=lambda x: (len(x), x))

def sao_camaradaveis(p: [int], r: [int]) -> (bool, list[int] | None):
    n = len(p)
    if len(r) != n: return (False, None)
    ciclos_p = decompor_ciclos(p)
    ciclos_r = decompor_ciclos(r)
    if sorted(len(c) for c in ciclos_p) != sorted(len(c) for c in ciclos_r): return (False, None)
    q = [0] * n
    for cp, cr in zip(ciclos_p, ciclos_r):
        if len(cp) != len(cr): return (False, None)
        for elem_p, elem_r in zip(cp, cr):
            q[elem_r - 1] = elem_p
    return (True, q)