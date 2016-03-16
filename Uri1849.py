def maior(a, b):
    if a > b: return a
    else: return b

def menor(a, b):
    if a < b: return a
    else: return b

try:
    while True:
        en = [int(i) for i in input().split()]
        a1, a2, b1, b2 = en
        if maior(a1, a2) == maior(b1, b2): print(maior(a1,a2)*maior(a1,a2))
        elif menor(a1, a2) == maior(b1, b2): print(menor(a1,a2)*menor(a1,a2))
        elif maior(a1, a2) == menor(b1, b2): print(maior(a1,a2)*maior(a1,a2))
        elif menor(a1, a2) == menor(b1, b2): print(menor(a1,a2)*menor(a1,a2))
        else:
            m = menor(maior(a1,a2), maior(b1,b2))
            print(m*m)
except EOFError:
    pass