import math

teste = int(input())


id_cidade = 0

while teste != 0:
    id_cidade = id_cidade + 1
    pessoa_consumo = []
    lista_consumo = []
    lista_pessoas = []

    for i in range(teste):
        pessoa, consumo = map(int, input().split())
        consumo_medio = int(consumo/pessoa)
        pessoa_consumo.append([pessoa, consumo_medio])
        lista_consumo.append(consumo)
        lista_pessoas.append(pessoa)
    print(f'Cidade# {id_cidade}:')

    # Ordenar a lista com base no consumo_medio
    pessoa_consumo.sort(key=lambda x: x[1])

    arr = [f'{pessoa}-{consumo_medio}' for pessoa,
           consumo_medio in pessoa_consumo]

    for i in range(len(arr)):
        if i == len(arr)-1:
            print(arr[i])
        else:
            print(arr[i], end=' ')

    # print(pessoa_consumo)
    consumo_medio_total = 100*(sum(lista_consumo)/sum(lista_pessoas))
    consumo_medio_total_formatado = math.floor(consumo_medio_total)/100
    print(f'Consumo medio: {consumo_medio_total_formatado:.2f} m3.')

    teste = int(input())
