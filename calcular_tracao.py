from scipy import constants
import math
gravidade = constants.g


class CalcularTracao:
    def __init__(self, massa, aceleracao_do_motor, secao_cabo = None, fator_de_seguranca = 10, resistencia_do_cabo):
        self.massa = massa
        self.aceleracao_do_motor = aceleracao_do_motor
        self.fator_de_seguranca = fator_de_seguranca
        self.resistencia_do_cabo = resistencia_do_cabo
        if secao_cabo:
            self.secao_cabo = secao_cabo
        else:
            diametro = float(input("Digite o diâmetro do cabo em milimetros: "))
            self.secao_cabo = (math.pi * diametro**2) / 4
            print(f"A seção do cabo é: {self.secao_cabo:.2f} mm²")

    def calcular_massa_max(self):
        

calcular_tracao = CalcularTracao(10, 2)
