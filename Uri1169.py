casos = int(input())
for x in range(casos):
    casas = int(input())
    gramas = (2 ** (casas)) /12
    print("{} kg".format(int(gramas/1000)))
