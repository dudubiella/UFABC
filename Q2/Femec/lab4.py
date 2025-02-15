import math
from lab3 import Esperimento3
class Esperimento4(Esperimento3):
    def aceleracao(self):
        self.acel = []
        for v, t in zip(self.velocidades, self.medtemp[:2] + self.medtemp[-1:]):
            a = v / t
            self.acel.append(a)
        print(f"Acelerações:\n{self.acel}")
        self.incacel = []
        for a, v, iv, t, it in zip(self.acel, self.velocidades, self.inctsvelo, self.medtemp[:2] + self.medtemp[-1:], self.inctemp[:2] + self.inctemp[-1:]):
            i = a * ((iv / v) ** 2 + (it / t) ** 2) ** 0.5
            self.incacel.append(i)
        print(f"incertezas:\n{self.incacel}\n")
        return

    def vel_final(self, tempototal):
        self.temptotal = tempototal
        self.velfinal = self.acel[0] * self.temptotal
        print(f"Velocicade Final:\n{self.velfinal}")
        return self.velfinal

    def calcincert(self, med, x, ix, y, iy):
        incerteza = med * ((ix / x) ** 2 + (iy / y) ** 2) ** 0.5
        print(f"incerteza:\n{incerteza}\n")
        return incerteza
    
    def momentoang(self, raio, vel):
        massa = self.massas / 1000
        raio = raio / 100
        vel = vel / 100
        self.momang = massa * raio * vel
        print(f"Momento Angular:\n{self.momang}")
        return self.momang



def main():
    tempos = [[0.505, 0.507, 0.531], [0.551, 0.559, 0.452], [0.329, 0.393, 0.417], [0.265, 0.317, 0.344]]
    distancias = [[16.8, 21, 18.8], [15.7, 17.6, 14], [17.4, 19.2, 15.5]]
    massa = 109.64
    raio = 6
    esp = Esperimento4(tempos, distancias, massa)
    miD = esp.imprime("Distâncias", esp.dist)
    miT = esp.imprime("Tempos", esp.temp)
    temptotal = sum(miT[0][2:])
    inctemptotal = sum([i ** 2 for i in miT[1][2:]]) ** 0.5
    miT = (miT[0][:2]+miT[0][-1:], miT[1][:2]+miT[1][-1:])
    esp.velocidade(miD, miT)
    esp.aceleracao()
    print(f"Tempo Total:\n{temptotal}\nincerteza:\n{inctemptotal}\n")
    velfinal = esp.vel_final(temptotal)
    incvelfin = esp.calcincert(velfinal, esp.acel[0], esp.incacel[0], temptotal, inctemptotal)
    print("Teóricio:")
    esp.momentoang(raio, velfinal)
    esp.calcincert(esp.momang, raio/100, 0.05/100, velfinal/100, incvelfin/100)
    print("Experimental")
    esp.momentoang(raio, esp.velocidades[-1])
    esp.calcincert(esp.momang, raio/100, 0.05/100, esp.velocidades[-1]/100, esp.inctsvelo[-1]/100)
    print("\n\nCOM COLISÃO:\n\n")
    tempos = [[0.505, 0.488, 0.488], [0.456, 0.462, 0.462], [0.508, 0.426, 0.355], [0.433, 0.355, 0.355]]
    distancias = [[16.8, 21, 18.8], [15.7, 17.6, 14], [17.4, 19.2, 15.5]]
    espc = Esperimento4(tempos, distancias, massa)
    miD = espc.imprime("Distâncias", espc.dist)
    miT = espc.imprime("Tempos", espc.temp)
    temptotal = sum(miT[0][2:])
    inctemptotal = sum([i ** 2 for i in miT[1][2:]]) ** 0.5
    miT = (miT[0][:2]+miT[0][-1:], miT[1][:2]+miT[1][-1:])
    espc.velocidade(miD, miT)
    omegas = [2 * math.pi / 0.59, 2 * math.pi / 0.53, 2 * math.pi / 0.5]
    espc.omegas = omegas
    espc.medome = espc.media(omegas)
    espc.income = espc.incert(omegas, espc.medome)
    print(f"Omegas:\n{omegas}\nMedia:\n{espc.medome}\nincerteza:\n{espc.income}\n")
    massacirculo = 54.7 / 1000
    raiomenor = 5.5 / 100
    incraio = 0.05 / 100
    i = (raiomenor ** 2 * massacirculo)/2
    print(f"Momento de Inércia:\n{i}")
    inci = espc.calcincert(i, raiomenor, incraio, raiomenor, incraio)
    momang = i * espc.medome
    print("DISCO:")
    print(f"Momento Angular:\n{momang}")
    incmomang = espc.calcincert(momang, i, inci, espc.medome, espc.income)
    print("CARRINHO")
    momcar = espc.momentoang(6, espc.velocidades[-1])
    incmomc = espc.calcincert(momcar, raio/100, 0.05/100, espc.velocidades[-1]/100, espc.inctsvelo[-1]/100)
    incmomfinal = (incmomang ** 2 + incmomc ** 2) ** 0.5
    print(f"Momento Total:\n{momcar + momang}\nincerteza:\n{incmomfinal}")
    return

if __name__ == "__main__":
    main()