class Matriz:
    def __init__( self, mat: [[float]]):
        self.mat = mat
        self.lin = len (mat)
        self.col = len (mat[0])

    def Linha (self, n: int):
        return [i for i in self.mat[n]]

    def Coluna (self, n: int):
        return [i[n] for i in self.mat]

    def __mul__ (self, mat2: [[float]]) -> [[float]]:
        matResultado = []
        for i in range (self.lin):           
            matResultado.append ([])
            for j in range (mat2.col):
                listMult = [x * y for x, y in zip (self.Linha (i), mat2.Coluna (j))]
                matResultado[i].append (sum (listMult))
        resultado = Matriz (matResultado)
        return resultado
    
    def __add__ (self, mat2: [[float]]) -> [[float]]:
        if self.lin != mat2.lin or self.col != mat2.col: return [[]]
        matResultado = [[x + y for x, y in zip (self.Linha (i), mat2.Linha (i))]for i in range(self.lin)]
        resultado = Matriz (matResultado)
        return resultado


def imprime_mat (M: [[float]]) -> None:
    try: [print (M.Linha(i)) for i in range (M.lin)]
    except: [print (M[i]) for i in range (len (M))]
    return

def main () -> None:
    mat1 = Matriz ([[2, 3, 2], [4, 6, 0]])
    mat2 = Matriz ([[1, 3, 0], [2, 1, 1]])
    mat3 = mat1*mat2
    imprime_mat (mat3)

if __name__ == "__main__":
    main ()