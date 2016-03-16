def fatorial(n):
    soma = 1
    for x in range(n, 1, -1):
        soma *= x
    return soma

casos = int(input())
rodadas = []
for x in range(casos):
    base, exp = [int(i) for i in input().split("^")]
    fat = int(input().replace("!", ""))
    if base**exp > fatorial(fat):
        rodadas.append("Lucas")
    else:
        rodadas.append("Pedro")

if rodadas.count("Lucas") > rodadas.count("Pedro"):
    print("Campeao: {}!".format("Lucas"))
elif rodadas.count("Lucas") < rodadas.count("Pedro"):
    print("Campeao: {}!".format("Pedro"))
elif rodadas.count("Lucas") == rodadas.count("Pedro"):
    print("A competicao terminou empatada!")
for x in range(len(rodadas)):
    print("Rodada #{}: {} foi o vencedor".format(x+1,rodadas[x]))