try:
    while True:
        dados = [int(i) for i in input().split()]
        print(dados[0] * dados[1] * 2)
except EOFError:
    pass