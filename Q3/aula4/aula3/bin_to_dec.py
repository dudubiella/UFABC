def bin_to_dec (b: str) -> int:
    p, n = 1, 0
    for a in range(len(b) -1, -1, -1):
        n += int(b[a]) * p
        p *= 2
    return n