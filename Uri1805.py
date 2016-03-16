gap = [int(i) for i in input().split()]
soma = ((gap[0] + gap[1]) * (gap[1] - gap[0] + 1))/2
'''for j in range(gap[0], gap[1] + 1, 1):
    soma += j
'''
print(int(soma))