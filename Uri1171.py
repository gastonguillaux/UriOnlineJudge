'''
class No:
    def __init__(self, data = None, prox = None):
        self.data = data
        self.prox = prox

class ListaLigada:
    def __init__(self, no_atual = None):
        self.no_atual = no_atual
        self.cabeca = no_atual
    
    def insere(self, data):
        novo_no = No(data, self.no_atual)
        self.no_atual = novo_no
        if self.cabeca == None:
            self.cabeca = novo_no
    
    def imprime(self):
        no = self.cabeca
        while no:
            print(no.data)
            no = no.prox

l = ListaLigada()
l.insere(10)
l.insere(20)
l.insere(30)
l.insere(30)
l.imprime()

'''

if __name__ == "__main__":
    casos = int(input())
    lista = {}
    for x in range(casos):
        num = input()
        if num in lista:
            lista[num] += 1
        else:
            lista[num] = 1
    
    numeros = sorted([int(i) for i in sorted(lista)])
    
    for x in range(len(numeros)):
        print("{} aparece {} vez(es)".format(numeros[x], lista[str(numeros[x])]))




