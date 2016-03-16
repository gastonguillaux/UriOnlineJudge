# JOGO DOIS OU UM
def verifica2ou1(entrada):
    if entrada[0] == entrada[1] == entrada[2]:
        return print("*")
    if entrada.count(0) < entrada.count(1):
        menor = 0
    else:
        menor = 1

    dic = {0:"A",1:"B",2:"C"}
    return print(dic[entrada.index(menor)])    

if __name__ == "__main__":
    try:
        while True:
            entrada = [int(x) for x in input().split()]
            verifica2ou1(entrada)
    except EOFError:
        pass
    