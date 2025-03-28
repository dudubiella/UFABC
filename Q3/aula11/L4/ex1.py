import random
def RandomInsert (A):
    n = len (A)
    for j in range (1,n):
        print (A, j)
        x = A[j]
        for i in range (j-1,-1,-1):
            print (i)
            print (A)
            if random.random() > 0.5: 
                A[i+1] = A[i]
                print (A)
            else: break
        A[i+1] = x
    return A

#A solução apresentada apresenta falhas na sua lógica de programação, pois apesar de utilizar a biblioteca random a lista devolvida não é embaralhada completamente, com os elementos não tendo a mesma probabilidade de estarem em qualquer posição da lista, por exemplo o primeiro elemento que nunca é trocado de sua posição inicial.

#Código correto para realizar o embaralhamento aleatório dos elementos de uma lista A.

def lista_random (A: [int]) -> [int]:
    n = len(a)
    for j in range (0, n - 1):
        i = random.randrange(j, n)
        A[j], A[i] = A[i], A[j]
    return A