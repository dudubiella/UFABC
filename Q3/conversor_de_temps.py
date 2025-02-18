def converteCF(x):
    f = 9 / 5 * x + 32
    print(f'O valor equivalente a {x} graus Celsius em Fahrenheit é: {f} graus\n{x} C -> {f} F\n')
    return f

def converteFC(x):
    c = (x - 32) / 9 * 5
    print(f'O valor equivalente a {x} graus Fahrenheit em Celsius é: {c} graus\n{x} F -> {c} C\n')
    return c

def converte(x, de):
    if de == 'Celsius':
        return converteCF(x)
    else:
        return converteFC(x)

def convertetemps(tipo):
    if tipo == 1:
        de = 'Celsius'
        para = 'Fahrenheit'
    else:
        de = 'Fahrenheit'
        para = 'Celsius'
    valido = False
    while(not(valido)):
        c = (input(f'Digite seu valor (ou conjuto de valores separados por virgulas) em graus {de} para ser transformada em {para}:\n'))
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
        f = converte(c, de)
    else:
        f = []
        for x in c:
            y = converte(x, de)
            f.append(y)
    return f

if __name__ == '__main__':
    valido = False
    while(not(valido)):
        tipo = input("escolha a conversão entre os casos:\n1- Celsius -> Fahrenheit\n2- Fahrenheit -> Celsius\n")
        if tipo == '1' or tipo == '2':
            valido = True
        else:
            print('Escolha uma opção válida\n')
    convertetemps(int(tipo))
