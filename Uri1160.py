casos = int(input())
for x in range(casos):
    dados = input().split()
    PA, PB, CA, CB = float(dados[0]), float(dados[1]), float(dados[2]), float(dados[3]) 
    
    anos = 0
    
    while PA <= PB:
        if anos > 100: break
        PA += int((CA * 10 ** -2) * PA)
        PB += int((CB * 10 ** -2) * PB)
        anos += 1
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print("{} anos.".format(anos))