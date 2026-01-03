def main ():
    instancia = 1
    n = input()
    while n and n != "0":
        n = int (n)
        achou = False
        m_max = int (n**0.5)
        if instancia > 1: print()
        for m in range (m_max, 0, -1):
            denom =  (m+1)**2           # (p1 + m) = (p2 - m) = (p3 * m) = (p4 / m) = k
            num = n * m                 # n = p1 + p2 + p3 + p4 = (k − m) + (k + m) + (k / m) + (k * m) = 2 * k + k / m + k * m = k / m * (2 * m + 1 + m * m) = k / m * (m + 1) ** 2
            if num % denom != 0:        # k = n * m / ((m + 1) ** 2)
                continue
            k = num // denom
            if k % m != 0:
                continue
            p1 = k - m
            p2 = k + m
            p3 = k // m
            p4 = k * m
            if p1 + p2 + p3 + p4 == n:
                print (f"Instancia {instancia}\n{m} {p1} {p2} {p3} {p4}")
                achou = True
                break
        if not achou:
            print (f"Instancia {instancia}\n{n} nao e quadripartido")
        instancia += 1
        n = input()

if __name__ == "__main__":
    main ()