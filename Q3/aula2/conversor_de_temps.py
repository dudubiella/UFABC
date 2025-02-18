def converteCF (c: float) -> float:
    f = 9 / 5 * c + 32
    return f

def converteFC (f: float) -> float:
    c = (f - 32) / 9 * 5
    return c

def conversor (x: float, de: str) -> float:
    if de == 'Celsius':
        f = converteCF (x)
        print (f'O valor equivalente a {x} graus Celsius em Fahrenheit é: {f} graus\n{x} C -> {f} F\n')
        return f
    else:
        c = converteFC (x)
        print (f'O valor equivalente a {x} graus Fahrenheit em Celsius é: {c} graus\n{x} F -> {c} C\n')
        return 

def convertetemps (tipo: int) -> float:
    if tipo == 1:
        de = 'Celsius'
        para = 'Fahrenheit'
    else:
        de = 'Fahrenheit'
        para = 'Celsius'
    valido = False
    while (not (valido)):
        x = (input (f'Digite seu valor (ou conjuto de valores separados por virgulas) em graus {de} para ser transformada em {para}:\n'))
        try:
            x = float(x)
            valido = True
        
        except:
            try:
                if x != '':
                    conjunto = x.split (',')
                    x = [float(x) for x in conjunto]
                    valido = True
                else:
                    print ('Nenhum valor foi incerido :(\nTente Novamente\n')
            except:
                print ('Valor inválido :(\nTente Novamente\n')
    if type (x) is float:
        convertido = conversor (x, de)
    else:
        convertido = []
        for valor in x:
            resultado = conversor (valor, de)
            convertido.append (resultado)
    return convertido

if __name__ == '__main__':
    valido = False
    while (not (valido)):
        tipo = input ('Escolha a conversão entre os casos:\n1- Celsius -> Fahrenheit\n2- Fahrenheit -> Celsius\n')
        if tipo == '1' or tipo == '2':
            valido = True
        else:
            print ('Escolha uma opção válida\n')
    convertetemps (int (tipo))
