def menor(a, b):
    if len(a) < len(b): return len(a)
    else: return len(b)

def maior(a, b):
    if len(a) > len(b): return len(a)
    else: return len(b)

def maiors(a, b):
    if len(a) > len(b): return a[::-1]
    else: return b[::-1]

while True:
    a, b = input().split()
    if a == b == '0': break
    aux1 = a[::-1]
    aux2 = b[::-1]
    aux3 = 0
    aux4 = maiors(a,b)
    carry = 0
    for x in range(maior(a,b)):
        if x < menor(a,b):
            if int(aux1[x]) + int(aux2[x]) + aux3 >= 10:
                carry += 1
                aux3 = 1
            elif int(aux1[x]) + int(aux2[x]) + aux3 < 10:
                aux3 = 0
        else:
            if int(aux4[x]) + aux3 >= 10:
                carry += 1
                aux3 = 1
            elif int(aux4[x]) + aux3 < 10:
                aux3 = 0
    if carry != 0 and carry != 1:
        print("{} carry operations.".format(carry))
    elif carry == 1:
        print("{} carry operation.".format(carry))
    else:
        print("No carry operations.")