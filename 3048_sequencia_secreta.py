teste = int(input())

coluna = []
for i in range(teste):
    coluna.append(int(input()))

nova_coluna = []
if coluna:
    nova_coluna.append(coluna[0])

for i in range(1, len(coluna)):
    if coluna[i] != coluna[i-1]:
        nova_coluna.append(coluna[i])


print(len(nova_coluna))
