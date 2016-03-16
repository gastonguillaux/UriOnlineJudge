casos = int(input())
for x in range(casos):
    tam = int(input())
    soma = 0
    for j in range(tam):
        if j % 2 == 0:
            soma += 1
        else:
            soma -= 1
    print(soma)