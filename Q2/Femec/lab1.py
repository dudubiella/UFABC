tempos = [[0.702, 0.656, 0.642], [1.119, 1.050, 1.028], [1.001, 0.938, 0.921], [0.987, 0.902, 0.889]]
distancias = [[16.6, 20.3, 18.5], [17.2, 20.8, 19], [18.9, 22.1, 22.2], [18.5, 21.9, 19.8]]

def media(lista):
    return [sum(a)/len(a) for a in lista]

def incert(list, media):
    return (sum([(a - media) ** 2 for a in list]) / (len(list) * (len(list) - 1))) ** 0.5

def vel(medt, desvt, medd, desvd):
    return (medd/medt) * ((desvt/medt) ** 2 + (desvd/medd) ** 2) ** 0.5

def calculos(valores):
    print(f"medições:")
    for a in valores:
        print(a)
    md = media(valores)
    print(f"media das medições:\n{md}")
    print("incerteza das medição:")
    inser = [incert(t,md[n]) for n, t in enumerate(valores)]
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
dist = []
insdist = []
temp = []
while (i < 4):
    print(f"\nS relativos {i + 1}")
    distrel = sum([medd[a] for a in range(i + 1)])
    dist.append(distrel)
    print(distrel)
    insetdistrel = (sum([desvd[a] ** 2 for a in range(i + 1)])) ** 0.5
    insdist.append(insetdistrel)
    print(insetdistrel)
    print(f"\nT relativos {i + 1}")
    temporel = sum([medt[a] for a in range(i + 1)])
    temp.append(temporel)
    print(temporel)
    insettemporel = (sum([desvt[a] ** 2 for a in range(i + 1)])) ** 0.5
    print(insettemporel)
    i += 1
print("\n\nMMQ\n")
varinsert = sum([1 / i ** 2 for i in insdist])
print(f"<σ²> = {varinsert}")
vart = 1 / varinsert * (sum([temp[i] / insdist[i] ** 2 for i in range(4)]))
print(f"<x> = {vart}")
vart2 = 1 / varinsert * (sum([temp[i] ** 2 / insdist[i] ** 2 for i in range(4)]))
print(f"<x²> = {vart2}")
varl = 1 / varinsert * (sum([dist[i] / insdist[i] ** 2 for i in range(4)]))
print(f"<y> = {varl}")
vartl = 1 / varinsert * (sum([dist[i] * temp[i] / insdist[i] ** 2 for i in range(4)]))
print(f"<xy> = {vartl}")
v = (vart*varl-vartl)/(vart ** 2 - vart2)
iv = (1 / varinsert / (vart2 - vart ** 2)) ** 0.5
print(f"a = {v}, ∆a = {iv}")
x0 = varl - v * vart
ix0 = (vart2 / varinsert / (vart2 - vart ** 2)) ** 0.5
print(f"b = {x0}, ∆b = {ix0}")

