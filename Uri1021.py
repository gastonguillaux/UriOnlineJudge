def trocoNotas(n, me):
    notas = {
             100: 0 ,
             50: 0 ,
             20: 0 ,
             10: 0 ,
             5: 0 ,
             2: 0 
             }
    while n > 1:
        if n >= 100:
            notas[100] += 1
            n -= 100
        elif n >= 50:
            notas[50] += 1
            n -= 50
        elif n >= 20:
            notas[20] += 1
            n -= 20
        elif n >= 10:
            notas[10] += 1
            n -= 10            
        elif n >= 5:
            notas[5] += 1
            n -= 5
        elif n >= 2:
            notas[2] += 1
            n -= 2
    l = sorted(notas,reverse=True)
    print("NOTAS:")
    for x in l:
        print("{} nota(s) de R$ {:.2f}".format(notas[x], round(float(x),2)))
    me += n
    return me
    
def trocoMoedas(m):
    moedas = {
             1 : 0 ,
             0.5 : 0 ,
             0.25 : 0 ,
             0.10 : 0 ,
             0.05 : 0 ,
             0.01 : 0 
             }
    while m != 0.00:
        if m >= 1:
            moedas[1] += 1
            m -= 1
        elif m >= 0.5:
            moedas[0.5] += 1
            m -= 0.5
            m = round(m,2)
        elif m >= 0.25:
            moedas[0.25] += 1
            m -= 0.25
            m = round(m,2)
        elif m >= 0.10:
            moedas[0.10] += 1
            m -= 0.10
            m = round(m,2)
        elif m >= 0.05:
            moedas[0.05] += 1
            m -= 0.05
            m = round(m,2)
        elif m >= 0.01:
            moedas[0.01] += 1
            m -= 0.01
            m = round(m,2)
    k = sorted(moedas,reverse=True)
    print("MOEDAS:")
    for j in k:
        print("{} moeda(s) de R$ {:.2f}".format(moedas[j], round(float(j),2)))
    
if __name__ == "__main__":
    valor = float(input())
    notas = int(valor)
    moedas = round(valor - int(valor),2)
    trocoMoedas(trocoNotas(notas, moedas))
    