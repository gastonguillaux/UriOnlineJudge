from operator import xor
try:
    while True:
        en = [int(i) for i in input().split()]
        print(xor(en[0], en[1]))
except EOFError:
    pass