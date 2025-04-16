def busca_binaria (x, v):
    e, d = -1, len(v)
    while e < d-1:
        m = (e + d) / 2
        if v[m] < x:
            e = m
        else:
            d = m
    return d

#O código de busca binária apresentado esta errado, pois ao determinar o valor de "m" não foi itilizado o quociente inteiro (//) da divisão de (e + d) por 2, então ao não é possível encontrar o valor de "v[m]", pois m deve ser um inteiro.

#Código corrigido da busca binária

def busca_binaria_correto (x, v):
    e, d = -1, len(v)
    while e < d-1:
        m = (e + d) // 2
        if v[m] < x:
            e = m
        else:
            d = m
    return d

#a)

def busca_binaria_correto_a_1 (x, v):
    e, d = -1, len(v)
    while e < d:
        m = (e + d) // 2
        if v[m] < x:
            e = m
        else:
            d = m
    return d

def busca_binaria_correto_a_2 (x, v):
    e, d = -1, len(v)
    while e <= d-1:
        m = (e + d) // 2
        if v[m] < x:
            e = m
        else:
            d = m
    return d

#Se o código (correto) for alterado para o "while e < d" ou para "while e <= d-1" o código apresentará um erro em sua lógica, pois ao longo do loop, o while nunca encontraria um valor "False", entrando em um loop infinito, tal que se d - e == 1 então (m = (e + d) // 2) seria equivalente a (m = (e + (e + 1)) // 2) que seria equivalente a e, desta forma, se não encontrado o valor "x", nunca será alterando os valores de d ou e, então o while entra em um loop infinito

#b)

def busca_binaria_correto_b_1 (x, v):
    e, d = -1, len(v)
    while e <= d-1:
        print(e, d, v)
        m = (d - e) // 2
        if v[m] < x:
            e = m
        else:
            d = m
    return d

# Se o código (correto) for alterado para o "(e + d - 1)//2", o valor de m não seria o meio entre "d" e "e", desta forma podendo nunca encontrar o valor que é buscado pois mesmo se ele estiver na lista, o m chegaria a valor j - 1 (poderia chegar apenas um indice antes do correto), entrando em um loop infinito. Se for alterado para o "(d - e)//2" o valor de m não seria a metade ente os valores de "d" e "e", pois calculou-se a metade da diferença entre eles, desta forma, mesmo alterando os valores que decidem o while, o loop nunca chegaria ao fim, entrando em um loop infinito

#c)

def busca_binaria_correto_c (x, v):
    e, d = -1, len(v)
    while e < d-1:
        m = (e + d) // 2
        if v[m] <= x:
            e = m
        else:
            d = m
    return d

# Se o código (correto) for alterado para o "if (v[m] <= x)", ao longo do while o código funcionaria corretamente, se o valor buscado não estiver na lista: o código funciona assim como antes, retornando um indice j tal que o x porcurado estaria entre v[j-1] e v[j]. Porém, se o valor estiver na lista, o código retornaria um indice errado, tal que se o valor procurado esta no indece i, o código erroniamente retornaria sempre i + 1.

#d)

def busca_binaria_correto_d_1 (x, v):
    e, d = -1, len(v)
    while e < d-1:
        print(e,d,v)
        m = (e + d) // 2
        if v[m] < x:
            e = m
        else:
            d = m + 1
    return d

def busca_binaria_correto_d_2 (x, v):
    e, d = -1, len(v)
    while e < d-1:
        print(e,d,v)
        m = (e + d) // 2
        if v[m] < x:
            e = m
        else:
            d = m - 1
    return d

# Se o código (correto) for alterado para o "d = m+1" podem ocorrer duas coisas, se o x procurado for maior que o ultimo valor da lista v[-1], o código apresentaria o mesmo resultado que antes (len(v)), pois a linha alterada nunca seria executada. Se o x não for maior que o maior valor de v, o código entraria em um loop infinito pois o e nunca seria maior que o d - 1 se o d fosse igual a m + 1. Se for alterado para o "d = m-1" o código sempre retornaria um valor errado, tal que se o valor esperado de retorno é o indice i, o valor devolvido erroniamente seria i - 1, se o x procurado não for maior que o maior valor presente em v (se x > v[-1] o valor retornado estaria correto ja que a linha alterada nunca seria executada).