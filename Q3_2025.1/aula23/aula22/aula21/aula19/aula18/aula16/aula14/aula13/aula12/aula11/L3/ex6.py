def bezout (m, n):
    r_ant, r, a_ant, b_ant, a, b = m, n, 1, 0, 0, 1
    while r != 0:
        quociente = r_ant // r
        r_ant, r, a_ant, a, b_ant, b = r, r_ant - quociente * r, a, a_ant - quociente * a, b, b_ant - quociente * b
    return (r_ant, a_ant, b_ant)