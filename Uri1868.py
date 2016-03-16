class Mapa:
    def __init__(self, n):
        self.lados = ['O' * n for k in range(n)]
        self.tam = n*n
        self.path = []
        for i in range(n):
            self.path.append([])
            for j in range(n):
                self.path[i].append(True)
        
    def imprime(self):
        for x in self.lados: print(x)
        print('@')
        
    def imprimePath(self):
        for x in self.path: print(x)
        print('@')
        
    def caminha(self):
        step = 0
        dire = {
                   "N":{"E":"O", "F":"L"},
                   "S":{"E":"L", "F":"O"},
                   "L":{"E":"N", "F":"S"},
                   "O":{"E":"S", "F":"N"}
                   }

        coluna = linha = int(len(self.path[0])/2)
        
        #while self.tam != 0:
            #if step == 0:
        self.path[linha][coluna] = False
        self.lados[linha] = list(self.lados[linha])
        self.lados[linha][coluna] = 'X'
        self.lados[linha] = ''.join(self.lados[linha])
        self.imprime()
        self.lados[linha] = list(self.lados[linha])
        self.lados[linha][coluna] = 'O'
        self.lados[linha] = ''.join(self.lados[linha])
        self.imprimePath()
        
        self.tam -= 1
        step += 1
        coluna += 1
            
        
    
if __name__ == "__main__":
    n = Mapa(3)
    n.caminha()
    n.imprime()

    
