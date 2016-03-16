def isPrime(num):
    if num % 2 == 0:
        return print("Not Prime") 
    if num > 1:
        for x in range(2, num):
            if (num % x) == 0:
                return print("Not Prime")
        else:
            return print("Prime")
    else:    
        return print("Not Prime")

if __name__ == "__main__":
    casos = int(input())    
    for x in range(casos):
        num = int(input())
        isPrime(num)