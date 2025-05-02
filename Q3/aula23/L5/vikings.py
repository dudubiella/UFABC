def ler_inteiros () -> [int]:
    return list (map (int, input().split()))

def ler_letras () -> [str]:
    return input().strip().split()

def codificar (letras):
    alfabeto = [chr (i) for i in range (ord ('A'), ord ('Z') + 1)]
    saida = []
    for letra in letras:
        pos = alfabeto.index (letra) + 1  # posição baseada em 1
        saida.append (pos)
        alfabeto = [letra] + alfabeto[:pos-1] + alfabeto[pos:]
    return saida

def decodificar (mensagem_codificada: [int]) -> [str]:
    alfabeto = [chr (i) for i in range (ord ('A'), ord ('Z') + 1)]
    resultado = []
    for pos in mensagem_codificada:
        letra = alfabeto[pos - 1]
        resultado.append (letra)
        alfabeto = [letra] + alfabeto[:pos - 1] + alfabeto[pos:]
    return ''.join (resultado)

def main ():
    instancia = 1
    while True:
        m = int (input())
        if m == 0:
            break
        codificada = ler_inteiros ()
        decodificada = decodificar (codificada)
        print (f"Instancia {instancia}\n{decodificada}\n")
        instancia += 1
    return

if __name__ == "__main__":
    main ()