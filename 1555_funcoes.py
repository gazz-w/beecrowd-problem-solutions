teste = int(input())


def comparar(r, b, c):
    if r > b and r > c:
        print("Rafael ganhou")

    if b > r and b > c:
        print("Beto ganhou")

    if c > b and c > r:
        print("Carlos ganhou")


for i in range(teste):
    x, y = map(int, input().split())

    r = ((3*x)**2)+(y**2)
    b = 2*(x**2)+((5*y)**2)
    c = -100*x + (y**3)

    comparar(r, b, c)
