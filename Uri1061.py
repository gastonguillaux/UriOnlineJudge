#CALCULA A DURACAO DE UM EVENTO

def calculaDuracao(inicio, fim):
    duracao = [0, 0, 0, 0]
    while inicio != fim:
        inicio[3] += 1
        duracao[3] += 1
        
        # SEGUNDOS
        if inicio[3] == 60:
            inicio[2] += 1
            inicio[3] = 0

        if duracao[3] == 60:
            duracao[2] += 1
            duracao[3] = 0
            
        # MINUTOS
        if inicio[2] == 60:
            inicio[1] += 1
            inicio[2] = 0

        if duracao[2] == 60:
            duracao[1] += 1
            duracao[2] = 0
            
        # HORAS
        if inicio[1] == 24:
            inicio[0] += 1
            inicio[1] = 0

        if duracao[1] == 24:
            duracao[0] += 1
            duracao[1] = 0
    return duracao

if __name__ == "__main__":
    dia = input().split()
    dia = int(dia[1])
    horas = [int(i) for i in input().split(":")]
    inicio = [dia, horas[0], horas[1], horas[2]]
    
    dia = input().split()
    dia = int(dia[1])
    horas = [int(i) for i in input().split(":")]
    fim = [dia, horas[0], horas[1], horas[2]]
    r = calculaDuracao(inicio, fim)
    print("{} dia(s)".format(r[0]))
    print("{} hora(s)".format(r[1]))
    print("{} minuto(s)".format(r[2]))
    print("{} segundo(s)".format(r[3]))