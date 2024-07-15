def fib(n):

    if n == 1:
        return 0
    elif n == 2:
        return "0 1"
    else:
        lista_de_saida = ["0", "1"]
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a+b
            lista_de_saida.append(str(b))
        return " ".join(lista_de_saida)


n = int(input())
resultado = fib(n)
print(resultado)
