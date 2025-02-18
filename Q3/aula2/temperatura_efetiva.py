from conversor_de_temps import converteCF, converteFC

def temp_efet (t: float, v:float) -> float:
    sens_termc = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16
    return sens_termc

def valores_validos (ftemp: float, mhvel:float) -> bool:
    if -459.67 <= ftemp and ftemp <= 50 and 3 <= mhvel and mhvel <= 120:
        return True
    else:
        return False

def main (temp: float, vel: float) -> float:
    sens_termc = temp_efet (temp, vel)
    print ('Sensação térmica:', sens_termc)
    return sens_termc

def fmh () -> float:
    valido = False
    while (not (valido)):
        try:
            temp = float (input ('Temperatura em Fahrenheit: '))
            vel = float (input ('Velocidade do vento em mi/h: '))
            if valores_validos (temp, vel):
                valido = True
            else:
                print ('\nValor inválido\n\nLembre-se:\nA temperatura deve ser entre: zero absoluto <= temp <= 50\nA velocidade do vento deve estar entre: 3 <= vel <= 120\n\nTente Novamente\n')
        except:
            print ('\nO valor inserido é inválido, tente novamente\n')
    main (temp, vel)

def ckh ():
    valido = False
    while (not (valido)):
        try:
            temp = converteCF (float (input ('Temperatura em Calsius: ')))
            vel = float (input ('Velocidade do vento em Km/h: ')) * 0.621371
            if valores_validos (temp, vel):
                valido = True
            else:
                print ('\nValor inválido\n\nLembre-se:\nA temperatura deve ser entre: zero absoluto <= temp <= 10\nA velocidade do vento deve estar entre: 1,864113 <= vel <= 74,56452\n\nTente Novamente\n')
        except:
            print ('\nO valor inserido é inválido, tente novamente\n')
    main (temp, vel)
    return



if __name__ == '__main__':
    valido = False
    while (not (valido)):
        tipo = input ('Escolha quais unidades de medida a serem utilizadas:\n1- Fahrenheit, Milhas / Hora\n2- Celsius, Kilômetros / Hora\n')
        if tipo == '1' or tipo == '2':
            valido = True
        else:
            print ('Escolha uma opção válida\n')
    if tipo == '1':
        fmh ()
    else:
        ckh ()