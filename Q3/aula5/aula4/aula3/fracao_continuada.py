def frac_cont (n: int, d: int) -> [int]:
    a = []
    while (r := n // d) >= 0:
        a.append (r)
        print (r, n, d)
        n, d = d, n % d
        if d <= 0: return a
