casos = int(input())
for k in range(casos):
    num = int(input())
    print(bin(num)[2:].count("1"))