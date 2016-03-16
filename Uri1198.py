try:
    while True:
        e = [float(i) for i in input().split()]
        if e[1] > e[0]: 
            print(int(e[1] - e[0]))
        else:
            print(int(e[0] - e[1]))
except EOFError:
    pass