def fatorial (n: int) -> int:
    if n == 0: return 1
    else: return n * fatorial (n-1)

def binomial (n: int, m: int) -> int:
    return fatorial (n)/(fatorial (m) * fatorial (n - m))