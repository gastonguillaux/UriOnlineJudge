def acima(lista, media):
    a = 0
    for x in lista:
        if x > media: a += 1
    return a

casos = int(input())
for x in range(casos):
    dados = [int(i) for i in input().split()]
    media = sum(dados[1:])/dados[0]
    print('{0:.3f}%'.format((acima(dados[1:], media)/dados[0])*100))