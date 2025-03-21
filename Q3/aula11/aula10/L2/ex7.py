def sub_list(A: [int], L: [int]):
    tam = len(A)
    if tam == 0: return True
    i = 0
    for l in L:
        if l == A[i]:
            i += 1
            if i == tam: return True
    return i == tam