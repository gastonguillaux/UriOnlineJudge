if __name__ == "__main__":
    casos = int(input())
    
    for x in range(casos):
        ataques = int(input())
        tiros = [int(i) for i in input().split()]
        golpes = input()
        
        pontos = 0
        for j in range(ataques):
            if tiros[j] < 3 and  golpes[j] == 'S':
                pontos += 1
            elif tiros[j] >= 3 and golpes[j] == 'J':
                pontos += 1
        print(pontos)