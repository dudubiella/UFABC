def max_zeros(A: [int]) -> (int, int, int):
    i = 0
    ant = A[i]
    for a in range(1, len(A)):
        if ant != 0 and A[a] == 0: return

max_zeros([1,23,43,0,0,0,1,2,0,0,12,23,423,0,0,0,0,432,523,23,0,0,0,423,0])