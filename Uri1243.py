def depura(lista):
    spe = "1234567890!@#$%¨&*()_+-=,.;/~]´[<>:?^}`{"
    depurada = []
    for palavra in lista:
        aux = ""
        for letra in palavra:
            if letra not in spe:
                aux += letra
        depurada.append(aux)
    return depurada

try:
    while True:
        en = input().replace(".", " ").split(" ")
        palavras = depura(en)
        media = sum([len(i) for i in palavras])/len(palavras)
        if media <= 3: print(250)
        elif media <= 5: print(500)
        else: print(1000)
except EOFError:
    pass