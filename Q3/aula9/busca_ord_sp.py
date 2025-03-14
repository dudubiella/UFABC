def busca_ord_sp (l: [int], n: int) -> int:
    i, f = -1, len(l)
    while i < f - 1:
        m = (i + f) // 2
        if l[m] < n: i = m
        else: f = m
    return f

def busca_ord_sp_rec (l: [int], n: int) -> int:
    def busca_rec (l: [int], i: int, d: int, n: int) -> int:
        if f == i - 1: return f
        m = (i + f) // 2
        if l[m] < n: return busca_rec (l, m, d, n)
        else: return busca_rec (l, m, d, n)
    return busca_rec (l, -1, len(l), n)