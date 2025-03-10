from aula2.bhaskara import bhaskara

def pos (a: float, b: float, c: float, d: float, t: float) -> float:
    return a * t ** 3 + b * t * t + c * t + d

def min_global (a: float, b: float, c: float, d: float, t: float) -> float:
    if 6 * a * t + 2 * b > 0: return True
    prox = 1e-10
    x1 = pos (a, b, c, d, t - prox)
    x2 = pos (a, b, c, d, t)
    x3 = pos (a, b, c, d, t + prox)
    if x2 > x1 and x2 < x3: return True
    else: return False

def fonc3grau (a: float, b: float, c: float, d: float, t1: float, t2: float) -> float:
    p1 = pos (a, b, c, d, t1)
    p2 = pos (a, b, c, d, t2)
    pmin = min (p1, p2)
    poss_min = bhaskara (3 * a, 2 * b, c)
    for a in range (poss_min[0]):
        p = pos (poss_min[a + 1])
        if p1 < p < p2 and min_global (a, b, c, d, p):
            pmin = p
    return pmin
