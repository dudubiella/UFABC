def primolog(n):
    l = [False, False] + [True for a in range(n-1)]
    c = 2
    while c * c <= n:
        j = 2
        while j * c <= n:
            l [j * c] = False
            j += 1
        c += 1
    return [a for a in range(len(l)) if l[a]]