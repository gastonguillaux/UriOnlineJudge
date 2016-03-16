

if __name__ == "__main__":
    lista = [0,0]
    try:
        while True:
            nome = input()
            #if nome == "0": raise EOFError 
            lista[0] += int(input())
            lista[1] += 1
            
    except EOFError:
        pass
    print(round(lista[0]/lista[1],1))