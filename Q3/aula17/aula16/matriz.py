class Matriz:
    def __init__(self, mat):
        self.mat = mat
        self.lin = len(mat)
        self.col = len(mat[0])

    def Linha(self, n):
        return [i for i in self.mat[n]]

    def Coluna(self, n):
        return [i[n] for i in self.mat]

    def __mul__(self, mat2: [[int]]):
        matResultado = []
        for i in range(self.lin):           
            matResultado.append([])
            for j in range(mat2.col):
                listMult = [x*y for x, y in zip(self.Linha(i), mat2.Coluna(j))]
                matResultado[i].append(sum(listMult))
        return matResultado

    def imprime(self) -> None:
        [print(self.Linha(i)) for i in range(self.lin)]
        return

def main():
    mat1 = Matriz([[2, 3], [4, 6]])
    mat2 = Matriz([[1, 3, 0], [2, 1, 1]])
    mat3 = Matriz(mat1*mat2)
    mat3.imprime()

if __name__ == "__main__":
    main()