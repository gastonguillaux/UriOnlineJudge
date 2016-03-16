try:
    while True:
        lados = [float(i) for i in input().split()]
        lados.sort()
        lados = lados[::-1]
        a, b, c = lados[0], lados[1], lados[2]
        if a >= (b + c):
            print("NAO FORMA TRIANGULO")
            continue
        if (a*a) == ((b*b) + (c*c)): print("TRIANGULO RETANGULO")
        if (a*a) > ((b*b) + (c*c)): print("TRIANGULO OBTUSANGULO")
        if (a*a) < ((b*b) + (c*c)): print("TRIANGULO ACUTANGULO")
        if a == b == c: print("TRIANGULO EQUILATERO")
        elif a == b or a == c or b == c: print("TRIANGULO ISOSCELES")
except EOFError:
    pass