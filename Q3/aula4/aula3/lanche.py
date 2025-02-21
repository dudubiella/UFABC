def preco (k: int, n: int, p: float, q: float) -> float:
    combo = min(k, n)
    return combo * (p + q) * 0.8 + (k - combo) * p + (n - combo) * q

if __name__ == '__main__':
    cafe = int(input('Quant. cafés: '))
    salgado = int(input('Quant. salgados: '))
    pcafe = float(input('Preço cafés: '))
    psalgado = float(input('Preço salga: '))
    preco ()