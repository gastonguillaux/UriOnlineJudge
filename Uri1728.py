while True:
    eq, res = input().split("=")
    a,b = eq.split("+")
    x = int(a[::-1])
    y = int(b[::-1])
    z = int(res[::-1])
    print((x+y) == z)
    if x == y == z == 0: break