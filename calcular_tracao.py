from scipy import constants
import math
gravidade = constants.g

# RESISTENCIA DO CABO EM MPA, SECAO DO CABO EM MM², MASSA EM KG, ACELERACAO DO MOTOR EM M/S².
class CalcularTracao:
    def __init__(self, diametro_tambor, massa, aceleracao_do_motor, resistencia_do_cabo=None, secao_cabo=None, fator_de_seguranca=10, diametro_cabo=None):
        self.diametro_tambor = diametro_tambor
        self.massa = massa
        self.aceleracao_do_motor = aceleracao_do_motor 
        self.fator_de_seguranca = fator_de_seguranca  # Padrão = 10

        if resistencia_do_cabo:
            self.resistencia_do_cabo = resistencia_do_cabo
        else:
            while True:
                tipo_cabo = input("Digite o tipo do cabo (Aço de alta resistência, Aço Inox (AISI316), Aço Comum, Cobre Revestido, Nylon/Poliamida): ").lower().split()
                if any(p in ("alta", "resistência", "resistencia") for p in tipo_cabo):
                    self.resistencia_do_cabo = 1770
                    break
                elif any(p == "inox" for p in tipo_cabo):
                    self.resistencia_do_cabo = 1570
                    break
                elif any(p == "comum" for p in tipo_cabo):
                    self.resistencia_do_cabo = 1370
                    break
                elif any(p == "cobre" for p in tipo_cabo):
                    self.resistencia_do_cabo = 200
                    break
                elif any(p in ("nylon", "poliamida") for p in tipo_cabo):
                    self.resistencia_do_cabo = 90
                    break
                else:
                    print("Tipo de cabo não conhecido / não cadastrado. Tente novamente.")

        # Trata o diâmetro e a seção transversal do cabo (mm e mm²)
        if secao_cabo is not None:
            self.secao_cabo = secao_cabo
            self.diametro_cabo = math.sqrt((4 * secao_cabo) / math.pi)
        elif diametro_cabo is not None:
            self.diametro_cabo = diametro_cabo
            self.secao_cabo = (math.pi * (diametro_cabo ** 2)) / 4
        else:
            self.diametro_cabo = float(input("Digite o diâmetro do cabo em milímetros: "))
            self.secao_cabo = (math.pi * (self.diametro_cabo ** 2)) / 4
            print(f"A seção do cabo é: {self.secao_cabo:.2f} mm²")

    def calcular_limite(self):
        limite_nominal = self.resistencia_do_cabo / self.fator_de_seguranca
        relacao_diametro_cabo_e_tambor = self.diametro_tambor/self.diametro_cabo
        if relacao_diametro_cabo_e_tambor >= 11.2:
            perca = (1)-(1/(relacao_diametro_cabo_e_tambor)**0.9)
            limite = limite_nominal * perca
        else:
            return 'Não é possível aplicar o cálculo segundo a ISO 16625:2025'
        return limite
    
    def calcular_massa_max(self):
        limite = self.calcular_limite()
        if self.aceleracao_do_motor:
            self.aceleracao_do_motor = aceleracao
            acel = self.aceleracao_do_motor
        else:
            while True:
                try:
                    acel = float(input("Insira a aceleração estimada: (em m/s²): "))
                    break
                except ValueError:
                    print("tente novamente. Não use ','. Utilize '.' no lugar. Não utilize strings")

        massa_max =  (limite * self.secao_cabo) / (gravidade + acel)
        return massa_max
    def calcular_tracao(self):
        tracao = (self.massa * (gravidade+ self.aceleracao_do_motor))/ self.secao_cabo
        return tracao
    def percentual_tracao_max_atual(self):
        tracao_atual = self.calcular_tracao()
        tracao_maxima = self.calcular_limite()
        percentual = (tracao_atual / tracao_maxima) * 100
        return percentual


calcular_tracao = CalcularTracao(diametro_tambor=113.2, diametro_cabo=4.7,resistencia_do_cabo=1370,secao_cabo=17.35,aceleracao_do_motor=10,massa=10)
c = calcular_tracao.percentual_tracao_max_atual()
print(c)