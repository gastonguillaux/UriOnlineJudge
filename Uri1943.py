cat = [1, 3, 5, 10, 25, 50, 100]
x = 0
valor = int(input())
while valor > cat[x]:
    x += 1
print("Top {}".format(cat[x])) 