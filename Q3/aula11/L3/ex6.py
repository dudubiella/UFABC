def bezout(m, n):
    d, r = m, n
    a_ant, a = 1, 0
    b_ant, b = 0, 1
    while r != 0:
        quociente = d / r
        d, r = r, d - quociente * r
        a_ant, a = a, a_ant - quociente * a
        b_ant, b = b, b_ant - quociente * b
    return (d, a_ant, b_ant)