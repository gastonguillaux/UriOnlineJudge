def isPrime(num):
    if num == 0:
        return print("{} nao eh primo".format(num)) 
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                return print("{} nao eh primo".format(num))
        else:
            return print("{} eh primo".format(num))
    else:    
        return print("{} nao eh primo".format(num))

if __name__ == "__main__":
    casos = int(input())    
    for x in range(casos):
        num = int(input())
        isPrime(num)