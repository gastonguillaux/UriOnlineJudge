
def teste(num):
    i = 1

    while True:
        if str(num) == '1': return print(1)
        if int(i) % num == 0 and len(i) > 1:
            return print(len(i))
        i += "1"

try:
    while True:
        num = int(input())
        if (num % 2 != 0) and (num % 5 != 0):
            teste(num)
except EOFError:
    pass