while True:
    palavras = input().split()
    if palavras[0] == "*": break
    letra = palavras[0].lower()[0]
    done = False
    for x in palavras:
        if x.lower()[0] != letra:
            print("N")
            done = True
            break
    if done: continue
    print("Y")