cha = int(input())

a, b, c, d, e = map(int, input().split())

respostas = [a, b, c, d, e]

count = 0
for i in respostas:
    if i == cha:
        count += 1

print(count)
