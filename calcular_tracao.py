from scipy import constants
import math
gravidade = constants.g

# RESISTENCIA DO CABO EM MPA, SECAO DO CABO EM MM², MASSA EM KG, ACELERACAO DO MOTOR EM M/S².
class CalcularTracao:
    def __init__(self, massa=None, aceleracao_do_motor=None,resistencia_do_cabo=None, secao_cabo=None, fator_de_seguranca = 10):
        self.massa = massa
        self.aceleracao_do_motor = aceleracao_do_motor
        self.fator_de_seguranca = fator_de_seguranca #PADRAO = 10. CONSULTE MANUAIS PARA O SABER QUAL O MAIS INDICADO PARA SEU PROCESSO
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

        if secao_cabo:
            self.secao_cabo = secao_cabo
        else:
            diametro = float(input("Digite o diâmetro do cabo em milimetros: "))
            self.secao_cabo = (math.pi * diametro**2) / 4
            print(f"A seção do cabo é: {self.secao_cabo:.2f} mm²")

    def calcular_limite(self):
        limite = self.resistencia_do_cabo / self.fator_de_seguranca
        return limite
    
    def calcular_massa_max(self,aceleracao=None):
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
        print(gravidade)
        return massa_max

calcular_tracao = CalcularTracao()
print(calcular_tracao.calcular_massa_max())
