def phex(n,c):
    dec = int(n,16)
    bina = bin(dec)
    print("Case {}:".format(c))
    print("{} dec".format(dec))
    print("{} bin".format(bina)[2:])
    print()

def pbin(n,c):
    dec = int(n, 2)
    hexa = hex(dec)
    print("Case {}:".format(c))
    print("{} dec".format(dec))
    print("{} hex".format(hexa)[2:])
    print()

def pdec(n,c):
    aux = int(n)
    hexa = hex(aux)
    bina = bin(aux)
    print("Case {}:".format(c))
    print("{} hex".format(hexa)[2:])
    print("{} bin".format(bina)[2:])
    print()

if __name__ == "__main__":
    d = {"bin": "0b", "hex": "0x","dec": ""}
    casos = int(input())
    for x in range(casos):
        num, tipo = input().split()
        if tipo == "bin": pbin(num, x+1)
        elif tipo == "hex": phex(num, x+1)
        elif tipo == "dec": pdec(num, x+1)