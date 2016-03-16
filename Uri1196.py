try:
    ref = {}
    c = ['qwertyuiop[]','asdfghjkl;\'\\','\\zxcvbnm,./','1234567890-=']
    for x in c:
        for j in range(1,len(x),1):
            # ref[x[j]] = x[j - 1]
            ref[x[j].upper()] = x[j - 1].upper()

    while True:
        codex = input()
        output = ""
        for x in range(len(codex)):
            if codex[x] == ' ': output += ' '
            else: output += ref[codex[x]]
        print(output + '\n')

except EOFError:
    pass