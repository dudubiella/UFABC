def Asterisco (n):
    if n > 0:
        Asterisco (n - 1)
        for i in range (n):
            print (n,"*")
        Asterisco (n - 1)

def num_asteriscos (n): 
    r = 0
    for i in range(0, n):
        r += (n - i) * 2 ** (i)
    return r

#Somatória (i = 0 até (n - 1)) de: ((n - i) * 2 ** (i)) = n * 2 ** 0 (= n) + (n - 1) * 2 ** 1 (= (n-1) * 2) ... (n - (n - 1)) * 2 ** (n - 1) (= 1 * 2 ** (n - 1))