teste = int(input())


def is_prime(n):
    if n <= 1:
        return "Not Prime"
    elif n <= 3:
        return "Prime"
    elif n % 2 == 0:
        return "Not Prime"
    i = 3
    while i * i <= n:
        if n % i == 0:
            return "Not Prime"
        i += 2
    return "Prime"


for i in range(teste):
    valida = is_prime(int((input())))
    print(valida)
