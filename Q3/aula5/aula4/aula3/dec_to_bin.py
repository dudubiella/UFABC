def dec_to_bin (n: int) -> str:
    b = ""
    while n > 0:
        b = str (n % 2) + b
        n //= 2
    return b