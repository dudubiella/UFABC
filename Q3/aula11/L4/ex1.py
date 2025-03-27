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

print(RandomInsert([1,2,3,4,5,6,7,8,9]))

def lista_random (A: [int]) -> [int]:
    n = len(a)
    for j in range (0, n - 1):
        i = random.randrange(j, n)
        A[j], A[i] = A[i], A[j]
    return A