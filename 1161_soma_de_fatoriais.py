def fatorial(n):
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


try:
    while True:
        m, n = map(int, input().split())
        soma_fatoriais = fatorial(m) + fatorial(n)
        print(soma_fatoriais)
except EOFError:
    pass
