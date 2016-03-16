res = {
       "empate" : 0,
       "inter" : 0,
       "gremio" : 0,
       "jogos" : 0,
       }
while True:
    res['jogos'] += 1
    
    placar = [int(i) for i in input().split()]
    
    if placar[0] > placar[1]:
        res['inter'] += 1
    elif placar[1] > placar[0]:
        res['gremio'] += 1
    else:
        res['empate'] += 1
        
    n = input("Novo grenal (1-sim 2-nao)\n")
    
    if n == '2': break
print("{} grenais".format(res['jogos']))
print("Inter:{}".format(res['inter']))
print("Gremio:{}".format(res['gremio']))
print("Empates:{}".format(res['empate']))

if res['inter'] > res['gremio']:
    print("Inter venceu mais")
elif res['gremio'] > res['inter']:
    print("Gremio venceu mais")
else:
    print('Nao houve vencedor')