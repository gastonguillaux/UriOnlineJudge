def contaMinutos(entrada):
    inicio = [entrada[0], entrada[1]]
    fim = [entrada[2], entrada[3]]
    minutos = 0
    while inicio != fim:
        inicio[1] += 1
        minutos += 1 
        if inicio[1] == 60:
            inicio[0] += 1
            inicio[1] = 0
        if inicio[0] == 24:
            inicio[0] = 0
    return minutos

if __name__ == "__main__":
    while True:
        dados = [int(i) for i in input().split()]
        if dados[0] == dados[1] == dados[2] == dados[3] == 0: break 
        print(contaMinutos(dados))
    