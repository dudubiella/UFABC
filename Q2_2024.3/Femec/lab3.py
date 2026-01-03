from lab2 import Esperimento2
class Esperimento3(Esperimento2):
    def momento(self):
        self.massas = [m / 1000 for m in self.massas]
        self.velocidades = [v / 100 for v in self.velocidades]
        self.inctsvelo = [i / 100 for i in self.inctsvelo]
        self.momentos = []
        for m, v in zip(self.massas, self.velocidades[:-1]):
            p = m * v
            self.momentos.append(p)
        pfinal = [self.massas[2] * self.velocidades[-1], self.massas[3] * self.velocidades[-1], (self.massas[1] + self.massas[3]) * self.velocidades[-1]]
        self.momentos.append(pfinal)
        print(f"Momentos:\n{self.momentos}")
        self.inctsmomento = []
        i = 0
        imassa = 0.00001 * 4
        while(i < 4):
            vel = self.velocidades[i]
            iv = self.inctsvelo[i]
            ma = self.massas[i]
            if i > 2:
                j = 0
                imof = []
                while(j < 3):
                    imo = self.momentos[-1][j] * ((iv/vel) ** 2 + (imassa/self.massas[j]) ** 2) ** 0.5
                    imof.append(imo)
                    j += 1
                imo = imof
            else:
                mo = self.momentos[i]
                imo = mo * ((iv/vel) ** 2 + (imassa/ma) ** 2) ** 0.5
            self.inctsmomento.append(imo)
            i += 1
        
        print(f"incertezas:\n{self.inctsmomento}\n")
        return 
    
    def energia(self):
        self.energias = []
        for m, v in zip(self.massas, self.velocidades[:-1]):
            e = m * v * v / 2
            self.energias.append(e)
        efinal = [self.massas[2] * self.velocidades[-1] ** 2 / 2, self.massas[3] * self.velocidades[-1] ** 2 / 2, (self.massas[1] + self.massas[3]) * self.velocidades[-1] ** 2 / 2]
        self.energias.append(efinal)
        print(f"Energias:\n{self.energias}")
        self.inctsenergia = []
        i = 0
        imassa = 0.00001 * 4
        while(i < 4):
            vel = self.velocidades[i]
            iv = self.inctsvelo[i]
            ma = self.massas[i]
            if i > 2:
                j = 0
                ief = []
                while(j < 3):
                    ie = self.energias[-1][j] * (2 * (iv/vel) ** 2 + (imassa/self.massas[j]) ** 2) ** 0.5
                    ief.append(ie)
                    j += 1
                ie = ief
            else:
                e = self.energias[i]
                ie = e * (2 * (iv/vel) ** 2 + (imassa/ma) ** 2) ** 0.5
            self.inctsenergia.append(ie)
            i += 1
        
        print(f"incertezas:\n{self.inctsenergia}")
        return 


def main():
    tempos = [[2.155, 2.152, 2.149], [1.185, 1.262, 1.261], [2.345, 2.509, 2.262], [1.643, 1.559, 1.4]]
    distancias = [[16.8, 21, 18.8], [18.3, 21.8, 19.7]] * 2
    massas = [109.22, 105.66, 111.12, 105]
    esp = Esperimento3(tempos, distancias, massas)
    miD = esp.imprime("Distâncias", esp.dist)
    miT = esp.imprime("Tempos", esp.temp)
    esp.velocidade(miD, miT)
    esp.momento()
    esp.energia()
    return

if __name__ == "__main__":
    main()