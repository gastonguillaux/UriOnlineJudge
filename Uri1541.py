import math

while True:
    dados = [int(i) for i in input().split()]
    if dados[0] == 0: break
    if dados[2] == 100:
        print(int((dados[0]*dados[1])**0.5))
    else:
        a = dados[0]*dados[1]
        b = a * (100/dados[2])
        print(int(math.sqrt(b)))
        