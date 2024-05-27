# include <stdio.h>

teste = int(input())


def count_diamonds(entrada):
    pilha_diamantes = []
    diamantes = 0

    for char in entrada:
        if char == '<':
            pilha_diamantes.append(char)
        elif char == '>' and pilha_diamantes:
            pilha_diamantes.pop()
            diamantes += 1
    print(diamantes)


for i in range(teste):
    entradas = str(input())
    count_diamonds(entradas)
