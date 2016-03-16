while True:
    en = [int(i) for i in input().split()]
    if en[0] == en[1] == 0: break
    soma = en[0] + en[1]
    print(str(soma).replace("0", ""))