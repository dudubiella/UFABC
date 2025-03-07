def primo (n):
    if n <= 1: return False
    for a in range (2, int (n ** 0.5)):
        if n % a == 0: return False
    return True