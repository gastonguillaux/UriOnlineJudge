def contaDigitos(inicio, fim, lista):
    for i in range(inicio, fim + 1):
        aux = str(i)
        for j in aux:
            lista[int(j)] += 1
    
def zeraLista():
    lista = []
    for x in range(10):
        lista.append(0)
    return lista

if __name__ == "__main__":
    #while True:
        lista = zeraLista()
        entrada = [int(x) for x in input().split()]
     #   if entrada[0] == 0 and entrada[1] == 0:
     #       break 
        contaDigitos(entrada[0], entrada[1], lista)
        for k in lista:
            print(k, end=" ")