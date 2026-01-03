from aula19.aula18.matriz import Matriz, imprime_mat
class Eq:
    def __init__ (self, A: [[float]], b: [float]):
        self.A = Matriz(A)
        self.b = b
        self.n = len(b)
    
    def x (self) -> [float]:
        self.X = [0] * (self.n)
        for i in reversed (range (self.n)):
            self.X[i] = (self.b[i] - sum(self.A.mat[i][j] * self.X[j] for j in range(i+1, self.n)))
        return self.X

    def pivotacao (self):
        def pivo(k = 0):
            if self.n == k: return
            for i in range(k + 1, self.n):
                mult = -self.A.mat [i][k] / self.A.mat [k][k]
                print(mult)
                for j in range(k, self.n):
                    self.A.mat [i][j] = mult * self.A.mat [k][j] + self.A.mat [i][j]
                    imprime_mat(self.A.mat)
        self.A = pivo()

def main() -> None:
    e = Eq([[1, 2, 3], [2, 4, 5], [4, 0, 6]], [3, 2, 1])
    e.pivotacao()

if __name__ == "__main__":
    main()