import math

def bhaskara (a: float, b: float, c: float) -> (int, float, float):
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        return (2, x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return (1, x, x)
    else:
        return (0, math.nan, math.nan)
    
if __name__ == '__main__':
    valido = False
    while (not (valido)):
        try:
            print("Digite os valores a serem aplicados na formula de Bhaskara")
            a = float (input ("a = "))
            b = float (input ("b = "))
            c = float (input ("c = "))
            valido = True
        except:
            print("\nValor inválido, tente novamente\n")
    n, x1, x2 = bhaskara(a, b, c)
    match n:
        case 0:
            print('Não possui raizes reais')
        case 1:
            print('Raiz dupla:', x1)
        case _:
            print('Raizes:', x1, 'e', x2)