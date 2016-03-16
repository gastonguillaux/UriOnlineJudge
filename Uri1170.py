casos = int(input())
for x in range(casos):
    kg = float(input())
    dias = 0
    while kg > 1:
        kg = kg/2
        dias += 1
    print("{} dias".format(dias))