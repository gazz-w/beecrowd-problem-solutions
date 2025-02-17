
input = int(input())


def top_n(position):
    n = 0
    if position == 1:
        n = 1
    elif position <= 3:
        n = 3
    elif position <= 5:
        n = 5
    elif position <= 10:
        n = 10
    elif position <= 25:
        n = 25
    elif position <= 50:
        n = 50
    else:
        n = 100

    return n


resultado = top_n(input)

print(f"Top {resultado}")
