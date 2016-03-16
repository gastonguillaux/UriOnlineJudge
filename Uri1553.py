while True:
    d = {}
    total = 0
    en = [int(i) for i in input().split()]
    if en[0] == en[1] == 0: break
    fq = en[1]
    perguntas = [int(i) for i in input().split()]
    uni = set(perguntas)
    for k in uni:
        d[k] = 0
    for j in perguntas:
        d[j] += 1
    for u in d.values():
        if u >= fq: total += 1
    print(total)