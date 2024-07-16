
produtos = {}
produtos['1001'] = 1.50
produtos['1002'] = 2.50
produtos['1003'] = 3.50
produtos['1004'] = 4.50
produtos['1005'] = 5.50

teste = int(input())


def calcula_preco(codigo, quantidade):
    resultado = produtos[codigo] * quantidade
    return resultado


valor_da_compra = 0
for i in range(teste):
    codigo, quantidade = (input().split())
    valor_da_compra += calcula_preco(codigo, float(quantidade))


print(f'{valor_da_compra:.2f}')
