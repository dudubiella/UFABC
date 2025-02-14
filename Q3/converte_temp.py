def converte(x):
    f = 9 / 5 * x + 32
    print(f'O valor equivalente a {x} graus celius em Fahrenheit é: {f} graus\n{x} C -> {f} F\n')
    return f

def main():
    valido = False
    while(not(valido)):
        c = (input('Digite seu valor (ou conjuto de valores separados por virgulas) em graus Calsius para ser transformada em Fahrenheit:\n'))
        try:
            c = float(c)
            valido = True
        
        except:
            try:
                if c != '':
                    conjunto = c.split(',')
                    c = [float(x) for x in conjunto]
                    valido = True
                else:
                    print('Nenhum valor foi incerido :(\nTente Novamente\n')
            except:
                print('Valor inválido :(\nTente Novamente\n')
    if type(c) is float:
        f = converte(c)
    else:
        f = []
        for x in c:
            y = converte(x)
            f.append(y)
    return f

if __name__ == '__main__':
    main()