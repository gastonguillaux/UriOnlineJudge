try:
    while True:
        linha = input()
        opera = input()
        mtz = []
        aux = []
        for x in range(144):
            num = float(input())
            aux.append(num)
            if (x + 1) % 12 == 0:
                mtz.append(aux)
                aux = []
        if opera == "S": print(sum(mtz[int(linha)]))
        else: print(sum(mtz[int(linha)])/len(mtz[0]))
except EOFError:
    pass