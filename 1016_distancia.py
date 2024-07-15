
# Distância em Km de diferença por minuto:
diferenca_por_min = 0.5

# Distância em Km informada pelo usuário:
distancia = int(input())

# tempo para a distância informada:
# tempo_para_distancia = distancia / diferenca_por_min
# para evitarmos utilizar um número decimal iremos alterar o algoritmo:
# distacia / 0.5 é igual a distacia * 2. Ou seja:

tempo_para_distancia = distancia * 2


print(f'{tempo_para_distancia} minutos')
