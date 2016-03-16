while True:
    vezes = int(input())
    if vezes == 0: break
    else:
        jogadas = [int(i) for i in input().split()]
        gamers = {"Mary": 0, "John": 0}
        for x in jogadas:
            if x == 0: gamers["Mary"] += 1
            else: gamers["John"] += 1
        print("Mary won {} times and John won {} times".format(gamers["Mary"], gamers["John"]))
            