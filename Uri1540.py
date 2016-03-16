casos = int(input())
for k in range(casos):
    ano1, taxa1, ano2, taxa2 = [int(i) for i in input().split()]
    if ano2 - ano1 == 0: anos = 1
    else: anos = ano2 - ano1
    res = str(round((taxa2 - taxa1)/anos,6)).replace(".",",")[:-4]
    print(res)