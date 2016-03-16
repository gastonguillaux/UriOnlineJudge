try:
    while True:
        en = [int(i) for i in input().split()]
        if len(en) > 1: tam, num = en[0], en[1]
        else: tam, num = 0, 0
        soma = 0
        if tam == 0:
            print("{} sim".format(soma))
        else:
            for i in str(num): soma += int(i)
            if soma % 3 != 0:
                print("{} nao".format(soma))
            else:
                print("{} sim".format(soma))
except EOFError:
    pass
