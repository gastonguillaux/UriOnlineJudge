casos = int(input())

for x in range(casos):
    o = int(input())
    soma = 0
    for j in range(1,o):
        if o % j == 0:
            soma += j
    if o == soma:
        print("{} eh perfeito".format(o)) 
    else:
        print("{} nao eh perfeito".format(o))