
#a)

def polinomio(A: [float], z: float) -> float:
    resultado = 0
    for a in reversed(A): resultado = resultado * z + a
    return resultado

#b)

def derivada_polinomial(A: [float]) -> [float]:
    return [i * A[i] for i in range(1, len(A))]

#c)

#A são os coeficientes para os calculos do polinomio e sua derivada

def raiz_polinomio(p_x, dp_x, x0: float, l: int, epsilon: float) -> (float, float):
    x_atual, i, delta = x0, 0, float('inf')
    while i < l and delta > epsilon:
        if dp_x == 0: break
        x_prox = x_atual - p_x(x_atual) / dp_x(x_atual)
        delta = abs(x_atual - x_prox)
        x_atual = x_prox
        i += 1
    return x_atual, delta

#d)

def raiz_p_esima(v: float, p: int) -> float:
    coeficientes = [-v] + [0] * (p - 1) + [1]
    p_x = lambda x: polinomio(coeficientes, x)
    dp_x = lambda x: polinomio(derivada_polinomial(coeficientes), x)
    x0 = max(1.0, v)
    raiz, _ = raiz_polinomio(p_x, dp_x, x0, l=1000, epsilon=1e-6)
    return round(raiz, 6)

#e)

raiz_5_11 = raiz_p_esima(11, 5)
print(f"Raiz quíntupla de 11: {raiz_5_11}")