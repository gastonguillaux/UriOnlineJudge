def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
casos = int(input())
for x in range(casos):
    a, b = input().split()
    a, b = int(a), int(b)
    if a > b:
        print(gcd(int(a), int(b)))
    else:
        print(gcd(int(b), int(a)))