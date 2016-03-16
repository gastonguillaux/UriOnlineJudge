#ESQUERDA VOLVER

direcao = {
         "N":{"E":"O", "D":"L"},
         "S":{"E":"L", "D":"O"},
         "L":{"E":"N", "D":"S"},
         "O":{"E":"S", "D":"N"}
         }

while True:
    tamanho = int(input())
    if tamanho == 0: break
    d = input()
    olhar = "N"
    for i in d:
        olhar = direcao[olhar][i]
    print(olhar)