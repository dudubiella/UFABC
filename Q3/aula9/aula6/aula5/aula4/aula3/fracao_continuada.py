def frac_cont (n: int, d: int) -> [int]:
    a = []
    while (r := n // d) >= 0:
        a.append (r)
        n, d = d, n % d
        if d <= 0: return a

def reverse_frac_cont (l: [int]) -> (int, int):
    tamnho = len (l)
    n, d = 1, l[-1]
    if tamnho == 1: return (l[0], 1)
    for i in range(tamnho - 2, 0, -1):
        n, d = d, l[i] * d + n
    return (l[0] * d + n, d)