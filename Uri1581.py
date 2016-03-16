'''
Created on Sep 28, 2015
CODE BELOW CHECK IF ITENS IN A LIST ARE THE SAME OR DIFFERENT

@author: Gast�nMauricio
'''
def linguas():
    idiomas = []
    duplicado = False
    quantidade = input()
    for i in range(int(quantidade)):
        idiomas.append(input())
        if i > 0 and idiomas[i] != idiomas[i-1]:
            duplicado = True
    if (duplicado):
        print("ingles")
    else:
        print(idiomas[0])
    
if __name__ == '__main__':
    vezes = int(input())
    for k in range(vezes):
        linguas()