casos = int(input())
for x in range(casos):
    a, b = input().lower().split()
    changes = 0
    aux = b
    for letra in range(len(b)):
        char = a[letra]
        while char != b[letra]:
            if char == "z":
                char = "a"
                changes += 1
            else:
                char = chr(ord(char) + 1)
                changes += 1
    print(changes)


