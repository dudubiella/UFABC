#algoritmo Knuth–Morris–Pratt KMP

def KMP(S: [int], T: int) -> int:
    i = j = ocorrencias = 0

    while j < len(T):
        if S[i] == T[j]:
            i += 1
            if i == len(S) - 1:
                ocorrencias += 1
                i = 0
        else: i = 0
        j += 1
    return ocorrencias

print(KMP([0, 1, 0],  [0, 1, 0, 0, 2, 1, 0, 3, 0, 1, 0, 1, 0, 4, 5, 0, 1, 0, 6, 7, 8, 9, 0, 3, 10, 2, 0, 1, 0,1, 0]))