while True:
    casos = int(input())
    gab = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", -1: "*"}
    if casos == 0: break
    for j in range(casos):
        respostas = [int(i) for i in input().split()]
        answer = []
        for x in respostas:
            if x <= 127:
                answer.append(x)
        if len(answer) == 1: print(gab[respostas.index(answer[0])])
        else: print(gab[-1])