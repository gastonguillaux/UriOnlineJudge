
if __name__ == "__main__":
    casos = int(input())
    preco = 0
    peso = 0
    for x in range(casos):
        preco += float(input())
        frutas = input().split()
        peso += len(frutas)
        print("day {}: {} kg".format(x+1, len(frutas))) 
    print("{} kg by day".format(round(peso/casos,2)))
    print("R$ {} by day".format(round(preco/casos,2)))   