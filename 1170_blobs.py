criatura = "Blobs"

teste = int(input())


def come_metade(comida):
    contador = 0
    while comida > 1:
        comida /= 2
        contador += 1
    return contador


for i in range(teste):
    dias = come_metade(float(input()))
    print(f'{dias} dias')
