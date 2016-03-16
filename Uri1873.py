jogo = {
        'tesoura' : ['papel', 'lagarto'],
        'papel' : ['pedra', 'spock'],
        'pedra' : ['lagarto', 'tesoura'],
        'lagarto' : ['spock', 'papel'],
        'spock' : ['tesoura', 'pedra'],
        }

jogos = int(input())

for x in range(jogos):
    j = input().split()
    if j[1] in jogo[j[0]]:
        print("rajesh".format(x + 1))
    elif j[0] in jogo[j[1]]:
        print("sheldon".format(x + 1))
    else:
        print("empate".format(x + 1))