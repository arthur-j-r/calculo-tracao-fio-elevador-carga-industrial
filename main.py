import csv
from calcular_tracao import SrElevador

def carregar_dados(arquivo='dados_elevador.csv'):
    try:
        with open(arquivo, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                if not any(linha.values()):
                    continue
                
                # Retorna imediatamente a primeira instância criada
                return SrElevador(
                    diametro_tambor=float(linha['diametro_tambor_mm']),
                    resistencia_do_cabo=float(linha['resistencia_cabo_mpa']),
                    secao_cabo=float(linha['secao_cabo_mm2']),
                    diametro_cabo=float(linha['diametro_cabo_mm']),
                    fator_de_seguranca=float(linha['fator_seguranca']),
                    aceleracao_do_motor=float(linha['aceleracao_motor_ms2']),
                    massa=float(linha['massa'])
                )
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None


if __name__ == "__main__":
    dados = carregar_dados()
    
    if dados:
        tracao = dados.calcular_tracao()
        print(f"Tração: {tracao:.2f} MPa")