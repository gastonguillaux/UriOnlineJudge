def checkNum(e):
    if len(e) == 5:
        return print(3)
    else:
        val = 0
        o = 'one'
        for x in range(len(e)):
            if e[x] == o[x]: val += 1
        if val == 2 or val == 3: 
            return print(1)
        else:
            return print(2)
    

if __name__ == "__main__":
    entrada = int(input())
    for x in range(entrada):
        n = input()
        checkNum(n)