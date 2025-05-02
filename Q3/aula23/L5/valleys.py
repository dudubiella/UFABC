def ler_inteiros () -> [int]:
    return list (map (int, input().split()))

def encontrar_vales (grid: [[int]], m: int, n: int) -> [(int, int)]:
    potencial_vale = [[True] * n for _ in range (m)]
    for i in range (m):
        for j in range (n):
            if potencial_vale[i][j]:
                # verifica direita
                if j + 1 < n:
                    if grid[i][j] > grid[i][j+1]:
                        potencial_vale[i][j] = False
                    elif grid[i][j] < grid[i][j+1]:
                        potencial_vale[i][j+1] = False
                # verifica abaixo
                if i + 1 < m:
                    if grid[i][j] > grid[i+1][j]:
                        potencial_vale[i][j] = False
                    elif grid[i][j] < grid[i+1][j]:
                        potencial_vale[i+1][j] = False
    vales = []
    for i in range (m):
        for j in range (n):
            if potencial_vale[i][j]:
                vales.append ((i+1, j+1))
    return vales

def main ():
    instancia = 1
    while True:
        m, n = ler_inteiros ()
        if m == 0 and n == 0:
            break
        grid = [ler_inteiros () for _ in range (m)]
        vales = encontrar_vales (grid, m, n)
        print (f"Instancia {instancia}")
        for x, y in vales:
            print (x, y)
        print ()
        instancia += 1
    return

if __name__ == "__main__":
    main ()