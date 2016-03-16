def cria_matriz():
    mtz = []
    for x in range(9):
        mtz.append([int(i) for i in input().split()])
    return mtz

def soma_quad(m):
    q1 = sum(m[0][0:3]) + sum(m[1][0:3]) + sum(m[2][0:3])
    if q1 != 45: return False
    q2 = sum(m[0][3:6]) + sum(m[1][3:6]) + sum(m[2][3:6])
    if q2 != 45: return False
    q3 = sum(m[0][6:9]) + sum(m[1][6:9]) + sum(m[2][6:9])
    if q3 != 45: return False

    q4 = sum(m[3][0:3]) + sum(m[4][0:3]) + sum(m[5][0:3])
    if q4 != 45: return False
    q5 = sum(m[3][3:6]) + sum(m[4][3:6]) + sum(m[5][3:6])
    if q5 != 45: return False
    q6 = sum(m[3][6:9]) + sum(m[4][6:9]) + sum(m[5][6:9])
    if q6 != 45: return False

    q7 = sum(m[6][0:3]) + sum(m[7][0:3]) + sum(m[8][0:3])
    if q7 != 45: return False
    q8 = sum(m[6][3:6]) + sum(m[7][3:6]) + sum(m[8][3:6])
    if q8 != 45: return False
    q9 = sum(m[6][6:9]) + sum(m[7][6:9]) + sum(m[8][6:9])
    if q9 != 45: return False
    return True

if __name__ == "__main__":
    casos = int(input())
    for q in range(casos):
        scolunas = [0,0,0,0,0,0,0,0,0]
        lista = cria_matriz()
        for linha in lista:
            if sum(linha) != 45:
                print("Instancia {}".format(q + 1))
                print("NAO\n")
                continue
            aux = [sum(k) for k in zip(linha, scolunas)]
            scolunas = aux

        nao_passou = False
        for u in range(len(scolunas)):
            if scolunas[u] != 45:
                print("Instancia {}".format(q + 1))
                print("NAO\n")
                nao_passou = True
                break
        if nao_passou: continue

        if soma_quad(lista):
            print("Instancia {}".format(q + 1))
            print("SIM\n")
        else:
            print("Instancia {}".format(q + 1))
            print("NAO\n")