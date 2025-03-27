def seq_zeros (A: [int]) -> (int, int, int):
    init_seq = 0
    maior_seq0 = (0, 0, 0)
    valor_ant = -1
    for i in range (len (A)):
        if valor_ant != 0 and A[i] == 0:
            init_seq = i
        elif A[i] != 0:
            seq = i - init_seq
            if seq > maior_seq0[0]: maior_seq0 = (seq, init_seq, i)
        elif i == len (A) - 1:
            seq = i - init_seq + 1
            if seq > maior_seq0[0]: maior_seq0 = (seq, init_seq, i + 1)
        valor_ant = A[i]

    return maior_seq0