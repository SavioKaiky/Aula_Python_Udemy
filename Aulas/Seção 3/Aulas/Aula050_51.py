"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print(f'A velocidade do veiculo está acima do limite de velocidade. O limite de velocidade é {RADAR_1}')
elif velocidade < RADAR_1:
    print(f'A velocidade do veiculo está no do limite de velocidade. O limite de velocidade é {RADAR_1}')
