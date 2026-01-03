#b)

def sub_list(N: list[int]) -> list[list[int]]:
    def recursao(inicio: int, M: list[int]) -> None:
        if M: resultado.append(M.copy())
        for i in range(inicio, len(N)):
            M.append(N[i])
            recursao(i + 1, M)
            print(M)
            M.pop()
    resultado = []
    recursao(0, [])
    return resultado

#a)

def n_sub_list (n: int) -> [[int]]:
    N = list(range(1, n + 1))
    return sub_list (N)

print(n_sub_list(3))