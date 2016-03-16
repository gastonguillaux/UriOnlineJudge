matrizes = int(input())
casos = 4
for x in range(matrizes):
    dimensoes = int(input())
    matriz = []
    tamanhos = 0
    for y in range(dimensoes):
        linha = [int(i)*int(i) for i in input().split()]
        matriz.append(linha)
        if y == 0:
            tamanhos = [len(str(k)) for k in linha]
        else:
            for j in range(len(linha)):
                if len(str(linha[j])) > tamanhos[j]:
                    tamanhos[j] = len(str(linha[j]))

    print("Quadrado da matriz #{}:".format(casos))
    casos += 1
    for line in matriz:
        for num in range(len(line)):
            print(str(line[num]).rjust(tamanhos[num]),end=" ")
        print()
    print()