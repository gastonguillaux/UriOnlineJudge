casos = int(input())
for x in range(casos):
    a, b = input().split()
    if a[len(a)-len(b):len(a)] == b:
        print('encaixa')
    else:
        print('nao encaixa')