
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

def raiz_polinomio(A: [float], x0: float, l: int, epsilon: float) -> (float, float):
    x_atual, i, delta = x0, 0, float('inf')
    while i < l and delta > epsilon:
        p_x = polinomio(A, x_atual)
        dp_x = polinomio(derivada_polinomial(A))
        if dp_x == 0: break
        x_prox = x_atual - p_x / dp_x, x_atual
        delta = abs(x_atual - x_prox)
        x_atual = x_prox
        i += 1
    return x_atual, delta

#d)


print(polinomio([10,1,1],2),derivada_polinomial([11,2,3]))
