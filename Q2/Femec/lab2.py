class Esperimento2:
    def __init__(self, temp, dist, mas) -> None:
        self.temp = temp
        self.dist = dist
        self.massas = mas
    
    def media(self, lista):
        med = sum(lista) / len(lista)
        print(f"média: {med}")
        return med
    
    def incert(self, lista, med):
        inc = (sum([(a - med) ** 2 for a in lista]) / (len(lista) * (len(lista) - 1))) ** 0.5
        print(f"incerteza: {inc}\n")
        return inc
    
    def imprime(self, nome, valores):
        print(f"\n{nome}:\n")
        med = []
        inc = []
        for i, v in enumerate(valores):
            print(f"{nome} {i + 1}:\n{v}")
            medvalor = self.media(v)
            med.append(medvalor)
            instvalor = self.incert(v, medvalor)
            inc.append(instvalor)
        return med, inc

    def velocidade(self, midistancias, mitempos):
        self.meddist, self.incdisr = midistancias
        self.medtemp, self.inctemp = mitempos
        self.velocidades = []
        for d, t in zip(self.meddist, self.medtemp):
            v = d / t
            self.velocidades.append(v)
        print(f"Velocidades:\n{self.velocidades}")
        self.inctsvelo = []
        for v, d, id, t, it in zip(self.velocidades, self.meddist, self.incdisr, self.medtemp, self.inctemp):
            iv = v * ((id/d) ** 2 + (it/t) ** 2) ** 0.5
            self.inctsvelo.append(iv)
        print(f"incertezas:\n{self.inctsvelo}")
        self.medvelo = self.media(self.velocidades)
        self.incvelo = self.incert(self.velocidades, self.medvelo)
        return self.medvelo, self.incvelo

    def acumulado(self, medias, incerts):
        medrela = [0]
        increla = [0]
        for cont in range(len(medias)):
            medrela.append(sum(medias[:cont + 1]))
            increla.append((sum([x ** 2 for x in incerts[:cont + 1]])) ** 0.5)
        print(f"Acumulado:\n{medrela}")
        print(f"Incerteza acumulada:\n{increla}\n")
        return medrela[1:], increla[1:]

    def tabrelativa(self):
        print("Dados Progressivos:\n")
        print("Distância:")
        self.distacum, self.incdistacum = self.acumulado(self.meddist, self.incdisr)
        print("Tempo:")
        self.tempacum, self.inctempacum = self.acumulado(self.medtemp, self.inctemp)
        print("Tempo²:")
        self.temp2acum = [t ** 2 for t in self.tempacum]
        self.inctempacum = [t2 * (2 * (it / t) ** 2) ** 0.5 for t2, t, it in zip(self.temp2acum, self.tempacum ,self.inctempacum)]
        print(f"Acumulado:\n{self.temp2acum}\nIncerteza acumulada:\n{self.inctempacum}\n")
    
    def MMQ(self, inc, x, y):
        print(f"MMQ:\ni = {inc}\nx = {x}\ny = {y}\n")
        varinsert = sum([1 / i ** 2 for i in inc])
        print(f"<σ²> = {varinsert}")
        varx = 1 / varinsert * (sum([x[i] / inc[i] ** 2 for i in range(4)]))
        print(f"<x> = {varx}")
        varx2 = 1 / varinsert * (sum([x[i] ** 2 / inc[i] ** 2 for i in range(4)]))
        print(f"<x²> = {varx2}")
        vary = 1 / varinsert * (sum([y[i] / inc[i] ** 2 for i in range(4)]))
        print(f"<y> = {vary}")
        varxy = 1 / varinsert * (sum([y[i] * x[i] / inc[i] ** 2 for i in range(4)]))
        print(f"<xy> = {varxy}")
        a = (varx * vary - varxy) / (varx ** 2 - varx2)
        ia = (1 / varinsert / (varx2 - varx ** 2)) ** 0.5
        print(f"a = {a}, ∆a = {ia}")
        x0 = vary - a * varx
        ix0 = (varx2 / varinsert / (varx2 - varx ** 2)) ** 0.5
        print(f"b = {x0}, ∆b = {ix0}")        
        
        print(varx * varinsert, varx2 * varinsert, vary * varinsert, varxy * varinsert)
        return

def main():
    tempos = [[0.423, 0.445, 0.529], [0.449, 0.451, 0.419], [0.317, 0.318, 0.325], [0.255, 0.256, 0.261]]
    distancias = [[16.9, 20.2, 18.8], [17.5, 20.9, 19.1], [19, 21.3, 22.5], [18.1, 21.8, 19.9]]
    massas = [109.61, 5.62]
    esp = Esperimento2(tempos, distancias, massas)
    miD = esp.imprime("Distâncias", esp.dist)
    miT = esp.imprime("Tempos", esp.temp)
    esp.velocidade(miD, miT)
    esp.tabrelativa()
    esp.MMQ(esp.incdistacum, esp.temp2acum, esp.distacum)

if __name__ == "__main__":
    main()