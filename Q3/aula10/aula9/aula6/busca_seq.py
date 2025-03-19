def ocorre_v1 (l: list, n: int) -> list:
    o = [i for i in range (len (l)) if l [i] == n]
    return o

def ocorre_v2 (l: list, n: int) -> list:
    i, o = 0, []
    while i < len (l):
        if l [i] == n:
            o.append (i)
        i += 1
    return o

def ocorre_v3 (l: list, n: int) -> list:
    i, f = 0, len (l)
    l.append (n)
    while n != l [i]:
        i += 1
    del (l, f)
    return i