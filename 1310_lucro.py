def alg_kadane_esp(lista):
    max_atual = max_total = lista[0]
    for i in range(1, len(lista)):
        max_atual = max(lista[i], max_atual + lista[i])
        max_total = max(max_total, max_atual)
    if max_total <= 0:
        return 0
    else:
        return max_total


try:
    while True:
        dias = int(input())
        custo_por_dia = int(input())
        renda_diaria = []

        for i in range(dias):
            renda_diaria.append(int(input()))
            lucro_diario = [i - custo_por_dia for i in renda_diaria]

        print(alg_kadane_esp(lucro_diario))
except EOFError:
    pass
