#CALCULA A DURACAO DE UM EVENTO

def calculaDuracao(inicio, fim):
        duracao = [0, 0]
        if inicio == fim:
            print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
        else:
            while inicio != fim:
                inicio[1] += 1
                duracao[1] += 1
                            
            # MINUTOS
                if inicio[1] == 60:
                    inicio[0] += 1
                    inicio[1] = 0
        
                if duracao[1] == 60:
                    duracao[0] += 1
                    duracao[1] = 0
                # HORAS    
                if inicio[0] == 24:
                    inicio[0] = 0

            print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao[0], duracao[1]))
                
    

if __name__ == "__main__":
    dados = [int(i) for i in input().split()]
    inicio = [dados[0], dados[1]]
    fim = [dados[2], dados[3]]
    calculaDuracao(inicio, fim)