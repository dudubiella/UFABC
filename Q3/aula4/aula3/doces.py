def fatorial(n):
    if n == 1 or n == 0: return 1
    return n * fatorial(n-1)

def distribui (n: int, m: int) -> int:
    if n < m: return 0
    sobra = n - m
    return int(fatorial(n-1)/(fatorial(m-1)*fatorial(sobra)))
