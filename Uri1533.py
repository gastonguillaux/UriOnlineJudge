
if __name__ == "__main__":
    try:
        while True:
            procurado = int(input())
            
            if procurado == 0: break
            lista = []
            for y in range(procurado):
                lista.append(int(input()))
                    
            if (procurado in lista):
                print(lista.index(procurado) + 1)
    except EOFError:
        pass