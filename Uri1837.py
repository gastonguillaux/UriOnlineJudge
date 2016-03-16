# THIS PROGRAM JUST PRINTS THE DIVISION OF TWO NUMBERS AND
# ITS REMINDER VALUE OF ITS MODULAR DIVISION
'''
if __name__ == "__main__":
    vezes = int(input())
    for x in range(vezes):
        s = input()
        if s[0] == s[2]:
            print(int(s[0]) * int(s[2]))
        elif s[1].isupper():
            print(int(s[2]) - int(s[0]))
        else:
            print(int(s[0]) + int(s[2]))
'''

try:
    while True:
        en = [int(i) for i in input().split()]
        a, b = en[0], en[1]
        r = a % b
        if r < 0:
            r = r - b
        q = int((a-r)/b)

        print(q, end=" ")
        print(r)
except EOFError:
    pass

