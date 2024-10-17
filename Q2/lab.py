tempos = [[0.968, 0.940, 0.948], [1.029, 0.992, 1.003], [2.038, 1.873, 2.006], [1.527, 1.329, 1.300]]
distancias = [[16, 17.5, 13.8], [15.7, 17.6, 14], [28.8, 30, 26.4], [17.4, 19.2, 15.5]]

def media(lista):
    return [sum(a)/len(a) for a in lista]

def incert(list, media, n = False):
    if n:
        return (sum([(a - media) ** 2 for a in list]) / (len(list) * (len(list) - 1))) ** 0.5
    else:
        return (sum([(a - media) ** 2 for a in list]) / (len(list) - 1)) ** 0.5

def vel(medt, desvt, medd, desvd):
    return (medd/medt) * ((desvt/medt) ** 2 + (desvd/medd) ** 2) ** 0.5

def calculos(valores):
    print(f"medições:")
    for a in valores:
        print(a)
    md = media(valores)
    print(f"media das medições:\n{md}")
    print("incerteza das medição:")
    if len(valores) == 1:
        inser = [ incert(t,md[n], True) for n, t in enumerate(valores)]
    else:
        inser = [ incert(t,md[n]) for n, t in enumerate(valores)]
    print(inser)
    return md, inser

print("TEMPOS\n")
medt, desvt = calculos(tempos)
print("\n\nDISTANCIAS\n")
medd, desvd = calculos(distancias)
print("\n\nVELOCIDADES\n")
velo = [d/t for t, d in zip(medt, medd)]
desvvel = [vel(t, de, d, dd) for t, de, d, dd in zip(medt, desvt, medd, desvd)]
print(velo, "\n", desvvel)
print("\n\nVELOCIDADE TOTAL\n")
medvelo, desvvelo = calculos([velo])
print("\n\nACUMULADOS\n")
i = 0
while (i < 4):
    print(f"\nS relativos {i + 1}")
    distrel = sum([medd[a] for a in range(i + 1)])
    print(distrel)
    insetdistrel = (sum([desvd[a] ** 2 for a in range(i + 1)])) ** 0.5
    print(insetdistrel)
    print(f"\nT relativos {i + 1}")
    temporel = sum([medt[a] for a in range(i + 1)])
    print(temporel)
    insettemporel = (sum([desvt[a] ** 2 for a in range(i + 1)])) ** 0.5
    print(insettemporel)
    i += 1
