while True:
    casos = int(input())
    if casos == 0: break
    maior = 0
    l = []
    for x in range(casos):
        l.append(input())
        if len(l[x]) > maior: maior = len(l[x])
    for k in range(len(l)):
        print(l[k].rjust(maior))
    print()    
        
    