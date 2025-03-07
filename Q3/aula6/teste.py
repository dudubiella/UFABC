from busca_ord import busca_ord, busca_ord_rec
import time, random

def teste(l, n):
    t1 = time.time()
    time.sleep(0.05)
    print(busca_ord(l, n))
    t = time.time()
    dt1 = t - t1 - 0.05
    print(dt1)
    t1 = time.time()
    time.sleep(0.05)
    print(busca_ord_rec(l, n))
    t = time.time()
    dt2 = t - t1 - 0.05
    print(dt2)
    print('o tempo do programa com recursão leva', (dt2 / dt1) * 100, '% do tempo em comparação a busca sem recursão' )
        


b = 0
n = 10
l = [random.randrange(a, a + 2) for a in range(0, n, 2)]
n = random.randrange(0, n)
print(l, n)
teste(l, n)

