from math import inf as oo
from aula16.matriz import Matriz, imprime_mat

class Digrafo:
    def __init__ (self, m, w):
        self.M = Matriz (m)
        self.W = Matriz (w)
    
    def existe_caminho_tam_n (self, a: int, b: int, n: int):
        chega = self.M
        for _ in range (n - 1):
            chega *= self.M
            if chega.mat[a][b] == 1:
                return True
        return False
    
    def peso_a_to_b (self, a: int, b: int):
        # w * w (soma = multiplicação, multiplicação = min)
        return

    def USSSP (self, s: int):
        d = [oo] * (n := self.M.lin); d[s] = 0
        p = [j for j in range (n)]
        Q = [s]
        while Q != []:
            i = Q.pop (0)
            for j in range(n):
                if self.M.mat[i][j] and d[i] + 1 < d[j]:
                    d[j] = d[i] + 1
                    p[j] = i
                    Q.append (j)
        self.d, self.p = d, p
        return

    def BFS (self, s: int) -> [int]:
        self.USSSP(s)
        return self.d

    def print_path (self, s: int, t: int, vez = 0) -> None:
        self.USSSP(s)
        if self.p[t] == t: 
            print (t, end = " ")
        else:
            self.print_path (s, self.p[t], 1)
            print ("-->", t, end = " ")
        if vez == 0: print()
        return
    
    def is_connected (self) -> bool:
        d = self.BFS (0)
        return all (di < oo for di in d)

def main() -> None:
    D = Digrafo([[0, 1, 1], [0, 0, 1], [1, 0, 0]], [[oo, 1, 4], [oo, oo, 2], [3, oo, oo]])
    D.print_path(2,1)
    print(D.is_connected())

if __name__ == "__main__":
    main()