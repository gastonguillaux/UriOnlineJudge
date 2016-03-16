casos = int(input())

for x in range(casos):
    s1, s2 = input().split()
    print('encaixa') if (s1[-len(s2):] == s2) else print('nao encaixa')