x = int(input())
while True:
    z = int(input())
    if z > x:
        count = 0
        soma = 0
        for j in range(x,z):
            soma += j
            count += 1
            if soma > z:
                print(count) 
                break
        break
    