jogo = {
        'tesoura' : ['papel', 'lagarto'],
        'papel' : ['pedra', 'Spock'],
        'pedra' : ['lagarto', 'tesoura'],
        'lagarto' : ['Spock', 'papel'],
        'Spock' : ['tesoura', 'pedra'],
        }

jogos = int(input())

for x in range(jogos):
    j = input().split()
    if j[1] in jogo[j[0]]:
        print("Caso #{}: Bazinga!".format(x + 1))
    elif j[0] in jogo[j[1]]:
        print("Caso #{}: Raj trapaceou!".format(x + 1))
    else:
        print("Caso #{}: De novo!".format(x + 1))