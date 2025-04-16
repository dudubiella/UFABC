from math import inf as oo
from aula16.matriz import Matriz

class Digrafo:
    def __init__(self, m, w):
        self.M = Matriz(m)
        self.W = Matriz(w)

def main():
    D = Digrafo([[0,1], [0,0]],[[oo, 1],[oo,oo]])
    D.M.imprime()

if __name__ == "__main__":
    main()