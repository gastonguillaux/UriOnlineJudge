def calcula_placar():
    p1 = 0
    p2 = 0
    placar1 = input().split()
    if int(placar1[0]) > int(placar1[2]):
        p1 += 3
        return p1, p2
    elif int(placar1[0]) < int(placar1[2]):
        p2 += 3
        return p1, p2
    else:
        return  p1, p2

if __name__ == "__main__":
    casos = int(input())
    for x in range(casos):
        j1a = 0
        j1b = 0
        j2a = 0
        j2b = 0
        j1a, j1b = calcula_placar()
        j2b, j2a = calcula_placar()
        time1 = j1a + j2a
        time2 = j1b + j2b
        if time1 > time2:
            print("Time 1")
        elif time1 < time2:
            print("Time 1")
        else:
            print("Penaltis")