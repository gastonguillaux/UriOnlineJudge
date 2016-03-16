'''
def maiorMenor(lista):
    if int(lista[0]) > int(lista[1]):
        lista[0] = 1
        lista[1] = 0
        return lista
    elif int(lista[0]) < int(lista[1]):
        lista[0] = 0
        lista[1] = 1
        return lista  
    if int(lista[0]) == int(lista[1]):
        lista[0] = 0
        lista[1] = 0
        return lista
    
def main():
    v = 1
    while v != 0:
        v = int(input())
        j1 = 0
        j2 = 0 
        for i in range(v):
            t = input().split()
            a = maiorMenor(t)
            if (a[0] > 0):
                j1 += 1
            elif a[1] > 0:
                j2 += 1
        print(str(j1) + " " + str(j2))
        

if __name__ == "__main__": main()
'''
while True:
    casos = int(input())
    if casos == 0: break
    resultado = [0,0]
    for x in range(casos):
        lista = [int(i) for i in input().split()]
        if lista[0] > lista[1]: resultado[0] += 1
        elif lista[0] < lista[1]: resultado[1] += 1
        elif lista[0] == lista[1]: 
            resultado[0] += 0
            resultado[1] += 0
    print("{} {}".format(resultado[0], resultado[1])) 
        
            