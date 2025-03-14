def andar_cavalo (n: int, x: int, y: int, z: int, w: int):
    def move(r):
        match r:
            case 0: return (2, 1)
            case 1: return (2, -1)
            case 2: return (-2, 1)
            case 3: return (-2, -1)
            case 4: return (1, 2)
            case 5: return (-1, 2)
            case 6: return (1, -2)
            case 7: return (-1, -2)
    
    def dentro(n: int, x: int, y: int, i: int, j: int):
        return 1 <= x + i <= n and 1 <= y + j <= n 
    
    if x == z and y == w: return True

    for a in range(8):
        (i, j) = move(a)
        if dentro:
            if x + i == z and y + j == w: return True
            x0, y0 = x + i, y + j
            for b in range(8):
                (k, l) = move(b)
                if dentro(n, x0, y0, k, l) and x0 + k == z and y0 + l == w: return True
    return False