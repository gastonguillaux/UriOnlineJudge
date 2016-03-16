def fatorial(numero):
    soma = 1
    for x in range(numero,0,-1):
        soma = soma * x
    return soma

if __name__ == "__main__":
    try:
        while True:
            entrada = [int(i) for i in input().split()]
            print(fatorial(entrada[0]) + fatorial(entrada[1]))
    except EOFError:
        pass