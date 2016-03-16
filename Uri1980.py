def anagramas(tam_palavra):
     total = 1
     while tam_palavra != 0:
         total *= tam_palavra
         tam_palavra -= 1
     return total

while True:
    palavra = input()
    if palavra == "0": break
    print(anagramas(len(palavra)))
