def busca_ord (l: list, n: int) -> int:
    i = 0
    while l != []:
        if n > l[-1] or n < l[0]: return -1
        mid = int (len (l) / 2)
        m = l[mid]
        if m < n: l, i = l[mid + 1:], i + mid + 1
        elif m > n: l = l[:mid]
        else: return i + mid

def busca_ord_rec (l: list, n: int, i: int = 0) -> int:
    if n > l[-1] or n < l[0]: return -1
    mid = int (len (l) / 2)
    m = l[mid]
    if m < n: return busca_ord_rec (l[mid + 1:], n, i + mid + 1)
    if m > n: return busca_ord_rec (l[:mid], n, i)
    return i + mid