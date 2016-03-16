try:
    while True:
        en = [int(i) for i in input().split()]
        heroes = [int(i) for i in input().split()]
        divers =[i+1 for i in range(en[0])]
        for k in heroes:
            divers.remove(k)
        if en[0] == en[1]: print("*");
        else:
            for j in divers: print(j, end=" ")
            print()
except EOFError:
    pass