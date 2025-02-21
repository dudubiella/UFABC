def perfeito(n):
    return n == sum ([a for a in range(1, n // 2 + 1) if n % a == 0])
