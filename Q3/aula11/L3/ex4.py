def padrao (S: [int], T: [int]) -> int:
    i = j = ocorrencias = 0
    while j < len (T):
        if S[i] == T[j]:
            i += 1
            if i == len (S) - 1:
                ocorrencias += 1
                i = 0
        else: i = 0
        j += 1
    return ocorrencias