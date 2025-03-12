def busca_ord_sp (l: list, n: int) -> int:
    i, f = -1, len(l)
    while i < f - 1:
        m = (i + f) // 2
        if l[m] < n: i = m
        else: f = m
    return f