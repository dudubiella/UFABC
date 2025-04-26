def mdc (m: int, n: int) -> int:
    if m < n: m, n = n, m
    while (r := m % n) > 0:
        m, n = n, r
    return n